import os
from pathlib import Path
import subprocess

def make_dummy_mp3(path, duration_sec=30 * 2 * 16):
    cmd = [
        'ffmpeg',
        '-hide_banner',
        '-loglevel', 'error',
        '-y',
        '-f', 'lavfi',
        '-i', f'sine=frequency=440:duration={duration_sec}',
        '-ar', '44100',
        '-ac', '2',
        str(path)
    ]
    subprocess.run(cmd, check=True)

dates = ['19990101', '20250101']
times = ['13_00_00.wav', '18_00_00.wav']

os.makedirs('RECORDER/Logger/PGM_256', exist_ok=True)

for date in dates:
    ddir = Path('RECORDER/Logger/PGM_256') / date
    ddir.mkdir(exist_ok=True)
    for tfile in times:
        make_dummy_mp3(ddir / tfile)