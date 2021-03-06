from setuptools import setup, find_packages

setup(
    
    name='siteconfig',
    version='0.1.0',
    description='Configuration of Python processes.',
    url='http://github.com/mikeboers/siteconfig',
    
    packages=find_packages(exclude=['tests', 'tests.*']),
    
    author='Mike Boers',
    author_email='siteconfig@mikeboers.com',
    license='BSD-3',

    entry_points={
        'console_scripts': [
            'siteconfig = siteconfig.commands.main:main',
        ],
    },

)
