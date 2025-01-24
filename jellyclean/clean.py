import os
import re
from pathlib import Path
from shutil import rmtree

from formatting import validate, reformat


def clean_entry_name(entry: str) -> str:
    """Check if file or directory name is valid and reformat if not"""

    valid: re.Match | None = validate(entry)

    if not valid:
        new_name: str = reformat(entry)
        valid_new_name: re.Match | None = validate(new_name)

        if not valid_new_name:
            raise ValueError(
                f"Could not validate entry name after reformatting: {entry} -> {new_name}"
            )

        return new_name

    return entry


if __name__ == "__main__":
    os.chdir("test_dir")

    for entry in os.listdir():
        subtitle_count: int = 1

        if os.path.isdir(entry):
            clean_dirname: str = clean_entry_name(entry)

            for subentry in os.listdir(entry):
                subentry_relative_path: Path = Path(entry, subentry)

                if subentry.endswith((".mkv", ".mp4")):
                    clean_filename: str = clean_entry_name(subentry)
                    os.rename(subentry_relative_path, Path(entry, clean_filename))

                elif subentry.endswith(".srt"):
                    os.rename(
                        subentry_relative_path,
                        Path(entry, f"{clean_dirname}.eng.{subtitle_count}.srt")
                    )
                    subtitle_count += 1

                elif os.path.isdir(subentry_relative_path):
                    for subtitle in os.listdir(subentry_relative_path):
                        if "eng" in subtitle.lower():
                            os.rename(
                                Path(subentry_relative_path, subtitle),
                                Path(entry, f"{clean_dirname}.eng.{subtitle_count}.srt")
                            )
                            subtitle_count += 1

                    rmtree(subentry_relative_path)

                else:
                    os.remove(subentry_relative_path)

            os.rename(entry, clean_dirname)
