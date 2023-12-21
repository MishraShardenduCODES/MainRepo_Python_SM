import multiprocessing
import requests
import os

url = "https://picsum.photos/200/300"

def downloadFile(args):
    url, name = args
    print(f"Started Downloading: {name}")
    response = requests.get(url)
    with open(f"files/file{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading: {name}")

if __name__ == "__main__":
    # Ensure the "files" directory exists
    os.makedirs("files", exist_ok=True)

    # Create a list of arguments for downloadFile function
    arguments_list = [(url, i+1) for i in range(10)]

    # Use multiprocessing.Pool to parallelize downloads
    with multiprocessing.Pool() as pool:
        pool.map(downloadFile, arguments_list)
