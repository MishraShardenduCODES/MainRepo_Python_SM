import multiprocessing
import requests
import os

url = "https://picsum.photos/200/300"

def downloadFile(url, name):
    print(f"Started Downloading: {name}")
    response = requests.get(url)
    with open(f"files2/file{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading: {name}")

if __name__ == "__main__":
    # Ensure the "files2" directory exists
    os.makedirs("files2", exist_ok=True)

    pros = []
    for i in range(50):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
