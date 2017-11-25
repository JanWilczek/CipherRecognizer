from sklearn.neural_network import MLPClassifier

class ANNClassifier:
    def __init__(self, hidden_layers_sizes=(100,), activation_function='relu', solver='lbfgs', nb_iterations=200, alpha=0.0001):
        self.MLPClassifier = MLPClassifier(hidden_layer_sizes=hidden_layers_sizes,
                                             activation=activation_function,
                                             solver=solver,
                                             max_iter=nb_iterations,
                                             alpha=alpha)

    def train(self, training_input_data, training_output_data):
        self.MLPClassifier.fit(training_input_data, training_output_data)

    def predict(self, test_input_data):
        return self.MLPClassifier.predict_log_proba(test_input_data)