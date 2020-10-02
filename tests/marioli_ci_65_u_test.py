from helpers.load_indicator_to_test import load_indicator_to_test
from helpers.assert_value import assert_value

# Load the indicator dataset
dataset = load_indicator_to_test(__file__)


def test_iceland():
    assert_value(1.037, "ISL", "2020-04-07", dataset, decimals=3)


def test_united_states():
    assert_value(2.696, "NLD", "2020-03-09", dataset, decimals=3)
