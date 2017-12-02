import numpy as np
from python_speech_features import mfcc

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
        return mfcc(signal=signal,
                    samplerate=samplerate,
                    winlen=self.winlen,
                    winstep=self.winstep,
                    numcep=self.numcep,
                    nfilt=self.nfilt,
                    nfft=self.nfft,
                    preemph=self.preemph,
                    ceplifter=self.ceplifter,
                    appendEnergy=self.appendEnergy)


    # returns vector of mfcc averaged in time with appended rows of the covariance matrix
    def super_vector(self, signal, samplerate):

        MFCC=self.parameters(signal,samplerate)

        AvgMFCC=np.zeros(self.numcep)
        for i in range (0, self.numcep):
            AvgMFCC[i]=np.mean(MFCC[i,:])

        Covariance=np.cov(np.transpose(MFCC))

        SuperVector=[AvgMFCC]
        for j in range (0,len(Covariance)):
            SuperVector.append(Covariance[j,:])

        FinalVector=[]
        for i in range (0,len(SuperVector)):
            tmp = SuperVector[i]
            for j in range (0, len(tmp)):
                FinalVector.append(tmp[j])

        return FinalVector
