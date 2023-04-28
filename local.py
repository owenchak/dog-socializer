import pygame
import time
import os
import random


def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def get_random_mp3(directory: str):
    mp3_files = [
        file for file in os.listdir(directory) if file.lower().endswith(".mp3")
    ]

    if not mp3_files:
        return None

    random_mp3 = random.choice(mp3_files)
    return os.path.join(directory, random_mp3)


if __name__ == "__main__":
    while True:
        mp3_file_path = get_random_mp3("assets")
        play_mp3(mp3_file_path)
        time.sleep(5)
