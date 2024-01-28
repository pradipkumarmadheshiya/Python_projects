#1 Folder and file compressor to .zip

from zipfile import ZipFile

file="word.docx"
newZip=ZipFile("archive.zip","w")
newZip.write(file)
newZip.close()


#2 decompress file and folder

# from zipfile import ZipFile

# file=ZipFile("archive.zip","r")
# file.extractall()
# file.close()