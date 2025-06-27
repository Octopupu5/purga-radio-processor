"""News cutter package for extracting audio segments"""
from .logger import get_logger
from .ffmpeg_utils import find_ffmpeg, cut_audio