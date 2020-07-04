def unmuteMusic():
    global currentvol
    root.UnmuteButton.grid_remove()
    root.muteButton.grid()
    mixer.music.set_volume(currentvol)


def mutemusic():
    global currentvol
    root.muteButton.grid_remove()
    root.UnmuteButton.grid()
    currentvol= mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text="Resume.....")

def volumeup():
 vol = mixer.music.get_volume()
 mixer.music.set_volume(vol+0.05)
 ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
 ProgressbarVolume['value']=mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol -0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100


def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text="Stopped.....")


def pausemusic():
 mixer.music.pause()
 root.ResumeButton.grid_remove()
 root.ResumeButton.grid()
 AudioStatusLabel.configure(text="Paused.....")

def playmusic():
 ad=audiotrack.get()
 mixer.music.load(ad)
 ProgressbarLabel.grid()
 root.muteButton.grid()
 ProgressbarMusic.grid()
 ProgressbarMusicLabel.grid()
 mixer.music.play()
 mixer.music.set_volume(0.4)
 ProgressbarVolume['value']=40
 ProgressbarVolumeLabel['text']='40%'
 AudioStatusLabel.configure(text="Playing.....")

 Song=MP3(ad)
 totalsonglength=int(Song.info.length)
 ProgressbarMusic['maximum']=totalsonglength
 ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))

 def ProgressbarMusictick():
     CurrentSongLength = mixer.music.get_pos()//1000
     ProgressbarMusic['value']=CurrentSongLength
     ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
     ProgressbarMusic.after(2,ProgressbarMusictick)
     ProgressbarMusictick()


def musicurl():
    try:
     dd = filedialog.askopenfilename(initialdir='E:\songs',title='select audio file',filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
     dd=filedialog.askopenfilename(title='select audio file',filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    audiotrack.set(dd)

def createwidthes():
     global AudioStatusLabel,ProgressbarVolumeLabel,ProgressbarVolume,ProgressbarLabel,ProgressbarMusicLabel,ProgressbarMusic, ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel

     ######################################################################### Labels
     TrackLable = Label(root,text='Select Audio Track : ',background='peachpuff',font=('chiller',20,'italic bold'))
     TrackLable.grid(row=0,column=0,padx=20,pady=20)

     AudioStatusLabel=Label(root,text='',background='peachpuff',font=('arial',15,'italic bold'),width=20)
     AudioStatusLabel.grid(row=2,column=1)

     ########################################################################## Entry Box
     TrackLableEntry= Entry(root,font=('arial',17,'italic bold'),width=30,text=audiotrack)
     TrackLableEntry.grid(row=0,column=1,padx=20,pady=20)

     ########################################################################### Buttons
     BrowseButton= Button(root,text='Search',bg='deeppink',font=('arial',14,'italic bold'),width=15,bd=5,activebackground='hotpink',command= musicurl)
     BrowseButton.grid(row=0,column=2,padx=20,pady=20)

     PlayButton = Button(root, text='Play', bg='sky blue', font=('arial', 14, 'italic bold'), width=20, bd=5,activebackground='steel blue',command=playmusic)
     PlayButton.grid(row=1, column=0, padx=20, pady=20)


     root.PauseButton = Button(root, text='Pause', bg='yellow', font=('arial', 14, 'italic bold'), width=15, bd=5,activebackground='steel blue',command=pausemusic)
     root.PauseButton.grid(row=1, column=1, padx=20, pady=20)

     root.ResumeButton = Button(root, text='Resume', bg='yellow', font=('arial', 14, 'italic bold'), width=15, bd=5,activebackground='steel blue', command=resumemusic)
     root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
     root.ResumeButton.grid_remove()

     root.muteButton=Button(root,text='Unmute',width=15,bg='yellow',activebackground='purple4',bd=5,command=mutemusic)
     root.muteButton.grid(row=3,column=2)
     root.muteButton.grid_remove()

     root.UnmuteButton = Button(root, text='Mute', width=15, bg='yellow', activebackground='purple4', bd=5,command=unmuteMusic)
     root.UnmuteButton.grid(row=3, column=2)


     VolumeUpButton = Button(root, text='Volume Up', bg='Blue', font=('arial', 14, 'italic bold'), width=13, bd=5,activebackground='seagreen',command=volumeup)
     VolumeUpButton.grid(row=1, column=2, padx=20, pady=20)

     StopButton = Button(root, text='Stop', bg='red', font=('arial', 14, 'italic bold'), width=15, bd=5,activebackground='steel blue',command=stopmusic)
     StopButton.grid(row=2, column=0, padx=20, pady=20)

     VolumeDownButton = Button(root, text='Volume down', bg='Blue', font=('arial', 14, 'italic bold'), width=13, bd=5,activebackground='seagreen',command=volumedown)
     VolumeDownButton.grid(row=2, column=2, padx=20, pady=20)
     ############################################################################################################################################################### Progrees bar Volume

     ProgressbarLabel=Label(root,text='',bg='red')
     ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
     ProgressbarLabel.grid_remove()


     ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                   value=0,length=190)
     ProgressbarVolume.grid(row=0,column=0,ipadx=5)

     ProgressbarVolumeLabel=Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
     ProgressbarVolumeLabel.grid(row=0,column=0)

     ########################################################################################################## ProgreeBar Music
     ProgressbarMusicLabel=Label(root,text='',bg='red')
     ProgressbarMusicLabel.grid(row=3, column=0, columnspan=3, padx=20, pady=20)
     ProgressbarMusicLabel.grid_remove()

     ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red',width=6)
     ProgressbarMusicStartTimeLabel.grid(row=0, column=0)

     ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
     ProgressbarMusic.grid(row=0,column=1,ipadx=205,ipady=3)


     ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red')
     ProgressbarMusicEndTimeLabel.grid(row=0, column=2)





#########################################################################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root = Tk()
root.geometry('1100x500+200+50')
root.title('Simple Music Player....')
root.iconbitmap('music.ico')
root.resizable(False, False)
root.configure(bg='peach puff')
###############################################################################Global Variable
audiotrack=StringVar()
currentvol= 0
totalsonglength=0
count = 0
text = ''
###############################################################################Create String
ss = 'Play Your Mood Playlist'
count = 0
text = ''
SliderLabel= Label(root,text='',bg='peach puff',font=('arial',25,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
 global count ,text
 if(count>=len(ss)):
     count = -1
     text= ''
     SliderLabel.configure(text=text)
 else:
     text=text+ss[count]
     SliderLabel.configure(text=text)
     count+=1
     SliderLabel.after(200,IntroLabelTrick)

IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()
