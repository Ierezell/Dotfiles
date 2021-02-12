from os import listdir, remove, walk, getcwd
from os.path import join, exists, isfile,expanduser, isdir, normpath
import os

def link_from_folder():
    for root, dirs, files in walk('.'):
        for file_path in files:
            home_file_path = file_path.replace('dot_','.')
            home_root = root.replace('dot_','.')

            if file_path == "link_all_files.py":
                continue

            on_laptop_path = normpath(join(expanduser("~"),home_root, home_file_path))
            on_git_path = normpath(join(getcwd(),root ,file_path))

            if os.path.lexists(on_laptop_path):
                os.remove(on_laptop_path)

            os.symlink(on_git_path, on_laptop_path)
            print(f"Linked : {on_laptop_path:<50} to {on_git_path:>20}")
link_from_folder()
