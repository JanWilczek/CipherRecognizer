import numpy as np
from python_speech_features import mfcc, delta

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
                 appendDeltas=15,
                 appendDeltasDeltas=15):
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


    # returns vector of mfcc averaged in time with appended rows of the covariance matrix and optionally deltas and deltas deltas
    def super_vector(self, signal, samplerate):

        mfcc = self.parameters(signal,samplerate)

        mean_mfcc = self.__mean_coefficients(mfcc)

        covariance = np.cov(np.transpose(mfcc))

        super_vector = [mean_mfcc]
        for j in range (0,len(covariance)):
            super_vector.append(covariance[j,:])

        if self.appendDeltas:
            deltas = delta(mfcc, self.appendDeltas)
            mean_deltas = self.__mean_coefficients(deltas)
            super_vector.append(mean_deltas)

            if self.appendDeltasDeltas:
                deltas_deltas = delta(deltas, self.appendDeltasDeltas)
                mean_deltas_deltas = self.__mean_coefficients(deltas_deltas)
                super_vector.append(mean_deltas_deltas)

        final_vector = []
        for i in range (0,len(super_vector)):
            tmp = super_vector[i]
            for j in range (0, len(tmp)):
                final_vector.append(tmp[j])

        return final_vector

    def __mean_coefficients(self, coefficients):
        mean = np.zeros(coefficients.shape[1])
        for i in range(0, coefficients.shape[1]):
            mean[i] = np.mean(coefficients[i, :])

        return mean