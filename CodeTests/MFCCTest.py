from WavFile import WavFile
import numpy as np
from python_speech_features import mfcc
import MFCCParametrizer as MP

wavFile = WavFile("test.wav")

fs2, not_normalized_data = wavFile.data(normalize=False)

mffcing=MP.MFCCParametrizer()
parameters=mffcing.parameters(not_normalized_data,fs2)
hypervector=mffcing.super_vector(not_normalized_data,fs2,)

print("Raw data")
print(not_normalized_data)
print("MFCC")
print(parameters)
print('Supervector')
print(hypervector)
