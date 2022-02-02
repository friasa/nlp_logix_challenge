"""
    File name: challenge2.py
    Author: alexfrias
    Date created: 2/1/22
    Date last modified: 2/1/22
    Python Version: 3.9
"""
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import os


def run():
    classify('metrics.txt')


def classify(filename) -> None:
    attrs = ['sepal_length', 'sepal_width',
             'petal_length', 'petal_width',
             'class']

    data_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'Data/iris_data/iris.data')
    df = pd.read_csv(data_file, names=attrs)

    # Mapping to numbers so we can classify
    mapping = {'Iris-setosa': 1,
               'Iris-versicolor': 2,
               'Iris-virginica': 3}

    # apply the mapping
    df['class'] = df['class'].apply(lambda x: mapping[x])

    # separate into attributes and labels
    X = df.values[:, 0:4]
    y = df.values[:, 4]

    # Split into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Fit the model
    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)

    # make the prediction
    prediction = rfc.predict(X_test)

    with open(filename, 'w+') as out:
        out.write(f'Accuracy: '
                  f'{metrics.accuracy_score(y_test, prediction) * 100:.2f}%\n')
        out.write(f'Confusion Matrix:'
                  f'\n{metrics.confusion_matrix(y_test, prediction)}')


if __name__ == '__main__':
    run()
