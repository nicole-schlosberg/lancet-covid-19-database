import pandas

from config import CODEBOOK_PATH, DATABASE_PATH, INDICATORS

database = pandas.read_csv(DATABASE_PATH)
indicator_ids_in_db = list(set(database.columns) - set(['country', 'date']))

def test_that_database_contains_all_indicators_defined_in_codebook():
    codebook = pandas.read_csv(CODEBOOK_PATH)
    indicators_defined_in_codebook = codebook['indicator'].tolist()
    assert indicator_ids_in_db.sort() == indicators_defined_in_codebook.sort()

def test_that_database_contains_all_indicators_defined_in_config():
    indicators_defined_in_config = [x['id'] for x in INDICATORS]
    assert indicator_ids_in_db.sort() == indicators_defined_in_config.sort()

def test_that_there_are_no_empty_rows():
    df = database.loc[:, ~database.columns.isin(['country', 'date'])]
    df = df.isnull().all(axis='columns')
    rows_that_are_empty = list(df.index[df])
    print(rows_that_are_empty)
    assert len(rows_that_are_empty) == 0
