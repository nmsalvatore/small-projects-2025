import os
import re
from pathlib import Path
import sys

import ffmpeg


os.chdir("test_dir")

for dir in os.listdir():
    if os.path.isdir(dir):
        release_year = None

        for file in os.listdir(dir):
            if file.endswith((".mkv", ".mp4")):
                cleaned = re.sub(r"\s", ".", dir)
                cleaned = re.sub(r"[\(\)]", "", cleaned)
                match = re.search(r"\b\d{4}\b", cleaned)

                if match:
                    cutoff_index = match.span(0)[1]
                    release_year = match.group(0)
                    print(cleaned[:cutoff_index])
