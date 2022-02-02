"""
    File name: setup.py
    Author: alexfrias
    Date created: 2/1/22
    Date last modified: 2/1/22
    Python Version: 3.9
"""

from setuptools import setup

setup(
    name='nlp_logix_challenge',
    version='0.0.1',
    author='Alex Frias',
    readme='README.md',
    packages=['nlp_logix_challenge'],
    install_requires=[
        'pandas==1.4.0',
        'requests==2.27.1',
        'scikit-learn==1.0.2',
    ],
    entry_points={
        'console_scripts': [
            'challenge-1 = nlp_logix_challenge.challenge1:run',
            'challenge-2 = nlp_logix_challenge.challenge2:run',
            'challenge-5 = nlp_logix_challenge.challenge5:run',
        ],
    },
    package_data={
        'nlp_logix_challenge': ['Data/*', 'Data/iris_data/*'],
    }
)
