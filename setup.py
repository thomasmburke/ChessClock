# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='ChessClock',
    version='0.0.0',
    description='chess blitz clock',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English'
        ],
    author='Thomas Burke',
    author_email='tburke@bu.edu',
    url='https://github.com/thomasmburke/ChessClock',
    py_modules=['chess_clock'],
    install_requires = ['pygame']
)
