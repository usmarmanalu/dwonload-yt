from pytube import YouTube

link = input('enter your link youtube : ')
yt = YouTube(link)

videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)
    
    
print(" ")
print("pengaturan durasi dan layout video : ")
dnoption = int(input("masukkan pengaturan : "))
dnvideo = videos[dnoption]
dnvideo.download()

print("download sukses")