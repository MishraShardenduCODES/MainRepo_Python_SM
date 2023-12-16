import os

if not os.path.exists("Data"):
    os.mkdir("Data")

for i in range(1, 101):
    os.mkdir(f"Data/Day{i}")

for i in range(1, 101):
    os.rename(f"Data/Day{i}", f"Data/Tutorial_By_Shardendu_Mishra_Day_{i}")

print(f"This is the current directory : {os.getcwd()}")
print(f"Files in the current directory : ", os.listdir('.'))
os.remove('ug.txt')

os.mkdir("Data2")
os.mkdir("Data3")

os.chdir("Data2")
os.mkdir("Data3")

os.chdir("..")  # Navigate back to the parent directory
os.rmdir("Data3")  # Remove 'Data3' from the parent directory

print(f"This is the current directory : {os.getcwd()}")
