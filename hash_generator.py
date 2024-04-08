import hashlib


def hash_gen_md5(file_path):
    with open(file_paht, "rb") as f:
        content = f.read()
        md = hashlib.md5()
        md.update(content)
        return  md.hexdigest()


def hash_gen_sha256(file_path):
     with open(file_paht, "rb") as f:
        content = f.read()
        sha256 = hashlib.sha256()
        sha256.update(content)
        return  sha256.hexdigest()


file_paht = r"C:\Users\user\Desktop\hash_generator\simple.txt"

print(hash_gen_md5(file_paht))