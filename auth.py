#!/usr/bin/env python
# encoding: utf-8
from douban_client import DoubanClient

API_KEY = '0385334896d5f9120a8f99d9c481eb36'
API_SECRET = 'f47becb96d38526d'

# 在 OAuth 2.0 中，
# 获取权限需要指定相应的 scope，请注意!!
# scope 权限可以在申请应用的 "API 权限" 查看。

SCOPE = 'douban_basic_common'

client = DoubanClient(API_KEY, API_SECRET, 'http://127.0.0.1:8000/', SCOPE)

# 以下方式 2 选 1:
# 1. 引导用户授权
print 'Go to the following link in your browser:'
print client.authorize_url
code = raw_input('Enter the verification code:')
client.auth_with_code(code)


# Token Code
token_code = client.token_code

# Refresh Token
# 请注意：`refresh_token_code` 值仅可在授权完成时获取(即在 `auth_with_code`, `auth_with_password` 之后)
refresh_token_code = client.refresh_token_code
client.refresh_token(refresh_token_code)
