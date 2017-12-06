from ConfigurationManager import ConfigurationManager
from os.path import join
from os import getcwd
from utilities import get_samples_matrix
from numpy import where
import pickle
import csv
from evaluation import evaluate

# deserialization of classifier object
classifier_file = open("classifier_data",'rb')
classifier = pickle.load(classifier_file)
classifier_file.close()

# deserialization of parametrizer object
parametrizer_file = open("parametrizer_data",'rb')
parametrizer = pickle.load(parametrizer_file)
parametrizer_file.close()

# testing
test_manager = ConfigurationManager(join(getcwd(),"test"))
test_filenames = test_manager.training_data(0)
for filename in test_manager.test_data(0):
    test_filenames.append(filename)
test_data = get_samples_matrix(test_filenames, parametrizer)

prediction = classifier.predict(test_data)

#Writing to csv file
with open('results.csv', 'w',newline='') as csvfile:
    result_writer=csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i,file in enumerate(test_filenames):
        file=file[(len(file)-7):]
        probability=max(prediction[i])
        answer = where(prediction[i,:]==probability)[0][0]
        result_writer.writerow([file] + [answer] + [probability])

evaluate()