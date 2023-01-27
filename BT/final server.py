import hashlib
str="HI there"
result = hashlib.sha512(str.encode())

print(result.hexdigest())