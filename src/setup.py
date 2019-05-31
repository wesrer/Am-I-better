from setuptools import setup, find_packages

setup(
    name='Am I Better',
    version='0.1',
    packages=find_packages(),
    py_modules=['yourscript'],
    install_requires=[
        'Click',
        'python-dateutil'
    ],
    entry_points='''
        [console_scripts]
        yourscript=yourscript:cli
    ''',
)