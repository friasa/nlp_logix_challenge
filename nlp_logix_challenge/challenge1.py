"""
    File name: challenge1.py
    Author: alexfrias
    Date created: 2/1/22
    Date last modified: 2/1/22
    Python Version: 3.9
"""
import pandas as pd
import os


def run():
    # City of Pittsburgh Playground Equipment Data
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'Data/e39ef76e-0a11-47c8-a86f-a37f55db7a2b.csv')
    df = read_csv(file_path)
    print_info(df)
    combine_columns(df)


def read_csv(filename) -> pd.DataFrame:
    return pd.read_csv(filename, index_col='id')


def print_info(_df: pd.DataFrame) -> None:
    print(f'Sorted Columns: {sorted(_df.columns)}')
    print(f'Number of rows: {_df.shape[0]}')


def combine_columns(_df: pd.DataFrame) -> None:
    # Map Street Number and Street to make Full Street
    _df['full_street'] = _df.apply(
        lambda x:
            # Change to int to avoid e.g. '844.0'
            f'{int(x.street_number) if not pd.isna(x.street_number) else ""} '
            f'{x.street}',
        axis=1
    )
    _df.to_csv('pittsburgh_playground_data.csv')


if __name__ == '__main__':
    run()
