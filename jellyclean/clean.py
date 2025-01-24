import os
from pathlib import Path
from shutil import rmtree

from formatting import validate, reformat


if __name__ == "__main__":
    os.chdir("test_dir")

    for entry in os.listdir():
        if os.path.isdir(entry):
            for subentry in os.listdir(entry):
                if subentry.endswith((".mkv", ".mp4")):
                    valid_dirname = validate(entry)
                    if not valid_dirname:
                        new_dirname = reformat(entry)
                        valid_new_dirname = validate(new_dirname)
                        if not valid_new_dirname:
                            raise ValueError(
                                f"Could not validate directory name after reformatting: {entry} -> {new_dirname}"
                            )
                        # TODO: save changes

                    valid_filename = validate(subentry)
                    if not valid_filename:
                        new_filename = reformat(subentry)
                        valid_new_filename = validate(new_filename)
                        if not valid_new_filename:
                            raise ValueError(
                                f"Could not validate file name after reformatting: {subentry} -> {new_filename}"
                            )
                        # TODO: save changes

                if os.path.isdir(Path(entry, subentry)) and subentry == "Subs":
                    for subtitle in os.listdir(Path(entry, subentry)):
                        if "eng" in subtitle.lower():
                            os.rename(
                                Path(entry, subentry, subtitle),
                                Path(entry, subtitle)
                            )

                    rmtree(Path(entry, subentry))
