
from setuptools import setup

setup(
    
    name='ficonfig',
    version='0.1.0',
    description='Configuration of Fluent Image processes.',
    url='http://github.com/mikeboers/ficonfig',
    
    py_modules=['ficonfig'],
    
    author='Mike Boers',
    author_email='ficonfig@mikeboers.com',
    license='BSD-3',

    entry_points={
        'console_scripts': [
            'ficonfig = ficonfig.commmands.main:main',
        ],
    },

)
