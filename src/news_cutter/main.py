"""Entry point for news cutter application"""
import sys
import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import shutil

from .logger import get_logger
from .ffmpeg_utils import find_ffmpeg, cut_audio

def clean_log_dir(log_dir):
    """
    Remove all files and subdirectories from log directory
    Args:
        log_dir: Path to log directory
    """
    log_path = Path(log_dir)
    if log_path.exists():
        for path in log_path.iterdir():
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)

def process_file(args):
    """
    Process a single audio file (worker process)
    Args:
        args: Tuple of (ffmpeg_path, src_path, out_path, duration_sec, log_dir, process_idx) 
    Returns:
        bool: Always True on completion
    """
    ffmpeg_path, src_path, out_path, duration_sec, log_dir, process_idx = args
    logger = get_logger(log_file=f'app_{process_idx}.log', log_dir=log_dir)
    logger.info(f"=== Запущен процесс #{process_idx} ===")
    input_short = '/'.join(Path(src_path).parts[-2:])
    output_short = '/'.join(Path(out_path).parts[-3:])
    logger.info(f"Обработка {input_short}")
    cut_audio(ffmpeg_path, src_path, out_path, duration_sec, logger, input_short, output_short)
    return True

def main(logs_root, outdir):
    """
    Main processing function
    Searches for specific audio files (13_00_00.wav, 18_00_00.wav) in the input directory,
    cuts first 10 minutes from each file using parallel processing.
    Args:
        logs_root: Root directory containing source audio files
        outdir: Output directory for processed files
    """
    log_dir = 'logs'
    clean_log_dir(log_dir)
    logger = get_logger(log_dir=log_dir)
    logger.info(f"=== Запущен главный процесс ===")
    ffmpeg = find_ffmpeg(logger)
    os.makedirs(outdir, exist_ok=True)
    target_times = ['13_00_00.wav', '18_00_00.wav']

    to_process = []
    idx = 0
    
    logs_root_path = Path(logs_root)

    for root, dirs, files in os.walk(logs_root):
        for fname in target_times:
            src_path = Path(root) / fname
            if src_path.exists():
                relative_path = Path(root).relative_to(logs_root_path)
                out_subdir = Path(outdir) / relative_path
                out_subdir.mkdir(parents=True, exist_ok=True)
                
                hour = fname.split('_')[0]
                out_name = f'{hour}_00_00.wav'
                out_path = out_subdir / out_name

                to_process.append((
                    ffmpeg,
                    str(src_path),
                    str(out_path),
                    600,
                    log_dir,
                    idx
                ))
                idx += 1
                
                logger.info(f"Добавлен в очередь: {src_path} -> {out_path}")

    max_workers = min(4, multiprocessing.cpu_count())

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_file, args) for args in to_process]
        for f in futures:
            f.result()

    logger.info("Завершено!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python -m news_cutter.main <входной путь> <путь для полученных отрывков>")
        sys.exit(1)
    logs_root = sys.argv[1]
    outdir = sys.argv[2]
    main(logs_root, outdir)
