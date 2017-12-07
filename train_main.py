from ConfigurationManager import ConfigurationManager
from os.path import join
from os import getcwd
from MFCCParametrizer import MFCCParametrizer
from ANNClassifier import ANNClassifier
from utilities import *
import pickle


training_manager = ConfigurationManager(join(getcwd(),"train"))
parametrizer = MFCCParametrizer(appendEnergy=False, numcep=18, nfft=1024, nfilt=26, ceplifter=27)
classifier = ANNClassifier((220,110),activation_function='logistic',solver='adam',alpha=0.0001, nb_iterations=200)

# training
train_filenames = training_manager.training_data(0)
for filename in training_manager.test_data(0):
    train_filenames.append(filename)
train_data = get_samples_matrix(train_filenames, parametrizer)

classifier.train(train_data,get_answers(train_filenames))

# serialization of the classifier object
classifier_file = open("classifier_data",'w+b')
pickle.dump(classifier,classifier_file)
classifier_file.close()

# serialization of the parametrizer object
parametrizer_file = open("parametrizer_data",'w+b')
pickle.dump(parametrizer,parametrizer_file)
parametrizer_file.close()