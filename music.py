# from cgitb import handler
import tkinter as tk
import fnmatch
import os
from pygame import mixer

device = tk.Tk()
device.title("Sooth Music Player")
device.geometry("600x800")
device.config(bg='orange')

ft = 'ds-digital'

music_path = "C:\\Users\lenovo\Music"
note = "*.mp3"

mixer.init()

prev_icon = tk.PhotoImage(file='prv.png')
play_icon = tk.PhotoImage(file='pl.png')
stop_icon = tk.PhotoImage(file='stp.png')
pause_icon = tk.PhotoImage(file='pus.png')
next_icon = tk.PhotoImage(file='nx.png')

def select():
   music_name = music_box.get("anchor")
   label.config(text = music_name)
   mixer.music.load(music_path + "\\" + music_name ) 
   mixer.music.play()

def stop():
    mixer.music.stop()
    music_box.select_clear('active')

def next_play():
    nxt_song = music_box.curselection()
    nxt_song = nxt_song[0] + 1
    nxt_name = music_box.get(nxt_song)
    label.config(text=nxt_name)
    #Configuring it to play
    mixer.music.load(music_path + "\\" + nxt_name)
    mixer.music.play()
    #to make it highlight the current playing music
    music_box.select_clear(0, 'end')
    music_box.activate(nxt_song)
    music_box.select_set(nxt_song)

def prev_play():
    prev_song = music_box.curselection()
    prev_song = prev_song[0] - 1
    prev_name = music_box.get(prev_song)
    label.config(text= prev_name)
    #Configuring it to play
    mixer.music.load(music_path + "\\" + prev_name)
    mixer.music.play()
    #to make it highlight the current playing music
    music_box.select_clear(0, 'end')
    music_box.activate(prev_song)
    music_box.select_set(prev_song)

def pause_song():
    if pause_button["text"] == "Pause":
        mixer.music.pause()
        pause_button["text"] = "Play"
    else:
        mixer.music.unpause()
        pause_button["text"] = "Pause"

music_box = tk.Listbox(device, fg='black', bg='orange', width=100, font=(ft, 14))
music_box.pack(padx=15, pady=15)

label = tk.Label(device, text='', bg='black', fg='yellow', font=(ft, 15 ))
label.pack(pady= 15)

button_holder = tk.Frame(device, bg='black')
button_holder.pack(padx=10, pady=5, anchor='center')

prev_button = tk.Button(device, text="Prev", image = prev_icon, bg='black', borderwidth=0, command=prev_play)
prev_button.pack(pady=15, in_=button_holder, side='left')

play_button = tk.Button(device, text="Play", image = play_icon, bg='black', borderwidth=0, command=select)
play_button.pack(pady=15, in_=button_holder, side='left')

pause_button = tk.Button(device, text="Pause", image = pause_icon, bg='black', borderwidth=0, command=pause_song)
pause_button.pack(pady=15, in_=button_holder, side='left')

stop_button = tk.Button(device, text="Stop", image = stop_icon, bg='black', borderwidth=0, command=stop)
stop_button.pack(pady=15, in_=button_holder, side='left')

next_button = tk.Button(device, text="Next", image = next_icon, bg='black', borderwidth=0, command=next_play)
next_button.pack(pady=15, in_=button_holder, side='left')

for root, dirs, files in os.walk(music_path):
    for filename in fnmatch.filter(files, note):
        music_box.insert('end', filename)


device.mainloop() 