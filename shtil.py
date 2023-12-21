import shutil
import os
# copy a file #
shutil.copy("shtil.py", "shtil2.py")

# copy a file along with its meta data #
shutil.copy2("shtil.py", "shtil3.py")

# copying C Tutorial as C+- Tutorial ie a folder #
# copytree is used to copy a file #
shutil.copytree(".tutorial",".2tutorial")
shutil.copytree(".tutorial",".3tutorial")

# # # # # # # # # # # # # # # # # # # # # # # # 

os.remove(".3tutorial")