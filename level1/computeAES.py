#!/usr/bin/python3

from Crypto.Cipher import AES
import base64 as b64

cip_text_b64 = "0hxb++cNGw5/mPbBGzFzmREFL9waMmCuHK0DmkqXzRYXvj6+AqKvvhDwP5e1CS/w"
key_b64 = "BmVWeKy6Qd+LEUXnG81SJQ=="

cip_text = b64.b64decode(cip_text_b64)
key = b64.b64decode(key_b64)
cip = AES.new(key, AES.MODE_ECB)
print (cip.decrypt(cip_text))
