import os
import shutil

files = os.scandir('c:\\test\\test_in')
files_list = list(files)
f = files_list[0]

print(f, f.name, f.path, f.is_dir(), f.stat().st_size)

files_txt = [f for f in os.scandir('c:\\test\\test_in') if os.path.isfile(f)]
print(files_txt)


