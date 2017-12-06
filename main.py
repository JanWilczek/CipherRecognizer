from ConfigurationManager import ConfigurationManager
from os.path import join
from os import getcwd
from MFCCParametrizer import MFCCParametrizer
from ANNClassifier import ANNClassifier
from ResultHandler import ResultHandler
from numpy import asarray
from utilities import *

# Main program loop
configuration_manager = ConfigurationManager(join(getcwd(),"train"))
result_handler = ResultHandler(asarray(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
setup_results_file = open("setup_results_file.txt",'a')

for loop_enforcer in range(0,1):
    for nb_neurons_in_1_layer in [220]:       # Best result yet: 240
       for nb_neurons_in_2_layer in [110]:     # Best result yet: 120
            for activation in ['logistic']:    # Best: 'logistic'
                for solver in ['adam']:                    # Best: 'adam'
                    for shuffle in [True, False]:
                        for max_iter in [200, 400, 800]:
                            for alpha in [0.0001, 0.0003, 0.0008]:
                                for appendEnergy in [True, False]:
                                    for winlen in [0.025, 0.03, 0.04]:
                                        for winstep in [0.01, 0.015, 0.02]:
                                            for numcep in [10, 15, 20, 25]:
                                                for nfilt in [14, 18, 20]:
                                                    for nfft in [512]: #1024 gives 6.5% better results but increases computing times by 16.7%
                                                        for preemph in [0.9]: #small statistical margin
                                                            for ceplifter in [27]: #small statistical margin
                                                                for iteration_of_setup in range (0,3):
                                                                    result_handler.reset()
                                                                    parametrizer = MFCCParametrizer(winlen=winlen, winstep=winstep, numcep=numcep, nfilt=nfilt, nfft=nfft, preemph=preemph, appendEnergy=appendEnergy, ceplifter=ceplifter)
                                                                    for i in range(0,configuration_manager.nb_configurations()):
                                                                        classifier = ANNClassifier(hidden_layers_sizes=(nb_neurons_in_1_layer,nb_neurons_in_2_layer),activation_function=activation,solver=solver, alpha=alpha, nb_iterations=max_iter)
                                                                        # training
                                                                        train_filenames = configuration_manager.training_data(i)
                                                                        train_data = get_samples_matrix(train_filenames, parametrizer)
                                                                        classifier.train(train_data,get_answers(train_filenames))

                                                                        # testing
                                                                        test_filenames = configuration_manager.test_data(i)
                                                                        test_answers = get_answers(test_filenames)
                                                                        test_data = get_samples_matrix(test_filenames,parametrizer)
                                                                        prediction = classifier.predict(test_data)

                                                                        # handling results
                                                                        for j,input in enumerate(prediction):
                                                                            result_handler.add_result(prediction[j],test_answers[j])

                                                                    # print the current setup and its effectiveness
                                                                    message = "{0} neurons in layer 1, {1} neurons in layer 2, {2} activation function, {3} solver, shuffle is {4}, {5} max_iter, {6} alpha, appendEnergy is {7}, {8} winlen, {9} winstep, {10} numcep, {11} nfilt, {12} nfft, {13} preemph, {14} ceplifter, iteration no. {15}, error rate: {16}".format(
                                                                        classifier.MLPClassifier.hidden_layer_sizes[0],
                                                                        classifier.MLPClassifier.hidden_layer_sizes[1],
                                                                        classifier.MLPClassifier.activation,
                                                                        classifier.MLPClassifier.solver,
                                                                        classifier.MLPClassifier.shuffle,
                                                                        classifier.MLPClassifier.max_iter,
                                                                        classifier.MLPClassifier.alpha,
                                                                        parametrizer.appendEnergy,
                                                                        parametrizer.winlen,
                                                                        parametrizer.winstep,
                                                                        parametrizer.numcep,
                                                                        parametrizer.nfilt,
                                                                        parametrizer.nfft,
                                                                        parametrizer.preemph,
                                                                        parametrizer.ceplifter,
                                                                        iteration_of_setup,
                                                                        result_handler.error_rate())
                                                                    print(message)
                                                                    setup_results_file.write(message + "\n")
                                                                    #sheet_name = "Sheet" + str(iteration_of_setup)
                                                                    #result_handler.write_results_to_excel_sheet(sheet_name)

setup_results_file.close()
#filename = "MainTests.xls"
#result_handler.save_excel_file(filename)