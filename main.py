from ConfigurationManager import ConfigurationManager
from os.path import join
from os import getcwd
from MFCCParametrizer import MFCCParametrizer
from ANNClassifier import ANNClassifier
from ResultHandler import ResultHandler
from WavFile import WavFile

# Main program loop

def get_answers(data):
    answers = []
    for string in data:
        answers.append(string[len(string)-6])
    return answers

def get_answer(data):
    return data[len(data)-6]

configuration_manager = ConfigurationManager(join(getcwd(),"train"))
parametrizer = MFCCParametrizer()
classifier = ANNClassifier((200,200,190,100,50,25,10,4,2))
result_handler = ResultHandler(['0','1','2','3','4','5','6','7','8','9'])

for i in range(0,configuration_manager.nb_configurations()):
    # training
    train_filenames = configuration_manager.training_data(i)
    train_data = []
    for train_filename in train_filenames:
        audio = WavFile(train_filename)
        fs, samples = audio.data(normalize=False)
        parameters = parametrizer.parameters(samples, fs)
        train_data.append(parameters)
    classifier.train(train_data,get_answers(train_data))

    # testing
    test_filenames = configuration_manager.test_data(i)
    test_answers = get_answers(test_filenames)
    test_data = []
    for test_filename in test_filenames:
        audio = WavFile(test_filename)
        fs, samples = audio.data(normalize=False)
        parameters = parametrizer.parameters(samples, fs)
        test_data.append(parameters)
    for i,input in enumerate(test_data):
        result_handler.add_result(classifier.predict(input),test_answers[i])

print(result_handler.classes_)
print(classifier.MLPClassifier.classes_)
print(result_handler.error_rate)
