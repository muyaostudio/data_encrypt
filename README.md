# 文件加解密

使用Python中的`cryptography`库，基于Fernet对称加密的加解密方案。

需要安装`cryptography`库，可以使用pip进行安装：

```bash
pip install cryptography
```

## 使用说明
- `encrypy.py` 用于生成秘钥和加密文件
- `decrypt.py` 用于加载秘钥和解码文件
- `main.py` 用于测试

## 补充说明
Fernet 是一种对称加密方案，由 Python 的 `cryptography` 库提供支持。它是一种高级加密标准，基于 AES (高级加密标准) 算法和 HMAC (基于散列的消息认证码)。Fernet 设计用于安全地存储和传输加密数据，确保数据的完整性和不可抵赖性。