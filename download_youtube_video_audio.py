'''
Author: Kai Li
Date: 2021-03-19 10:21:03
LastEditors: Kai Li
LastEditTime: 2021-03-19 11:32:45
'''
import os
import logging
import subprocess
from tqdm import tqdm
logging.getLogger().setLevel(logging.INFO)


class Download_YouTube:
    """Download CSV files a line at a time.
    Arguments
    ---------
    id_lists : list
        List of YouTube video id. egs: https://www.youtube.com/watch?v=Q88P1gpOJxA, id is Q88P1gpOJxA
    video : balse
        If is True, download video file.
    audio: balse
        If is True, download audio file.
    sr: int
        Sample Rate
    Example
    -------
    >>> # Download both video and audio
    >>> down = Download_YouTube(['kjKR2GBuQWw', 'ErtFfLCNtz8'])
    >>> down.download()
    """

    def __init__(self, id_lists, video=True, audio=True, sr=16000):
        logging.info('Initing Download .......')
        self.id_lists = id_lists
        self.video = video
        self.audio = audio
        self.sr = sr

    def download(self):
        logging.info('Starting Download .......')
        for id in tqdm(self.id_lists):
            link = "https://www.youtube.com/watch?v="+id
            if self.video:
                os.makedirs('./video', exist_ok=True)
                command = subprocess.Popen('ffmpeg -i $(youtube-dl -f ”mp4“ --get-url ' + link + ') ' + '-c:v h264 -c:a copy ./video/%s.mp4'
                                           % (id), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                command.wait()
            if self.audio:
                os.makedirs('./audio', exist_ok=True)
                command = 'youtube-dl -x --audio-format wav -o ./audio/o' + id + '.wav ' + link + ';'
                command += 'ffmpeg -i ./audio/o%s.wav -ar %d -ac 1 ./audio/%s.wav;' % (
                    id, self.sr, id)
                command += 'rm ./audio/o%s.wav' % id
                command = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                command.wait()
        logging.info('Finish Download {} files !'.format(len(self.id_lists)))


if __name__ == '__main__':
    print('1')
    down = Download_YouTube(['kjKR2GBuQWw', 'ErtFfLCNtz8'])
    down.download()

