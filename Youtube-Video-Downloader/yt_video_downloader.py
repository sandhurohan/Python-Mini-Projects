#----------------------------------- Youtube-Audio-Video-Downloader ------------------------------------
from pytube import YouTube

link=input("Enter Youtube Video Link    :   ")
link=YouTube(link)

print(link.title)
#print(link.description)
print(link.thumbnail_url)

videos=list(enumerate(link.streams))

for i in videos:
    i=list(i)
    print(i)

print()
stream=int(input("Enter Stream Id   : "))

x=videos[stream][1]
print(x)
x.download()

print("-------------------------- VIDEO DOWNLOADED SUCCESSFULLY --------------------")
