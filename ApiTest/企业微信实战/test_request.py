import json

import requests


# corpid：wwdfdeefbb90350b71
# AgentId：3010011
# corpsecret：g5WM5YLPqTCe-Jma4nnbdGhvpuwc5QLqZHqHymRq_Y4
def test_token():
    res = None
    # 获取token
    corpid = 'wwdfdeefbb90350b71'
    corpsecret = 'g5WM5YLPqTCe-Jma4nnbdGhvpuwc5QLqZHqHymRq_Y4'
    ret = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    return ret.json()['access_token']


def test_add_pepper():
    # 添加成员
    data = {
        "userid": "zhangguangzhou",
        "name": "张广州",
        "mobile": "13800000000",
        "department": [1],
    }

    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token()}', json=data)
    print(res.json())


def test_read_pepper():
    # 读取成员
    userid = 'yangchao'
    ret = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token()}&userid={userid}')
    print(ret.json())


def test_update():
    # 更新成员
    data = {
        "userid": "zhangguangzhou",
        "name": "李四",
        "department": [1],
        "order": [10],
        "position": "后台工程师",
        "mobile": "13800000000",
        "gender": "1",
        "email": "zhangsan@gzdev.com",
    }
    ret = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token()}', json=data)
    print(ret.json())


def test_delete():
    ret = requests.get(
        f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token()}&userid=zhangguangzhou')
    print(ret.json())


def test_create_department():
    # 创建部门
    data = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1,
        "id": 2
    }
    ret = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}', json=data)
    print(ret.json())


def test_update_department():
    # 更新部门
    data = {
        "id": 2,
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1
    }

    ret = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}', json=data)
    print(ret.json())


def test_delete_department():
    # 删除部门
    ret = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2')
    print(ret.json())

