from setuptools import setup, find_packages
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xayah',
    version='0.0.1',
    description='A lightweight testing tool with test report functionality',
    long_description=long_description,
    license='MIT',
    packages=find_packages(
        include=['src']
    ),
    include_package_data=True,
    install_requires=[
        'pydantic == "1.7.3"',
        'python_version == "3.8"',
    ]
)
