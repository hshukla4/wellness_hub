import os

import pygame
from playsound import playsound  # type: ignore


def play_shiva_music(file_name):
    """
    Play Shiva bhajan using the simple playsound library.
    """
    if os.path.exists(file_name):
        playsound(file_name)
        print("✅ Playing Shiva bhajan with playsound")
    else:
        print(f"❌ File not found: {file_name}")


def play_music_pygame(file_name: str = ".music/om_namah_shivaya.mp3"):
    """
    Play Shiva bhajan using pygame for more control.
    """
    print(f"📂 Looking for: {file_name}")

    if not os.path.exists(file_name):
        print(f"❌ File not found: {file_name}")
        return

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()

    print("🎶 Playing Shiva bhajan with pygame...")

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
