import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import StringVar
from pytube import YouTube
from tkinter import messagebox

window = tk.Tk()
window.title('Youtube Downloder vahid')
window.minsize(450,200)



def gui():
    
    link_label = tk.Label(window,text = "Video link")
    link_label.grid(row = 0,column = 0,padx = 20,pady = 20)
    link_label.config(font=('none',15),fg = 'red')
    link_input = tk.Entry(window , width = 40,textvariable=video_link)
    link_input.grid(row = 0,column = 1)

    place_label = tk.Label(window,text = "Directory")
    place_label.grid(row = 1,column = 0)
    place_label.config(font=('none',15),fg = 'red')
    place_input = tk.Entry(window , width = 30,textvariable=download_dir)
    place_input.grid(row = 1,column = 1,sticky = "w")

    place_btn = tk.Button(window,text = "open", width = "8",bg = "red", fg = 'white',command = browse)
    place_btn.grid(row = 1,column = 2)

    download_btn = tk.Button(text = "Download",command=download)
    download_btn.grid(row = 2,column = 1,pady = 15)
    download_btn.config(height = 2,width = 20,bg = "blue",fg = "white")
    
def browse():
    directory = askdirectory(initialdir = 'YOUR DIRECTORY PATH',title = "save")
    download_dir.set(directory)
def download():
    link = video_link.get()
    save_dir = download_dir.get()
    yt_film = YouTube(link)
    yt_film.streams.filter(file_extension='mp4').get_highest_resolution().download(save_dir)
    messagebox.showinfo(title=('Succes'),message='The video is dowmloaded please Thank me!!!')
    

download_dir = tk.StringVar()
video_link = tk.StringVar()


gui()

window.mainloop()