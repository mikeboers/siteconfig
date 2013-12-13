from setuptools import setup, find_packages

setup(
    
    name='ficonfig',
    version='0.1.0',
    description='Configuration of Fluent Image processes.',
    url='http://github.com/mikeboers/ficonfig',
    
    packages=find_packages(exclude=['tests', 'tests.*']),
    
    author='Mike Boers',
    author_email='ficonfig@mikeboers.com',
    license='BSD-3',

    entry_points={
        'console_scripts': [
            'ficonfig = ficonfig.commands.main:main',
        ],
    },

)
