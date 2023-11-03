from pytube import YouTube

link = input("Link: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()