import concurrent.futures
import requests
import os

url = "https://picsum.photos/200/300"

def downloadFile(args):
    url, name = args
    print(f"Started Downloading: {name}")
    response = requests.get(url)
    with open(f"files3/file{name}.jpg", "wb") as file:
        file.write(response.content)
    print(f"Finished Downloading: {name}")

if __name__ == "__main__":
    # Ensure the "files3" directory exists
    os.makedirs("files3", exist_ok=True)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        arguments_list = zip(l1, l2)
        results = executor.map(downloadFile, arguments_list)

    for r in results:
        print(r)
