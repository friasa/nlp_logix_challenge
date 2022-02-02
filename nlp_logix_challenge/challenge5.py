"""
    File name: challenge5.py
    Author: alexfrias
    Date created: 2/1/22
    Date last modified: 2/1/22
    Python Version: 3.9
"""
import requests
from time import time


def run():
    scrape('https://scikit-learn.org/stable/modules/generated/sklearn'
           '.ensemble.RandomForestClassifier.html',
           'web-download.html')


def scrape(url, filename) -> None:
    t0 = time()
    r = requests.get(url)
    t1 = time()
    print(f'Download took {(t1-t0)*1000:.2f} milliseconds.')

    with open(filename, 'w+') as out:
        out.write(r.text)


if __name__ == '__main__':
    run()
