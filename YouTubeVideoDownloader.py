from pytube import YouTube
link=input("Paste the youtube link here to download:")
yt=YouTube(link)
videos=yt.streams
i=1
for stream in videos:
	stream,fps=str(stream).split()[3],str(stream).split()[4]
	if stream.startswith('res'):
		print(i,'-->  Choose the resolution ',stream,' ',fps)
		i+=1
stream_num=int(input('Enter the stream number to download:(our choice is 1-9)'))
video=videos[stream_num-1]
try:
	video.download('/home/mahesh/Downloads')
except:
	print('Connection error')
print('Video downloaded')
