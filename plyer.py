import tkinter as tk
from tkinter import filedialog
import os
import random
import pygame
import time

def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        music_list.append(file_path)
        playlist_box.insert(tk.END, os.path.basename(file_path))

def play_music():
    global is_playing
    if not pygame.mixer.music.get_busy() and music_list:
        current_song = random.choice(music_list)
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
        is_playing = True
        update_playbar()

def stop_music():
    pygame.mixer.music.stop()
    play_bar_slider.set(0)

def pause_music():
    global is_playing
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        is_playing = False

def unpause_music():
    global is_playing
    if not is_playing:
        pygame.mixer.music.unpause()
        is_playing = True
        update_playbar()

def set_volume(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)

def update_playbar():
    current_time = 0
    while pygame.mixer.music.get_busy() and is_playing:
        current_time = pygame.mixer.music.get_pos() / 1000
        play_bar_slider.set(current_time)
        window.update()
        time.sleep(1)

# Create the main window
window = tk.Tk()
window.title("Good Music")
window.geometry("400x300")

# Initialize Pygame mixer
pygame.mixer.init()

# Music playlist
music_list = []

# Play status
is_playing = False

# Create buttons
load_button = tk.Button(window, text="Load Music", command=load_music)
load_button.pack(pady=10)

play_button = tk.Button(window, text="Play", command=play_music)
play_button.pack(pady=5)

pause_button = tk.Button(window, text="Pause", command=pause_music)
pause_button.pack(pady=5)

unpause_button = tk.Button(window, text="Unpause", command=unpause_music)
unpause_button.pack(pady=5)

stop_button = tk.Button(window, text="Stop", command=stop_music)
stop_button.pack(pady=5)

# Play bar slider
play_bar_slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, length=300, showvalue=False, command=set_volume)
play_bar_slider.pack(pady=10)

# Playlist
playlist_box = tk.Listbox(window, selectmode=tk.SINGLE)
playlist_box.pack(pady=10)

# Start the application
window.mainloop()
