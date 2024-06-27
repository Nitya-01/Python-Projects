import hashlib

def calculate_file_hash(file_path1, file_path2):
    hash1 = hashlib.sha1()
    hash2 = hashlib.sha1()

    try:
        with open(file_path1, "rb") as file1, open(file_path2, "rb") as file2:
            chunk_size = 1024
            while True:
                chunk1 = file1.read(chunk_size)
                chunk2 = file2.read(chunk_size)
                if not chunk1 and not chunk2:
                    break
                hash1.update(chunk1)
                hash2.update(chunk2)
    except FileNotFoundError:
        print(f"Error: One or both files not found.")
        return None, None
    except PermissionError:
        print(f"Error: Access permission denied for one or both files.")
        return None, None

    return hash1.hexdigest(), hash2.hexdigest()

file_path1 = "pd1.pdf"
file_path2 = "pd1.pdf"

hash1, hash2 = calculate_file_hash(file_path1, file_path2)

if hash1 and hash2:
    if hash1 != hash2:
        print("These files are not identical.")
    else:
        print("These files are identical.")
