from pytube import YouTube
import os

os.system("cls")

def download_YouTube_Video():
    print("Inter the video link:")
    url=input().strip()      # go to youtube share option and copy the link from there. 
    try:
        myVideo=YouTube(url)
        print()
        print("Video Title is:")
        print(myVideo.title)
        print()
        print("Get the Thumbnail image from the link below:")
        print(myVideo.thumbnail_url)
        print()
        print("Please wait! video is being Download.")
    except:
        print("Invalid url")

    try:
        myVideo=myVideo.streams.get_highest_resolution()
        myVideo.download()
        print()
        print(f"{myVideo.title} >--> Downloaded Successfully.")
    except:
        print("Failed.")


if __name__=="__main__":
    download_YouTube_Video()