from pytube import YouTube

link = 'https://www.youtube.com/watch?v=Id8YjwJDQwg&t=839s'
#To save the video to your location
save_location = 'E:\\'
try:
    YouTube(link).streams.first().download(save_location)
    print('Video saved')
except:
    print('Connection Error')

#To save the video where the python is installed
try:
    YouTube(link).streams.first().download()
    print('Video saved')
except:
    print('Connection Error')
