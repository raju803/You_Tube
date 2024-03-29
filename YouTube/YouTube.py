from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

FolderName = ""
fileSizeInBytes =0
MaxFileSize =0

def openDirectry():
    global FolderName
    FolderName=filedialog.askdirectory()
    if(len(FolderName)>1):
        fileLocationLabelError.config(text=FolderName,fg="green")
    else:
        fileLocationLabelError.config(text="Please Choose Folder",fg="red")

def DownloadFile():
    global MaxFileSize,fileSizeInBytes
    choice = youtubeChoices.get()
    video = youtubeEntry.get()
    if(len(video)>1):
        youtubeEntryError.config(text="")
        print(video,"at",FolderName)
        yt = YouTube(video,on_progress_callback=progress)
        print("video name is : \n\n",yt.title)
        
        if(choice ==downloadChoices[0]):
            print("720p video is downloading....")
            loadingLabel.config(text="720p video file downloading..")
            selectVideo = yt.streams.filter(progressive=True).first()
        elif (choice ==downloadChoices[1]):
            print("144p video is downloading...")
            selectVideo = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice ==downloadChoices[2]):
            print('3gp file is downloading...')
            selectVideo =yt.streams.filter(file_extension='3gp').first()
        elif(choice==downloadChoices[3]):
            print('Audio file is downloading...')
            selectVideo =yt.streams.filter(only_audio=True).first()
        fileSizeInBytes = selectVideo.filesize 
        MaxFileSize =fileSizeInBytes/1024000
        MB =str(MaxFileSize)+ "MB"
        print("File SIze = : { :00.00f }".format(MaxFileSize))

        #download
        selectVideo.download(FolderName)
        print("Downloaded on : {}".format(FolderName))
        complete()

    else:
        youtubeEntryError.config(text="Please paste youtube link",fg="red")

def progress(stream=None, chunk = None, file_handle=None,remaining=None):
    percent = (100*(fileSizeInBytes-remaining)/fileSizeInBytes)
    print("{ :00.0f} % download".format(percent))

def complete():
    loadingLabel.config(text="Download Complete")


root = Tk()

root.title("YouTube Video Downloader")
root.grid_columnconfigure(0,weight=1)

youtubeLinkLabel = Label(root,text="Please YouTube Link Here.......",fg='green',font=('Agency FB',30))
youtubeLinkLabel.grid()


youtubeEntryVar = StringVar()
youtubeEntry = Entry(root,width=50,textvariable=youtubeEntryVar)
youtubeEntry.grid(pady=(0,20))

youtubeEntryError = Label(root,fg='red',text="",font=('Agency FB',30))
youtubeEntryError.grid(pady=(0,10))

SaveLabel = Label(root,text="Where to download file?",fg='green',font=('Agency FB',30,"bold"))
SaveLabel.grid()


SaveEntry =Button(root,width=20, bg="blue",fg="white",text="Choose Folder",font=('Arial',15),command=openDirectry)
SaveEntry.grid()

fileLocationLabelError = Label(root,text="",font=('agency Fb',20))
fileLocationLabelError.grid(pady=(0,0))

youtubeChooseLabel = Label(root,text="Please chosse what to download",font=('agency Fb',20))
youtubeChooseLabel.grid()

downloadChoices = ["Mp4 720p",
                    "Mp4 144p",
                    "Video 3gp",
                    "song mp3"
]

youtubeChoices =ttk.Combobox(root,values=downloadChoices)
youtubeChoices.grid()


downloadButton = Button(root,text="Download",width=15,bg="red",command=DownloadFile)
downloadButton.grid()


loadingLabel = ttk.Label(root,text="App Developed by |> Raju",font=("Agency FB",20))
loadingLabel.grid()

root.mainloop()