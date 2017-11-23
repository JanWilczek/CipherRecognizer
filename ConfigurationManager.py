from os import listdir
from os import getcwd
from os.path import isfile, join
import numpy as np

class ConfigurationManager:
    def __init__(self, foldername, test_persons_percentage):
        self.foldername = foldername
        self.filenames = [f for f in listdir(self.foldername) if isfile(join(self.foldername,f)) and f.endswith(".wav")]
        persons = set()
        for filename in self.filenames:
            persons.add(filename[:2])
        self.persons = []
        for person in persons:
            self.persons.append(person)
        self.nb_test_persons = int(len(self.persons) * test_persons_percentage / 100)
        self.__generate_configurations()

    def __generate_configurations(self):
        self.__configurations_dictionary = {}
        conf_number = 0
        for i in range(0,len(self.persons)-self.nb_test_persons + 1):
            test_file_indexes = []
            for j in range(i, i+self.nb_test_persons):
                test_file_indexes.append(j)
            self.__configurations_dictionary[conf_number] = test_file_indexes
            conf_number += 1

    def nb_configurations(self):
        return len(self.__configurations_dictionary)

    def test_data(self, configuration_id):
        test_filenames = []
        for i in self.__configurations_dictionary[configuration_id]:
            for filename in self.filenames:
                if (filename.startswith(self.persons[i])):
                    test_filenames.append(join(self.foldername,filename))
        return test_filenames

    def training_data(self, configuration_id):
        training_filenames = []
        for i in self.__configurations_dictionary[configuration_id]:
            for filename in self.filenames:
                if not (filename.startswith(self.persons[i])):
                    training_filenames.append(join(self.foldername,filename))
        return training_filenames







manager = ConfigurationManager(join(getcwd(),"train"),20)
print("number of all people:")
print(len(manager.persons))
print("test data:")
print(len(manager.test_data(2)))
print("train data:")
print(len(manager.test_data(2)))