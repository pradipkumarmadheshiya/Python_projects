from pytube import YouTube
import instaloader as il
import os

os.system("cls")

# Download Youtube content:
print("Content Downloader:-")
print()

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

# Download Instagram content:

def download_Instagram_Video():
    try:
        print("If you want to download profile pic only. press 1")
        print("If you want to download all content, press 2")
        option=int(input("Enter your wish: "))
        if option==1:
            print("Inter the User Name:")
            user_name=input().strip()
            print()
            img=il.Instaloader()
            img.download_profile(user_name,profile_pic_only=True)
            print()
            print("Profile picture successfully downloaded.")
            print()
        elif option==2:
            img=il.Instaloader()
            user_name=input("Enter the User Name: ").strip()
            print()
            img.download_profile(user_name,profile_pic_only=False)
            print()
            print(user_name,"All photos and videios Downloaded")
        else:
            print("Invalid choose.")
    except:
        print("User name does not exist.")

def main():
    print("Press 1 for Youtube content")
    print("Press 2 for Instagram content")
    print()

    choose={1:download_YouTube_Video,2:download_Instagram_Video}
    user_wish=int(input("Choose option: "))

    if user_wish in choose:
        choose[user_wish]()
    else:
        print("Invalid press.")


if __name__=="__main__":
    main()