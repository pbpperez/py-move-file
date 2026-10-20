import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    src = parts[1]
    dest = parts[2]

    # If destination ends with '/', treat it as a directory
    # and keep the original file name.
    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    shutil.move(src, dest)
