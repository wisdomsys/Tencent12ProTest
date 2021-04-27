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
