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
result_handler = ResultHandler()
#['0' '1' '2' '3' '4' '5' '6' '7' '8' '9']
for i in range(0,configuration_manager.nb_configurations()):
    #classifier = ANNClassifier((200,200,190,100,50,25,10,4,2))
    classifier = ANNClassifier()
    # training
    train_filenames = configuration_manager.training_data(i)
    train_data = []
    for train_filename in train_filenames:
        audio = WavFile(train_filename)
        fs, samples = audio.data(normalize=False)
        super_vector = parametrizer.super_vector(samples, fs)
        train_data.append(super_vector)
    classifier.train(train_data,get_answers(train_filenames))

    # testing
    test_filenames = configuration_manager.test_data(i)
    test_answers = get_answers(test_filenames)
    test_data = []
    for test_filename in test_filenames:
        audio = WavFile(test_filename)
        fs, samples = audio.data(normalize=False)
        super_vector = parametrizer.super_vector(samples, fs)
        test_data.append(super_vector)
    prediction = classifier.predict(test_data)
    for i,input in enumerate(prediction):
        result_handler.add_result(prediction[i],test_answers[i])
    result_handler.classes_ = classifier.MLPClassifier.classes_

print(result_handler.error_rate())

result_handler.write_results_to_excel_file("InitialRun.xls","Sheet1")
