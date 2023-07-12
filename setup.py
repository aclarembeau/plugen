from pathlib import Path

from setuptools import setup, find_packages


setup(
    entry_points={
        'console_scripts': [
            'plugen = plugen:main',
        ],
    },
    name='plugen',
    version='1.1.2',
    license='MIT',
    site="https://github.com/aclarembeau/plugen",
    author="Clarembeau Alexis",
    author_email='alexis.clarembeau@gmail.com',
    packages=find_packages('./'),
    package_dir={'': './'},
    url='https://github.com/aclarembeau/plugen',
    keywords='static website generator',
    install_requires=['PyYAML', 'websockets'],
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown'
)
