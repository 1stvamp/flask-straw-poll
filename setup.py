"""Installer for flask-straw-poll
"""

from setuptools import setup, find_packages

setup(
    name='flask-straw-poll',
    description='Example straw poll Flask app',
    long_description=open('README.rst').read(),
    provides=['flask_straw_poll'],
    version='1.0.0',
    author='Wes Mason',
    author_email='wes@1stvamp.org',
    url='https://github.com/1stvamp/flask-straw-poll',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=open('requirements.txt').readlines(),
    package_data={'flask_straw_poll/data': ['wmc.json.example']},
    include_package_data=True,
    license='BSD'
)
