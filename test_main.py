from ConfigurationManager import ConfigurationManager
from os.path import join
from os import getcwd
from MFCCParametrizer import MFCCParametrizer
from ANNClassifier import ANNClassifier
from ResultHandler import ResultHandler
from WavFile import WavFile
import pickle
import csv
from Evaluation import evaluate


def get_answers(data):
    answers = []
    for string in data:
        answers.append(string[len(string)-6])
    return answers

def get_answer(data):
    return data[len(data)-6]

# deserialization of classifier object
classifier_file = open("classifier_data",'rb')
classifier = pickle.load(classifier_file)

parametrizer = MFCCParametrizer(appendEnergy=False, numcep=18)

result_handler = ResultHandler()
# testing
test_manager = ConfigurationManager(join(getcwd(),"test"))
test_filenames = test_manager.training_data(0)
for filename in test_manager.test_data(0):
    test_filenames.append(filename)
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
filename = "OutsideTestRun.xls"
sheet_name = "Sheet1"
result_handler.write_results_to_excel_file(filename,sheet_name)

#Writing to csv file
with open('results.csv', 'w',newline='') as csvfile:
    result_writer=csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    i=0
    for file in test_filenames:
        file=file[(len(file)-7):]
        probability=max(prediction[i])
        for a in range (0,10):
            if probability==prediction[i,a] :
                answer=a
        result_writer.writerow([file] + [answer] + [probability])
        i=i+1
classifier_file.close()

evaluate()