"""
Create new cpp project template from terminal.
"""

import os
import click

from pathlib import Path
from shutil import copyfile
from time import sleep

CONFIG_PATH = '~/.new'


@click.command()
@click.argument('project_name', type=str)
@click.option('-i', is_flag=True, help='Add test input data')
@click.option('-a', is_flag=True, help='Add test arguments')
@click.option('--editor', default='vim', help='Specify in what editor you want to edit test data, vim by default')
def main(project_name, i, a, editor):

    click.echo("Creating new C++ project " + project_name)
    os.mkdir(project_name)
    os.chdir(project_name)

    # filenames = [f'{CONFIG_PATH}/header', f'{CONFIG_PATH}/main.cpp']
    if os.path.isfile(f'{CONFIG_PATH}/header'):
        # filenames.insert(0, f'{CONFIG_PATH}/header')
        os.system('cat ~/.new/header > main.cpp')
        sleep(0.2)

    os.system('cat ~/.new/main.cpp >> main.cpp')
    # with open(f'{project_name}/main.cpp', 'w') as outfile:
    #     for file_name in filenames:
    #         with open(file_name) as infile:
    #             outfile.write(infile.read())

    if i:
        input_path = f'{CONFIG_PATH}/input.in'
        Path(input_path).touch()
        os.system(f'{editor} {input_path}')
    if a:
        arguments_path = f'{CONFIG_PATH}/arguments'
        Path(arguments_path).touch()
        os.system(f'{editor} {arguments_path}')

    copyfile(f'{CONFIG_PATH}/Makefile', project_name)
