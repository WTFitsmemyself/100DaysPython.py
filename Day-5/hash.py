import hashlib

hash_matn = "Hossein nouri"
result = hashlib.sha256(hash_matn.encode())
hashasli = result.hexdigest()
print(hashasli)
