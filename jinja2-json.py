#! /usr/bin/env python3

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
    template = templateEnv.get_template('data.json')
    print(template.render(context=data))


if __name__ == '__main__':
    main()