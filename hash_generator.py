import hashlib


def hash_generator(file_path):
    with open(file_paht, "rb") as f:
        content = f.read()
        md = hashlib.md5()
        md.update(content)
        sha1 = hashlib.sha1()
        sha1.update(content)
        sha256 = hashlib.sha256()
        sha256.update(content)
        sha224 = hashlib.sha224()
        sha224.update(content)
        sha384 = hashlib.sha384()
        sha384.update(content)
        sha512 = hashlib.sha256()
        sha512.update(content)

        print("{}: {}".format(md.name, md.hexdigest()))
        print("-------------------------------")
        

        

        print("{}: {}".format(sha1.name, sha1.hexdigest()))
        print("-------------------------------")
        

        print("{}: {}".format(sha512.name, sha512.hexdigest()))
        print("-------------------------------")
        

        print("{}: {}".format(sha224.name, sha224.hexdigest()))
        print("-------------------------------")
        

        print("{}: {}".format(sha256.name, sha256.hexdigest()))
        print("-------------------------------")
        

        print("{}: {}".format(sha384.name, sha384.hexdigest()))
        print("-------------------------------")




file_paht = r"C:\Users\user\Desktop\hash_generator\simple.txt"

hash_generator(file_paht)