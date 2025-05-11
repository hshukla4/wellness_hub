import os
import sys

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from music.music_player import play_music_pygame, play_shiva_music

FILE_NAME_SHIVA = ".music/om_namah_shivaya.mp3"


@pytest.mark.play_shiva
@pytest.mark.skipif(not os.path.exists(FILE_NAME_SHIVA), reason="Music file not found")
def test_play_shiva_music():
    print("🎵 Testing play_shiva_music...")
    play_shiva_music(FILE_NAME_SHIVA)


@pytest.mark.play_pygame
@pytest.mark.skipif(not os.path.exists(FILE_NAME_SHIVA), reason="Music file not found")
def test_play_music_pygame():
    print("🎧 Testing play_music_pygame...")
    play_music_pygame(FILE_NAME_SHIVA)
