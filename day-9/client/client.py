import os
import requests
import hashlib
import time

CLIENT_PATH = "target"
SERVER_URL = "http://127.0.0.1:8000"
TOKEN = "12345678"
CHECK_INTERVAL = 10

cache = {}


def hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()


def get_server_file_hash(file_name):
    if file_name in cache:
        return cache[file_name]

    endpoint = f"{SERVER_URL}/get_file_hash"
    response = requests.post(
        endpoint, params={"file_name": file_name}, headers={"Authorization": f"Bearer {TOKEN}"}
    )
    if response.status_code == 200:
        hash = response.json()["file_hash"]
        cache[file_name] = hash
        return hash
    else:
        return None


def upload_file(file_name):
    file_path = os.path.join(CLIENT_PATH, file_name)
    endpoint = f"{SERVER_URL}/upload_file"
    with open(file_path, 'rb') as file:
        files = {'file': file}

        response = requests.post(
            endpoint,
            files=files,
            params={"file_name": file_name},
            headers={"Authorization": f"Bearer {TOKEN}"}
        )
    if response.status_code != 200:
        print(f"Failed to upload {file_name}")
        return
    
    print("File uploaded:", file_name)
    del cache[file_name]


def sync_files():
    while True:
        changed_files = detect_changes()
        if len(changed_files) == 0:
            print("No change")

        for file in changed_files:
            upload_file(file)
        time.sleep(CHECK_INTERVAL)


def detect_changes():
    changed_files = []
    for root, dirs, files in os.walk(CLIENT_PATH):
        for file_name in files:
            client_file_path = os.path.join(root, file_name)
            relative_file_path = os.path.relpath(client_file_path, CLIENT_PATH)
            server_file_hash = get_server_file_hash(relative_file_path)
            client_file_hash = hash_file(client_file_path)

            if client_file_hash != server_file_hash:
                changed_files.append(relative_file_path)
                print("File changed:", relative_file_path)

    return changed_files



if __name__ == "__main__":
    sync_files()
