# CipherRecognizer

## by Jan Jasiński and Jan Wilczek
##### &copy; Jan Jasiński and Jan Wilczek 2017

Cipher recognition software.

### Classes overview

1. GlobalParameters:
   - a singleton class containing current parameters

1. WaveFile:
    * \_\_init__(self, filepath)  - constructor   
    * data(self, normalize=True) - returns data in <-1,1> range
  
 2. MFCCParametrizer:
    * \_\_init__(self,
                 winlen=0.025,
                 winstep=0.01,
                 numcep=13,
                 nfilt=26,
                 nfft=512,
                 preemph=0.97,
                 ceplifter=22,
                 appendEnergy=True) - constructor that extracts MFCC parameters from audio data
    * parameters(self) - returns extracted parameters (a matrix)
	* super\_vector(self) - returns averaged extracted parameters with appended rows of the covariance matrix
  
 3. ANNClassifier:
    * \_\_init__(self, nb_hidden_layers, nb_neurons_in_layer, activation_function='relu', solver='lbfgs', nb_iterations=200) - constructor
    * train(self, training_input_data, training_output_data)
    * predict(self, test_input_data)
    
 4. ResultHolder:
    * \_\_init__(self, classes)
    * add_result(self, prediction_vector, correct_result)
    * error_rate(self)
    * write_results_to_excel_file(self, filename, sheet)
    * \_\_is_correct(self, index)
  
 4. Recognizer: - main program class


 5. ConfigurationManager:
    * \_\_init__(self, foldername)
    * \_\_generate_configurations(self, nb_test_files) - generates configurations with specified number of test files
    * nb_configurations(self) - returns the number of configurations
    * test_data(self, configuration_id)
    * training_data(self, configuration_id)
    * output_configurations_to_file(self, filename)
