from ConfigurationManager import ConfigurationManager
from os import getcwd
from os.path import join

manager = ConfigurationManager(join(getcwd(),"train"))
print("number of all people:")
print(len(manager.persons))
print("train data:")
print(len(manager.training_data(0)))
print(manager.training_data(2))
print("test data:")
print(len(manager.test_data(0)))
print(manager.test_data(0))
