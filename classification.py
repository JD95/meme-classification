# -*- coding: utf-8 -*-
"""classification

This module contains the logic for sorting fresh memes into the
appropriate folders based on their similarity to already sorted
images.

"""
import os
import imagehash
from PIL import Image
from typing import List


def safe_cast(val, to_type, default=None):
    """A helper for safe casts between types"""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def existing_hashes(root_dir: str) -> List[int]:
    """Collects hashes from folder names in root directory"""
    folders = [name for name in
               os.listdir(root_dir) if os.path.isdir(name)]
    hashes = []
    for folder in folders:
        if folder is int:
            hashes.append(folder)
    return hashes


def get_image_hash(filepath: str) -> int:
    """Given a path to a file, calculate it's image hash"""
    img = Image.open(filepath)
    size = (256, 256)
    img.thumbnail(size, Image.ANTIALIAS)
    return imagehash.whash(img)


def hamdist(str1: str, str2: str) -> int:
    """Count the # of differences between
       equal length strings str1 and str2"""
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs
