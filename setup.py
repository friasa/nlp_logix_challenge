"""
    File name: setup.py
    Author: alexfrias
    Date created: 2/1/22
    Date last modified: 2/1/22
    Python Version: 3.7
"""

from setuptools import setup

setup(
    name='nlp_logix_challenge',
    version='0.0.1',
    packages=['nlp_logix_challenge'],
    install_requires=[
        # 'build==0.7.0',
        # 'certifi==2021.10.8',
        # 'charset-normalizer==2.0.11',
        # 'idna==3.3',
        # 'joblib==1.1.0',
        # 'numpy==1.22.1',
        # 'packaging==21.3',
        'pandas==1.4.0',
        # 'pep517==0.12.0',
        # 'pyparsing==3.0.7',
        # 'python-dateutil==2.8.2',
        # 'pytz==2021.3',
        'requests==2.27.1',
        'scikit-learn==1.0.2',
        # 'scipy==1.7.3',
        # 'six==1.16.0',
        # 'threadpoolctl==3.1.0',
        # 'tomli==2.0.0',
        # 'urllib3==1.26.8',
    ],
    entry_points={
        'console_scripts': [
            'challenge-1 = nlp_logix_challenge.challenge1:run',
            'challenge-2 = nlp_logix_challenge.challenge2:run',
            'challenge-5 = nlp_logix_challenge.challenge5:run',
        ],
    },
    package_data={
        'Data': ['*']
    }
)
