from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Ahmed Eladdad',
    author_email='eehaddad@gmail.com',
    description='A utility for backing up PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='github.com/example',
    packages=find_packages('src')
)
