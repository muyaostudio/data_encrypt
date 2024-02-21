#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : encrypt.py
@Date    : 2024/02/21 11:08:03
@Version : 1.0
@Desc    : 
'''

from cryptography.fernet import Fernet


# 生成一个密钥，并确保安全地将其传输给需要解密的团队
def generate_key(key_path="./files/data.key"):
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    return key

# 加密函数
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        # 读取JSON文件内容
        data = file.read()
    # 加密数据
    encrypted_data = f.encrypt(data)
    # 将加密后的数据写入新文件
    with open(file_path + ".encrypt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
