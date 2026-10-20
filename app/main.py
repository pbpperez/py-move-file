import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Expected: mv <src> <dest>")

    src = parts[1]
    dest = parts[2]

    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    dest_dir = os.path.dirname(dest)
    if dest_dir:
        current = ""
        for part in dest_dir.replace("\\", "/").split("/"):
            if part:
                current = os.path.join(current, part) if current else part
                try:
                    os.mkdir(current)
                except FileExistsError:
                    pass

    shutil.copy(src, dest)
    os.remove(src)
