import os

#1 creat directory
os.mkdir("file")
os.mkdir("hello")
os.makedirs("file1/file2/file3/file4")

#2 delete directory
# os.rmdir("file")
# os.removedirs("file1/file2/file3/file4")

#3 rename file
# os.rename("hello","word")

#4 file details
# print(os.stat("word"))
# print(os.stat("word").st_size)

#5 current working Directory
# print(os.getcwd())

#7 all file & folder 
# print(os.listdir())

#6 change directory
# path=r"C:\Users\HP\Desktop"
# os.chdir(path)
# print(os.getcwd())