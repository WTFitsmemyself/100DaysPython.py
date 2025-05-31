import hashlib

hash_matn = "Hosseinnouri"
result = hashlib.sha512(hash_matn.encode())
hashasli = result.hexdigest()
print(hashasli)
