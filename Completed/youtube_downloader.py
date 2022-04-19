import sys
from pytube import YouTube
link = input("Enter your link: ")
yt = YouTube(link)
video = yt.get('mp4', '720p')
video.download('~/Desktop')
# yt.streams.first().download()

