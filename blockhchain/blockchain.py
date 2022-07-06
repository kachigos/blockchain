import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'

def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def get_file():
    files = os.listdir(blockchain_dir)
    return sorted(map(int, files))

def check_integrity():
    files = get_file()
    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']
        prev_hash = str(file - 1)
        actual_hash = get_hash(prev_hash)
        if h == actual_hash:
            res = "Ок, они совпадают"
        else:
            res = "Жок"
        print(f"Блок {prev_hash} - {res}")

def write_block(creditor, money, borrower, prev_hash=''):
    files = get_file()
    last_file = files[-1]
    filename = str(last_file+1)
    prev_hash = get_hash(str(last_file))
    data = {
        'creditor' : creditor,
        'money' : money,
        'borrower' : borrower,
        'hash' : prev_hash
    }
    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    write_block('Daniar', 2000, 'Dastan')
    check_integrity()

if __name__ == "__main__":
    main()