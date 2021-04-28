import yaml


def test_yaml_load():
    with open('../data/main.yaml', encoding='utf-8') as  f:
        steps = yaml.safe_load(f)
    for step in steps:
        if 'by' in step.keys():
            print('查找元素')
        if 'action' in step.keys():
            print('动作解析')
            action = step['action']
            if 'click' == action:
                print('click操作')
            if 'send' == action:
                value = step['value']
                print(f'send({value})')


def test_replace():
    _parame = {'name': '12345'}
    str = 'xxxxxxxxxxxxxx ${name} llllllllll'
    for key, value in _parame.items():
        # str = str.replace(f'${{{key}}}', value)
        # str = str.replace('${{{}}}'.format(key), value)
        str = str.replace('${' + key + '}', value)
    print(str)
