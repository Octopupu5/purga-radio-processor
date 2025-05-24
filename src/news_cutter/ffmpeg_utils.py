import subprocess
import sys
from pathlib import Path

import subprocess
import sys
from pathlib import Path

def find_ffmpeg(logger):
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