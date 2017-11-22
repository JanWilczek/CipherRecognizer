import numpy as np
import scipy.io.wavfile as wav



class WavFile:
    def __init__(self, path):
        self.path=path

    def data2file(self, outputpath):
        fs, samples = wav.read(self.path)
        #Normalizing
        maximum=np.max(samples)
        NormSamples=[]
        for i in range (0, len(samples)):
            NormSamples=samples[i]/maximum

        #saving to file
        file = open(outputpath, "w+")
        #data=np.array([samples, fs])
        np.savetxt(file, samples, fmt='%x')





