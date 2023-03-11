from pytube import YouTube
import os

ytv = YouTube("https://www.youtube.com/watch?v=MFLVmAE4cqg")
video = ytv.streams.filter(res='360p').first()
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
video.download(desktop)
