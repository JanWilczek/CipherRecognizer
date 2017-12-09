# CipherRecognizer

## by Jan Jasiński and Jan Wilczek
##### &copy; Jan Jasiński and Jan Wilczek 2017

Digit recognition software.

### Classes overview

 1. `WavFile` - responsible for retrieving audio data from a .wav file
    * `__init__(self, filepath)`  - constructor   
    * `data(self, normalize=True)` - returns audio data in <-1,1> range if normalize=True in short format otherwise
  
 2. `MFCCParametrizer` - responsible for extraction of MFCC parameters 
    * `__init__(self,
                 winlen=0.025,
                 winstep=0.01,
                 numcep=13,
                 nfilt=26,
                 nfft=512,
                 preemph=0.97,
                 ceplifter=22,
                 appendEnergy=True,
                 appendDeltas=15, 
                 appendDeltasDeltas=15)` - constructor setting up the MFCC extraction arguments. The last two arguments specify the
                 number of frames between which the deltas (or deltas deltas) are being calculated. If they are equal to 0 none are calculated.
    * `parameters(self)` - extracts and returns a matrix of MFCC parameters according to the specified setup
	* `super_vector(self)` - returns averaged extracted parameters with appended rows of the covariance matrix
  
 3. `ANNClassifier` - a classifier based on Artificial Neural Network
    * `__init__(self, hidden_layers_sizes=(100,), activation_function='relu', solver='lbfgs', nb_iterations=200, alpha=0.0001)` -
     constructor with passed in neural network parameters
    * `train(self, training_input_data, training_output_data)` - performs training of the neural network classifer
    * `predict(self, test_input_data)` - for a matrix of input data returns a matrix of prediction vectors
    
 4. `ResultHandler` - a utility for handling results of cross-validation tests
    * `__init__(self, classes)` - constructor setting up the vector of possible classes
    * `reset(self)` - removes all results from the inner buffer (but not from the Excel file)
    * `add_result(self, prediction_vector, correct_result)` - adds a result to the inner buffer along with the correct result
    * `error_rate(self)` - returns the error rate of all results currently stored in the buffer
    * `write_results_to_excel_sheet(self, sheet)` - writes the results to the specified worksheet (but doesn't save it in a Excel file)
    * `save_excel_file(self, filename)` - saves all the sheets in an Excel file under the given filename

 5. `ConfigurationManager` - responsible for generating leave-one-out cross-validation configurations 
    where all recordings from one speaker are removed from training and set as a test for the system
    * `__init__(self, foldername)` - constructor with passed in name of the folder with the training files
    * `nb_configurations(self)` - returns the number of leave-one-out configurations
    * `test_data(self, configuration_id)` - returns an array of full paths to the test files of the given configuration ID
    * `training_data(self, configuration_id)` - returns an array of full paths the training files of the given configuration ID

### Other functions

 1. `utilities.py`:
    * `get_answers(data)` - returns an array of correct anwers for the given array of recordings. The convention is that the digit spoken in the 
   recording is positioned on the second position from the end of the filename (not counting the ".wav" extension)
    * `get_answer(data)` - returns the correct anwers for the given recording. The convention is that the digit spoken in the 
   recording is positioned on the second position from the end of the filename (not counting the ".wav" extension)
    * `get_samples_matrix(filenames, parametrizer)` - reads the audio data from all of the given filenames using `WavFile` class and parametrizes them using the `super_vector()`
   method of the parametrizer object. Returns an array of super vectors corresponding to the given filenames.
   
 1. `main.py` - consists of a significant number of loops used for the optimization of system's parameters. It may write results to an Excel file
 using `ResultHandler` class and append error rate along with parameters' setup to a .txt file
 
 1. `train_main.py` - a program setting up the system with a set of parameters and then training it on the whole train set. At the end the parametrizer
 and classifier are being serialized to the `parametrizer_data` and `classifier_data` files respectively
 
 1. `test_main.py` - a program testing the serialized system on a set of outside files. It writes the predictions to a .csv file and evaluates it
 using `evaluate()` function from `eval.py`
 
 1. `evaluation.py` - an outside code written by Marcin Witkowski evaluating the predictions of the final system setup by analyzing its output from the .csv file
 
### Code guidelines

 1. Software
    * Python 3.6.3
    * Pycharm Community Edition 2016.3 or newer

 ### Resources
 
 1. Instruction:
  https://docs.google.com/document/d/1KIReJ3yLtDpJ8ysbnC86NsdOKLp1Tn2SW4-lrliqFpw/edit

 1. A Beginner's Guide to Neural Networks in Python:
  https://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/

 1. The sklearn.neural_network module:
  http://scikit-learn.org/stable/modules/neural_networks_supervised.html
  
 1. Documentation of the MLPClassifie class of the above library:
  http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier

 1. Used Python modules
  * `pickle` - object serialization
  * `xlwt` - Excel files and sheets handling
  * `os` - file paths handling
  * `numpy` - numerical operations
  * `matplotlib.pyplot` - used in Marcin Witkowski's code to draw confusion matrix graph