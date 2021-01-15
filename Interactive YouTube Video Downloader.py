from tkinter import *
from pytube import YouTube

window=Tk()
window.title('YouTube Video Downloader')
def videodownload():
	link=e1.get()
	yt=YouTube(link)
	videos=yt.streams
	i=1
	for stream in videos:
		stream,fps=str(stream).split()[3],str(stream).split()[4]
		if stream.startswith('res'):
			l1=Label(window,text='Choose a resolution: ')
			l2=Label(window,text=stream)
			l3=Label(window,text=fps)
			l4=Label(window,text=i)
			l4.grid(column=6,row=10*(i+6))
			l1.grid(column=7,row=10*(i+6))
			l2.grid(column=9,row=10*(i+6))
			l3.grid(column=10,row=10*(i+6))
			i+=1
	e2=Entry(window,width=10)
	e2.grid(column=9,row=950)
	
	l=Label(window,text=' By choosing the quality and fps enter a number ')
	l.grid(column=6,row=950)
	
	b2=Button(window,text=' Download ',fg='red',bg='blue',command=fun1)
	b2.grid(column=9,row=1050)

def fun1():
	
	link=e1.get()
	yt=YouTube(link)
	videos=yt.streams
	stream_num=e2.get()
	stream_num=int(stream_num)
	video=videos[stream_num-1]
	try:
		video.download('/home/mahesh/Downloads')
	except:
		print('Connection error')
	print('Video downloaded')


l1=Label(window,text='URL')
l1.grid(column=1,row=1)

e1=Entry(window,width=30)
e1.grid(column=10,row=1)

b1=Button(window,text=' Enter ',fg='red',bg='blue',command=videodownload)
b1.grid(column=18,row=20)



window.geometry('900x600')
window.mainloop()
