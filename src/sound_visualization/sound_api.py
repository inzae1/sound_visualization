import ffmpeg
from pydub import AudioSegment
import time
import librosa.display, librosa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.converter import time_converter


def slice_mp3(input_path: str, output_path: str, start_time: int, end_time: int):
    """
    for slice mp3 file
    :param input_path:
    :param output_path:
    :param start_time:
    :param end_time:
    :return: void
    """
    start = time.time()
    mp3_file = AudioSegment.from_mp3(input_path)
    output_file = mp3_file[start_time:end_time]
    output_file.export(output_path, format='mp3')
    print('time : ', time.time() - start)


def get_sig_time(sig, sr, _time):
    d = int((sig.shape[0] / sr) * 1000)
    result_time = (sig.shape[0] * _time) / d
    return result_time


if __name__ == "__main__":
    PATH = '/Users/inzae/Documents/004_data/datacrush_data/sound_test/'
    MP3_INPUT_PATH = PATH + 'PS-2014200192-01-000.mp3'
    MP3_OUTPUT_PATH = PATH + 'PS-2014200192-01-000out.mp3'
    VTT_INPUT_PATH = PATH + 'PS-2014200192-01-000_fixed.vtt'

    with open(VTT_INPUT_PATH, 'r') as vtt_file:
        vtt_lines = vtt_file.readlines()
        start_time_lines = [time_converter.time_to_second(x.split(' --> ')[0]) for x in vtt_lines if '-->' in x]
        end_time_lines = [time_converter.time_to_second(x.split(' --> ')[1]) for x in vtt_lines if '-->' in x]

        sig, sr = librosa.load(MP3_INPUT_PATH)
        for start_time, end_time in zip(start_time_lines, end_time_lines):
            start_time = start_time * 1000
            end_time = end_time * 1000
            btw_time = 5500 - (end_time - start_time)
            outside_start_time = start_time - (btw_time / 2)
            outside_end_time = end_time + (btw_time / 2)

            start_sig = int(get_sig_time(sig, sr, start_time))
            end_sig = int(get_sig_time(sig, sr, end_time))
            print('sig_num : ', sig[start_sig:end_sig].shape)
            print('num : ', end_sig - start_sig)

    # librosa.display.waveshow(sig, sr)
    # plt.savefig(PATH + 'savefig_default.png')
    # slice_mp3(MP3_INPUT_PATH, MP3_OUTPUT_PATH, 5000, 15000)
