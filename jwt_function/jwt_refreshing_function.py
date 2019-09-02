from __future__ import print_function

from jwt_function.lib import jwt
import datetime


# 刷新token
def handler(event, context):
    if not (event['authorizationToken'] is None):
        try:
            encoded = event['authorizationToken']
            public_file = open('public.key')
            decode = jwt.decode(encoded, public_file.read(), leeway=3660, algorithm='RS256')
            private_file = open('private.key')
            user = {
                'id': decode.get('id'),
                'username': decode.get('username'),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
            }
            refresh_token = jwt.encode(user, private_file.read(), algorithm='RS256')
            return {
                'statusCode': 200,
                'data': {'token': str(refresh_token, "utf-8")}
            }
        # token 过期
        except jwt.ExpiredSignatureError as e:
            print("error :{}".format(e))
            return {
                'statusCode': 200,
                'data': {'err': "token已过期"}
            }
    else:
        return {
            'statusCode': 200,
            'data': {'err': "token已过期"}
        }
