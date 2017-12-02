"""
Auxiliary script for evaluation of a digits classifier developed at TM lab.
Requirements:
    Headerless CSV file with classification results in format (%s,%d,%f)%(filename, predicted_label, score).
    Content example:
    001.WAV,9,-35.87
    002.WAV,2,-73.89
    003.WAV,2,-32.99
    004.WAV,3,-94.24

Marcin Witkowski
AGH November 2017
"""
import matplotlib.pyplot as plt


def evaluate(results_fname="results.csv"):
    """
    Main function that evaluates predictions stored in the CSV file. Function computes classification accuracy
    and plots confusion matrix.
    :param results_fname: CSV filename (default: 'results.csv')
    :return: None
    """
    from sklearn.metrics import confusion_matrix, accuracy_score
    prediction_dict = load_results(results_fname)
    true_dict = load_keys()
    prediction_list = []
    true_list = []
    for k, v in true_dict.items():
        if k not in prediction_dict:
            raise Exception("No prediction for file %s" % k)
        true_list.append(v)
        prediction_list.append(prediction_dict[k])
    eval_ca = accuracy_score(true_list, prediction_list)
    print("Classification accuracy based on '%s': %0.2f%%" % (results_fname, 100*eval_ca))
    cm = confusion_matrix(true_list, prediction_list)
    plot_confusion_matrix(cm, classes=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def load_results(filename):
    """
    Loads content of CSV file into a dictionary.
    :param filename: CSV file path
    :return: dictionary [wav_filename]->label
    """
    import csv
    results_dict = dict()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            results_dict[row[0]] = int(row[1])
    return results_dict


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap='Blues'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Details & Source: http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    import numpy as np
    import itertools
    plt.figure(1)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


def load_keys():
    keys = dict()
    keys['001.wav'] = 4
    keys['002.wav'] = 9
    keys['003.wav'] = 0
    keys['004.wav'] = 3
    keys['005.wav'] = 7
    keys['006.wav'] = 9
    keys['007.wav'] = 0
    keys['008.wav'] = 2
    keys['009.wav'] = 9
    keys['010.wav'] = 0
    keys['011.wav'] = 1
    keys['012.wav'] = 2
    keys['013.wav'] = 5
    keys['014.wav'] = 7
    keys['015.wav'] = 8
    keys['016.wav'] = 3
    keys['017.wav'] = 2
    keys['018.wav'] = 6
    keys['019.wav'] = 9
    keys['020.wav'] = 4
    keys['021.wav'] = 6
    keys['022.wav'] = 9
    keys['023.wav'] = 6
    keys['024.wav'] = 7
    keys['025.wav'] = 0
    keys['026.wav'] = 3
    keys['027.wav'] = 9
    keys['028.wav'] = 5
    keys['029.wav'] = 8
    keys['030.wav'] = 7
    keys['031.wav'] = 7
    keys['032.wav'] = 3
    keys['033.wav'] = 6
    keys['034.wav'] = 5
    keys['035.wav'] = 3
    keys['036.wav'] = 2
    keys['037.wav'] = 7
    keys['038.wav'] = 1
    keys['039.wav'] = 3
    keys['040.wav'] = 2
    keys['041.wav'] = 5
    keys['042.wav'] = 3
    keys['043.wav'] = 9
    keys['044.wav'] = 8
    keys['045.wav'] = 6
    keys['046.wav'] = 0
    keys['047.wav'] = 2
    keys['048.wav'] = 2
    keys['049.wav'] = 6
    keys['050.wav'] = 5
    keys['051.wav'] = 3
    keys['052.wav'] = 7
    keys['053.wav'] = 5
    keys['054.wav'] = 8
    keys['055.wav'] = 2
    keys['056.wav'] = 1
    keys['057.wav'] = 4
    keys['058.wav'] = 4
    keys['059.wav'] = 0
    keys['060.wav'] = 8
    keys['061.wav'] = 1
    keys['062.wav'] = 0
    keys['063.wav'] = 6
    keys['064.wav'] = 3
    keys['065.wav'] = 4
    keys['066.wav'] = 7
    keys['067.wav'] = 9
    keys['068.wav'] = 8
    keys['069.wav'] = 1
    keys['070.wav'] = 3
    keys['071.wav'] = 1
    keys['072.wav'] = 7
    keys['073.wav'] = 9
    keys['074.wav'] = 1
    keys['075.wav'] = 1
    keys['076.wav'] = 6
    keys['077.wav'] = 5
    keys['078.wav'] = 2
    keys['079.wav'] = 1
    keys['080.wav'] = 9
    keys['081.wav'] = 3
    keys['082.wav'] = 7
    keys['083.wav'] = 8
    keys['084.wav'] = 2
    keys['085.wav'] = 7
    keys['086.wav'] = 0
    keys['087.wav'] = 9
    keys['088.wav'] = 3
    keys['089.wav'] = 0
    keys['090.wav'] = 1
    keys['091.wav'] = 3
    keys['092.wav'] = 6
    keys['093.wav'] = 2
    keys['094.wav'] = 7
    keys['095.wav'] = 3
    keys['096.wav'] = 2
    keys['097.wav'] = 5
    keys['098.wav'] = 8
    keys['099.wav'] = 9
    keys['100.wav'] = 8
    keys['101.wav'] = 8
    keys['102.wav'] = 9
    keys['103.wav'] = 2
    keys['104.wav'] = 2
    keys['105.wav'] = 5
    keys['106.wav'] = 6
    keys['107.wav'] = 1
    keys['108.wav'] = 2
    keys['109.wav'] = 1
    keys['110.wav'] = 6
    keys['111.wav'] = 8
    keys['112.wav'] = 4
    keys['113.wav'] = 5
    keys['114.wav'] = 6
    keys['115.wav'] = 4
    keys['116.wav'] = 2
    keys['117.wav'] = 5
    keys['118.wav'] = 3
    keys['119.wav'] = 5
    keys['120.wav'] = 4
    keys['121.wav'] = 0
    keys['122.wav'] = 8
    keys['123.wav'] = 7
    keys['124.wav'] = 1
    keys['125.wav'] = 3
    keys['126.wav'] = 7
    keys['127.wav'] = 5
    keys['128.wav'] = 3
    keys['129.wav'] = 8
    keys['130.wav'] = 8
    keys['131.wav'] = 4
    keys['132.wav'] = 8
    keys['133.wav'] = 9
    keys['134.wav'] = 9
    keys['135.wav'] = 0
    keys['136.wav'] = 8
    keys['137.wav'] = 0
    keys['138.wav'] = 9
    keys['139.wav'] = 1
    keys['140.wav'] = 7
    keys['141.wav'] = 0
    keys['142.wav'] = 7
    keys['143.wav'] = 9
    keys['144.wav'] = 1
    keys['145.wav'] = 2
    keys['146.wav'] = 0
    keys['147.wav'] = 5
    keys['148.wav'] = 3
    keys['149.wav'] = 0
    keys['150.wav'] = 1
    keys['151.wav'] = 5
    keys['152.wav'] = 7
    keys['153.wav'] = 5
    keys['154.wav'] = 1
    keys['155.wav'] = 5
    keys['156.wav'] = 9
    keys['157.wav'] = 4
    keys['158.wav'] = 1
    keys['159.wav'] = 6
    keys['160.wav'] = 0
    keys['161.wav'] = 6
    keys['162.wav'] = 7
    keys['163.wav'] = 4
    keys['164.wav'] = 4
    keys['165.wav'] = 4
    keys['166.wav'] = 4
    keys['167.wav'] = 0
    keys['168.wav'] = 6
    keys['169.wav'] = 4
    keys['170.wav'] = 6
    keys['171.wav'] = 0
    keys['172.wav'] = 9
    keys['173.wav'] = 1
    keys['174.wav'] = 0
    keys['175.wav'] = 4
    keys['176.wav'] = 2
    keys['177.wav'] = 7
    keys['178.wav'] = 8
    keys['179.wav'] = 4
    keys['180.wav'] = 8
    keys['181.wav'] = 2
    keys['182.wav'] = 0
    keys['183.wav'] = 4
    keys['184.wav'] = 6
    keys['185.wav'] = 9
    keys['186.wav'] = 6
    keys['187.wav'] = 2
    keys['188.wav'] = 8
    keys['189.wav'] = 5
    keys['190.wav'] = 6
    keys['191.wav'] = 5
    keys['192.wav'] = 3
    keys['193.wav'] = 7
    keys['194.wav'] = 3
    keys['195.wav'] = 8
    keys['196.wav'] = 1
    keys['197.wav'] = 6
    keys['198.wav'] = 5
    keys['199.wav'] = 4
    keys['200.wav'] = 4
    return keys