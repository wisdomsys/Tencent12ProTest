import json
import random
import re

import pytest
import requests


@pytest.fixture(scope='session')
def test_token():
    res = None
    # 获取token
    corpid = 'wwdfdeefbb90350b71'
    corpsecret = 'g5WM5YLPqTCe-Jma4nnbdGhvpuwc5QLqZHqHymRq_Y4'
    ret = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print(ret.json())
    return ret.json()['access_token']


def test_add_pepper(userid, name, mobile, test_token):
    # 添加成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }

    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}', json=data)
    return res.json()


def test_read_pepper(userid, test_token):
    # 读取成员
    ret = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}')
    return ret.json()


def test_update(userid, name, mobile, test_token):
    # 更新成员
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
    }
    ret = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}', json=data)
    return ret.json()


def test_delete(userid, test_token):
    # 删除指定用户
    ret = requests.get(
        f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}')
    return ret.json()


def test_create_data():
    # data = [(str(random.randint(0, 100000000)), '李四', str(random.randint(13800000000, 13890000000))) for x in range(10)]
    data = [('test' + str(x), '李四', '138%08d' % x) for x in range(10)]
    return data


# @pytest.mark.parametrize('userid,name,mobile', [('zhangsan', '李四', '13799999999')])
@pytest.mark.parametrize('userid,name,mobile', test_create_data())
def test_all(userid, name, mobile, test_token):
    # 可能会出现创建用户失败的情况
    try:
        assert 'created' == test_add_pepper(userid, name, mobile, test_token)["errmsg"]
    except AssertionError as e:
        if 'mobile existed' in e.__str__():
            re_userid = re.findall(":(.*)$", e.__str__()[0])
            if re_userid.endswith("'") or re_userid.endwith():
                re_userid = re_userid[:-1]
            assert 'deleted' == test_delete(re_userid, test_token)['errmsg']
            assert 60111 == test_read_pepper(userid, test_token)['errcode']
            assert 'created' == test_add_pepper(userid, name, mobile, test_token)["errmsg"]
    # 可能会发生name不存在的异常情况
    assert name == test_read_pepper(userid, test_token)['name']
    assert 'updated' == test_update(userid, '修改名', mobile, test_token)['errmsg']
    assert '修改名' == test_read_pepper(userid, test_token)['name']
    assert 'deleted' == test_delete(userid, test_token)['errmsg']
    assert 60111 == test_read_pepper(userid, test_token)['errcode']
