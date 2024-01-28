from pytube import YouTube
url="https://www.youtube.com/watch?v=Ns9o3Ixysqo"
my_video=YouTube(url)
print("Video title.....")
print(my_video.title)
print("Thumbnail....")
print(my_video.thumbnail_url)
print("Downloading.....")
my_video=my_video.streams.get_highest_resolution()
my_video.download()