"""Generate dummy audio files for testing purposes"""
import os
from pathlib import Path
import subprocess
import sys

def find_ffmpeg():
    """
    Find ffmpeg executable in system PATH or local directory
    Returns:
        str: Path to ffmpeg executable
    Raises:
        SystemExit: If ffmpeg is not found
    """
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return 'ffmpeg'
    except Exception:
        pass

    ffmpeg_path = Path("ffmpeg.exe")
    if ffmpeg_path.exists():
        return str(ffmpeg_path.absolute())
    parent_ffmpeg = Path("../ffmpeg.exe")
    if parent_ffmpeg.exists():
        return str(parent_ffmpeg.absolute())
    sys.exit(1)

def make_dummy_mp3(path, duration_sec=30 * 2 * 16):
    """
    Create a dummy audio file with sine wave
    Args:
        path: Output file path
        duration_sec: Duration in seconds (default: 960)
    """
    ffmpeg = find_ffmpeg()
    cmd = [
        ffmpeg,
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