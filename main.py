import os

# os.mkdir("Data")

# for i in range (1,101) :
#     os.mkdir(f"data/Day{i}")

for i in range (1,101) :
    os.rename(f"data/Tutorial{i}",f"data/Tutorial {i}")