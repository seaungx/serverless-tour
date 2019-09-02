from __future__ import print_function

import urllib.request
import urllib.parse
import urllib.error
import json


def lambda_handler(event, context):
    # 授权用户身份信息
    authorizer = event.get('requestContext').get('authorizer')
    # 用户key
    user_key = authorizer.get('key')
    if authorizer.get('bool') == 'true':
        print('user :{}'.format(user_key))
        body_json = {}
        # 业务了逻辑....
        api_rep = {
            "isBase64Encoded": "false",
            "statusCode": "200",
            "headers": {"content-type": "application/json;charset=utf-8", "access-control-allow-origin": "*"},
            "body": json.dumps({"flag": "success", "data": body_json['data']})
        }
        return api_rep
    else:
        msg = "用户没权限访问，请向管理员申请授权接口：{}".format("api")
        api_rep = {
            "isBase64Encoded": "false",
            "statusCode": "200",
            "headers": {"content-type": "application/json;charset=utf-8", "access-control-allow-origin": "*"},
            "body": json.dumps({"flag": "limit", "msg": msg})
        }
        return api_rep


def get_server_data(request_url):
    try:
        # 发起请求
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/76.0.3809.87 Safari/537.36'}
        req = urllib.request.Request(url=request_url, headers=headers)
        request = urllib.request.urlopen(req)
        response_body = request.read().decode('utf-8')
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f'[!] request exception in urllib.request {e}')
        raise e
    if response_body:
        # 获取请求内容
        return response_body
    else:
        raise ValueError('调用获取数据接口失败')


def post_server_data(request_url, data):
    try:
        # 发起请求
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/76.0.3809.87 Safari/537.36'}
        data = json.dumps(data)
        data = bytes(data, 'UTF8')
        req = urllib.request.Request(url=request_url, headers=headers, data=data, method='POST')
        request = urllib.request.urlopen(req)
        response_body = request.read().decode('utf-8')
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        print(f'[!] request exception in urllib.request {e}')
        raise e
    if response_body:
        # 获取请求内容
        return response_body
    else:
        raise ValueError('调用获取数据接口失败')
