from os import listdir
from os.path import isfile, join

# Leave One Out configurator
class ConfigurationManager:
    def __init__(self, foldername):
        self.foldername = foldername

        # Create a list of all .wav files in the folder
        self.filenames = [f for f in listdir(self.foldername) if isfile(join(self.foldername,f)) and f.endswith(".wav")]

        # Extract a list of persons in the folder
        persons = set()
        self.__persons_dictionary = {}
        for filename in self.filenames:
            persons.add(filename[:2])
        persons = sorted(persons)
        self.persons = []
        for person in persons:
            self.persons.append(person)
            self.__persons_dictionary[person] = []

        # Create a dictionary of all persons' recordings
        for filename in self.filenames:
            self.__persons_dictionary[self.__person_name(filename)].append(filename)

    def __belongs_to(self,person,filename):
        return (person == filename[:2])

    def __person_name(self,filename):
        return filename[:2]

    def nb_configurations(self):
        return len(self.persons)

    def test_data(self, configuration_id):
        test_data = []
        for filename in self.__persons_dictionary[self.persons[configuration_id]]:
            test_data.append(join(self.foldername,filename))
        return test_data

    def training_data(self, configuration_id):
        training_data = []
        for filename in self.filenames:
            if not (self.__belongs_to(self.persons[configuration_id],filename)):
                training_data.append(join(self.foldername,filename))
        return training_data



