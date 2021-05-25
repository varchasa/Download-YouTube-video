from pytube import Playlist
from pytube import YouTube

playlist = Playlist('https://www.youtube.com/watch?v=YcnKSdC1U2Y&list=PL3N9eeOlCrP52Zxv_ZQ4El-VR3Phd5cZO')

#To save the video to your location
save_location = 'E:\\'
try:
    for video in playlist:
        print(video)
        YouTube(video).streams.first().download('E:\\')
    print('Video saved.')
except:
    print('Connection Error')

#To save the video where the python is installed
try:
    for video in playlist:
        print(video)
        YouTube(video).streams.first().download()
    print('Video saved.')
except:
    print('Connection Error')

