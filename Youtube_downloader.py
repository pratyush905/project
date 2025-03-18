from pytube import YouTube
from sys import argv

try:
    link = argv[1]
    yt = YouTube(link)

    print("Title: ",yt.title)
    print("Author: ",yt.author)

    yd = yt.streams.get_highest_resolution()
    yd.download("D:\Downloads")
    print("Download complete.")
    
except Exception as e:
    print("An error occurred:", str(e))
