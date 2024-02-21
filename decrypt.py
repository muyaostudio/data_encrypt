#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : decrypt.py
@Date    : 2024/02/21 11:20:15
@Version : 1.0
@Desc    : 
'''

from cryptography.fernet import Fernet


# 加载密钥
def load_key(key_path="./files/data.key"):
    return open(key_path, "rb").read()

# 解密函数（to file）
def decrypt_file_to_disk(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        # 读取加密文件内容
        encrypted_data = encrypted_file.read()
    # 解密数据
    decrypted_data = f.decrypt(encrypted_data)
    # 将解密后的数据写入新文件
    with open(file_path+".decrypt", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

def decrypt_file_to_memory(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        # 读取加密文件内容
        encrypted_data = encrypted_file.read()
    # 解密数据
    decrypted_data = f.decrypt(encrypted_data).decode("utf-8")
    return decrypted_data
