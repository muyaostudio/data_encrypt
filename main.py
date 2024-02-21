#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    : main.py
@Date    : 2024/02/21 11:21:33
@Version : 1.0
@Desc    : 
'''

from encrypt import generate_key, encrypt_file
from decrypt import load_key, decrypt_file_to_disk, decrypt_file_to_memory

# 生成密钥
key = generate_key(key_path="./files/data.key")

# 加密文件
encrypt_file("./files/data.json", key)

# 假设需要解密时，先加载密钥
key = load_key(key_path="./files/data.key")

# 解密文件 (存储到文件)
decrypt_file_to_disk(file_path="./files/data.json.encrypt", key=key)

# 解密文件 (解密到内存)
decrypt_file_to_memory(file_path="./files/data.json.encrypt", key=key)
