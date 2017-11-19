from sklearn.neural_network import MLPClassifier

class ANNClassifier:
    def __init__(self, nb_hidden_layers, nb_neurons_in_layer, activation_function='relu', solver='lbfgs', nb_iterations=200):
        self.nb_hidden_layers = nb_hidden_layers
        self.nb_neurons_in_layer = nb_neurons_in_layer
        self.__hidden_layer_sizes = (self.nb_neurons_in_layer,)*self.nb_hidden_layers  # Each of __nb_hidden_layers layers has __nb_neurons_in_layer neurons
        self.MLPClassifier = MLPClassifier(hidden_layer_sizes=self.__hidden_layer_sizes,
                                             activation=activation_function,
                                             solver=solver,
                                             max_iter=nb_iterations)

    def train(self, training_input_data, training_output_data):
        self.MLPClassifier.fit(training_input_data, training_output_data)

    def predict(self, test_input_data):
        return self.MLPClassifier.predict_log_proba(test_input_data)