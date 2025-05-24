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
times = ['13_00_00.mp3', '18_00_00.mp3']

os.makedirs('PGM_logger', exist_ok=True)

for date in dates:
    ddir = Path('PGM_logger') / date
    ddir.mkdir(exist_ok=True)
    for tfile in times:
        make_dummy_mp3(ddir / tfile)