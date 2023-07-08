import shutil
import os

source_path = "/Users/swanhtetmac/Downloads/flash-card-project-start/data"

dis_path = os.getcwd()

for file in os.listdir(source_path):
    source = os.path.join(source_path, file)
    desried = os.path.join(dis_path, file)
    shutil.move(source, desried)
    print(f"{file} is moved")