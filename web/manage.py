#!/usr/bin/env python
import importlib
import os
import sys

from django.core.management import execute_from_command_line


SETTINGS_MODULE_PREFIX = 'slides.settings.'
CONFIG_FILENAME = '.django_settings_module'

# Get a fully qualified path for the config file.
# This will let us run manage from outside this directory.
cwd = os.path.dirname(__file__)
CONFIG_FILENAME = os.path.join(cwd, CONFIG_FILENAME)


def read_settings_module():
    with open(CONFIG_FILENAME, 'r', encoding='utf-8') as fin:
        settings_module = fin.read()
        settings_module = settings_module.strip()
        return settings_module


def write_settings_module(module):
    with open(CONFIG_FILENAME, 'w+', encoding='utf-8') as fout:
        fout.write(module)


def prompt_settings_module():
    module = input("Settings Module {}".format(SETTINGS_MODULE_PREFIX))
    module = module.strip()
    return '{}{}'.format(SETTINGS_MODULE_PREFIX, module)


settings_module = ''
try:
    settings_module = read_settings_module()

# When we can't open the file, let's try to create one.
except IOError as e:
    settings_module = prompt_settings_module()
    write_settings_module(settings_module)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    execute_from_command_line(sys.argv)


