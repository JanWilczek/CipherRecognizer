import numpy as np
from python_speech_features import mfcc

'''
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
'''

class MFCCParametrizer:
    def __init__(self,
                 winlen=0.025,
                 winstep=0.01,
                 numcep=13,
                 nfilt=26,
                 nfft=2048,
                 preemph=0.97,
                 ceplifter=22,
                 appendEnergy=True):
        self.winlen = winlen
        self.winstep = winstep
        self.numcep = numcep
        self.nfilt = nfilt
        self.nfft = nfft
        self.preemph = preemph
        self.ceplifter = ceplifter
        self.appendEnergy = appendEnergy

    def parameters(self, signal, samplerate):
        return mfcc(signal,
                    samplerate,
                    self.winlen,
                    self.winstep,
                    self.numcep,
                    self.nfilt,
                    self.nfft,
                    self.numcep,
                    preemph=self.preemph,
                    ceplifter=self.ceplifter,
                    appendEnergy=self.appendEnergy)


    #returns vector of mfcc averaged in time with appended rows of the covariance matrix
    def super_vector(self, signal, samplerate):
        MFCC=self.parameters(signal,samplerate)
        AvgMFCC=np.zeros(13)
        for i in range (0, 13):
            AvgMFCC[i]=np.mean(MFCC[i,:])
        Covarience=np.cov(np.transpose(MFCC))
        SuperVector=[AvgMFCC]
        for j in range (0,len(Covarience)):
            SuperVector.append(Covarience[j,:])
        FinalVector=[]
        for i in range (0,len(SuperVector)):
            tmp = SuperVector[i]
            for j in range (0, len(tmp)):
                FinalVector.append(tmp[j])
        return FinalVector
