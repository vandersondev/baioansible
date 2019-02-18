#! /usr/bin/env python3
from yaml import load
from jinja2 import Environment, FileSystemLoader

def main():
    data = [
        {
            'name': 'Paramiko',
            'version': '2.0'
        },
        {
            'name': 'Jinja2',
            'version': '2.10.x'
        }
    ]

    loader = FileSystemLoader('./')
    templateEnv = Environment(loader=loader)
    template = templateEnv.get_template('data.yaml')
    yamlData = template.render(context=data)
    print(load(yamlData))


if __name__ == '__main__':
    main()