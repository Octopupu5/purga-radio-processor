"""FFmpeg utilities for audio processing"""
import subprocess
import sys
from pathlib import Path

import subprocess
import sys
from pathlib import Path

def find_ffmpeg(logger):
    """
    Locate ffmpeg executable
    Args:
        logger: Logger instance for output
    Returns:
        str: Path to ffmpeg executable
    Raises:
        SystemExit: If ffmpeg is not found
    """
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info("ffmpeg найден в системе.")
        return 'ffmpeg'
    except Exception:
        pass

    ffmpeg_path = Path("ffmpeg.exe")
    if ffmpeg_path.exists():
        logger.info("Используется ffmpeg.exe, лежащий рядом со скриптом.")
        return str(ffmpeg_path.absolute())

    logger.error("ffmpeg не найден!")
    sys.exit(1)

def cut_audio(ffmpeg, src_path, out_path, duration_sec, logger, input_short, output_short):
    """
    Cut audio file to specified duration
    Args:
        ffmpeg: Path to ffmpeg executable
        src_path: Source audio file path
        out_path: Output file path
        duration_sec: Duration to cut in seconds
        logger: Logger instance
        input_short: Short input path for logging
        output_short: Short output path for logging
    Returns:
        bool: True if successful, False otherwise
    """
    command = [
        ffmpeg,
        '-y',
        '-i', str(src_path),
        '-t', str(duration_sec),
        '-acodec', 'copy',
        str(out_path)
    ]
    logger.info(f"Вырезаем {input_short} -> {output_short} (первые {duration_sec//60} мин)")
    proc = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode == 0:
        logger.info(f"Файл сохранён: {output_short}")
        return True
    else:
        logger.error(f"Ошибка ffmpeg: {proc.stderr.decode(errors='ignore')}")
        return False