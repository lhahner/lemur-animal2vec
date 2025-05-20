import librosa
import soundfile as sf
import os

DATA_PATH = "../data/wav/"
files = os.listdir("../data/wav/")
print(files) # debug

'''
'''
def print_sample_rate(files):
    for file in files:
        print("Samplerate for ", file, ": ", librosa.get_samplerate(DATA_PATH + file))

'''
'''
def resample_wav(old_rate, new_rate):
    for file in files:
        if librosa.get_samplerate(DATA_PATH + file) == new_rate:
            continue
        else:
            # Load and resample
            audio, original_sr = librosa.load(DATA_PATH + file)  # sr=None preserves original
            resampled_audio = librosa.resample(audio, orig_sr=old_rate, target_sr=new_rate)
            create_wav_file(DATA_PATH + file, resampled_audio, new_rate) # Exclude if not needed

'''
'''
def create_wav_file(file, resampled_audio, new_rate):
    # Write to new .wav file
    sf.write(file, resampled_audio, new_rate)

resample_wav(22050, 16000)
print_sample_rate(files)