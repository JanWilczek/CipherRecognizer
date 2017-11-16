# CipherRecognizer

## by Jan Jasiński and Jan Wilczek
##### &copy; Jan Jasiński and Jan Wilczek 2017

Cipher recognition software.

### Classes overview

1. GlobalParameters:
   - a singleton class containing current parameters

1. WaveFileReader:
   * __init(self, filepath)  - constructor   
   * data(self, normalize=True) - returns data in <-1,1> range
  
 2. MFCCParametrizer:
   * __init(self, data, parameters_list) - constructor that extracts MFCC parameters from audio data
   * parameters_(self) - returns extracted parameters
  
 3. ANNClassifier:
   * __init(self, parameters_list) - constructor
   * train(self, training_data)
   * test(self, test_data)
   * output_results_to_file(self, filename)
  
 4. Recognizer:

   * output_configurations_to_file(self, filename)

 5. ConfigurationManager:
   * __init(self, foldername)
   * __generate_configurations(self, np_test_files) - generates configurations with specified number of test files
   * np_configurations(self) - returns the number of configurations
   * test_data(self, configuration_id)
   * training_data(self, configuration_id)
   * output_configurations_to_file(self, filename)
