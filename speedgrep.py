import sys
import os
import math
import threading

def grep(file, keyword):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if keyword in line:
                print(line)

def split_file(filename, parts):
    files = []
    size = os.path.getsize(filename)
    with open(filename, 'rb') as f:
        for i in range(parts):
            chunk = size // parts
            if i == parts - 1:
                chunk = size - f.tell()
            chunk_file = f"{filename}_{i}"
            with open(chunk_file, 'wb') as chunk_f:
                chunk_f.write(f.read(chunk))
            files.append(chunk_file)
    return files

def main():
    filename = sys.argv[1]
    keyword = sys.argv[2]
    parts = int(sys.argv[3])

    files = split_file(filename, parts)
    threads = []
    for file in files:
        t = threading.Thread(target=grep, args=(file, keyword))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
