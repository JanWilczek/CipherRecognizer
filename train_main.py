from ConfigurationManager import ConfigurationManager
from os.path import join
from os import getcwd
from MFCCParametrizer import MFCCParametrizer
from ANNClassifier import ANNClassifier
from ResultHandler import ResultHandler
from WavFile import WavFile
import pickle


# Main program loop

def get_answers(data):
    answers = []
    for string in data:
        answers.append(string[len(string)-6])
    return answers

def get_answer(data):
    return data[len(data)-6]

training_manager = ConfigurationManager(join(getcwd(),"train"))
parametrizer = MFCCParametrizer(appendEnergy=False, numcep=18)

result_handler = ResultHandler()

classifier = ANNClassifier((240,120),activation_function='logistic',solver='adam',alpha=0.0001, nb_iterations=200)

# training
train_filenames = training_manager.training_data(0)
for filename in training_manager.test_data(0):
    train_filenames.append(filename)
train_data = []
for train_filename in train_filenames:
    audio = WavFile(train_filename)
    fs, samples = audio.data(normalize=False)
    super_vector = parametrizer.super_vector(samples, fs)
    train_data.append(super_vector)
classifier.train(train_data,get_answers(train_filenames))

# serialization of classifier object
classifier_file = open("classifier_data",'w+b')
pickle.dump(classifier,classifier_file)
classifier_file.close()