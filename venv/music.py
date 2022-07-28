import pyttsx3
import pygame
from pygame import mixer
import playsound

pygame.init()
def playmusic():
    mixer.music.load('m24.mp3')
    mixer.music.play()

playmusic()