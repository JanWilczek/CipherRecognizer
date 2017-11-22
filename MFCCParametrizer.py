import numpy as np
from python_speech_features import mfcc

class MFCCParametrizer:
    def __init__(self, InputPath,OutputPath, parameters_list):
        # Otworzenie pliku z danymi
        file = open(InputPath, 'r')
        # Pobranie danych - Trzeba uzgodni jak będziemy ukadac dane żeby pobiera naraz samples i fs
        samples = file.readlines()
        #Liczenie MFCC
        MFCC_Data=mfcc(samples,fs)
        #wypisywanie parametrow do pliku
        file = open(OutputPath, "w+")
        # data=np.array([samples, fs])
        np.savetxt(file, samples, fmt='%x')
