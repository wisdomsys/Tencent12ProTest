
import yaml

with open('main.yaml') as f:
    steps = yaml.safe_load(f)
    s = list(steps.keys())
    print(steps,s[0])
    # for step in steps['mine']:
    #     if 'by' in step.keys():
    #         print(step['by'])
    #     if 'action' in step.keys():
    #         action = step['action']
    #         if action == 'click':
    #             print(step['click'])