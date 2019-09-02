from __future__ import print_function
from jwt_function.lib import jwt

import datetime


def handler(event, context):

    # 用户信息，可自行选择设置,可加入登录授权具体功能实现|钉钉扫描登录相关业务
    # 此处设置了用户id,用户名，token 过期时间
    user = {
        'id': 1,
        'user_name': 'silly_dog',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
    }
    # 获取私钥
    private_file = open('private.key')
    # 生成token
    encoded = jwt.encode(user, private_file.read(), algorithm='RS256')
    return {
        'statusCode': 200,
        'data': {'token': str(encoded, "utf-8")}
    }
