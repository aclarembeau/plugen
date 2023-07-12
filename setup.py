from setuptools import setup, find_packages


setup(
    entry_points={
        'console_scripts': [
            'plugen = plugen:main',
        ],
    },
    name='plugen',
    version='1.0.4',
    license='MIT',
    author="Clarembeau Alexis",
    author_email='alexis.clarembeau@gmail.com',
    packages=find_packages('./'),
    package_dir={'': './'},
    url='https://github.com/aclarembeau/plugen',
    keywords='static website generator',
    install_requires=['PyYAML', 'websockets'],
)
