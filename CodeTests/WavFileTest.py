from WavFile import WavFile

wavFile = WavFile("test.wav")


fs1, normalized_data = wavFile.data()
fs2, not_normalized_data = wavFile.data(normalize=False)

print(normalized_data[:10])
print(not_normalized_data[:10])