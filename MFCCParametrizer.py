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
                 appendEnergy=True,
                 lowfreq=0,
                 highfreq=20000,
                 appendDeltas=True,
                 appendDeltasDeltas=True):
        self.winlen = winlen
        self.winstep = winstep
        self.numcep = numcep
        self.nfilt = nfilt
        self.nfft = nfft
        self.preemph = preemph
        self.ceplifter = ceplifter
        self.appendEnergy = appendEnergy
        self.lowfreq=lowfreq
        self.highfreq=highfreq
        self.appendDeltas=appendDeltas
        self.appendDeltasDeltas=appendDeltasDeltas

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

        mfcc = self.parameters(signal,samplerate)

        mean_mfcc = self.__mean_coefficients(mfcc)

        covariance = np.cov(np.transpose(mfcc))

        super_vector = [mean_mfcc]
        for j in range (0,len(covariance)):
            super_vector.append(covariance[j,:])

        if self.appendDeltas:
            deltas = self.deltas(mfcc)
            mean_deltas = self.__mean_coefficients(deltas)
            super_vector.append(mean_deltas)

            if self.appendDeltasDeltas:
                deltas_deltas = self.deltas(deltas)
                mean_deltas_deltas = self.__mean_coefficients(deltas_deltas)
                super_vector.append(mean_deltas_deltas)

        final_vector = []
        for i in range (0,len(super_vector)):
            tmp = super_vector[i]
            for j in range (0, len(tmp)):
                final_vector.append(tmp[j])

        return final_vector

    def deltas(self, mfcc_parameters):
        deltas = np.zeros((mfcc_parameters.shape[0], self.numcep))

        for i in range(1,mfcc_parameters.shape[0]):
            deltas[i] = mfcc_parameters[i]-mfcc_parameters[i-1]

        return deltas

    def __mean_coefficients(self, coefficients):
        mean = np.zeros(coefficients.shape[1])
        for i in range(0, coefficients.shape[1]):
            mean[i] = np.mean(coefficients[i, :])

        return mean