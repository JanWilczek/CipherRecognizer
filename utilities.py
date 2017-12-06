from WavFile import WavFile

def get_answers(data):
    answers = []
    for string in data:
        answers.append(string[len(string)-6])
    return answers

def get_answer(data):
    return data[len(data)-6]

def get_samples_matrix(filenames, parametrizer):
    data = []
    for filename in filenames:
        audio = WavFile(filename)
        fs, samples = audio.data(normalize=False)
        super_vector = parametrizer.super_vector(samples, fs)
        data.append(super_vector)
    return data
