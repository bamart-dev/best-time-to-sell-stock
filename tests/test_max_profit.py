from main import max_profit

inputs = {
    "empty": [],
    "single": [5],
    "nominal": [7, 1, 5, 3, 6, 4],
    "ascending": [1, 2, 3, 4, 5],
    "same": [8, 8, 8, 8],
    "no profit": [7, 6, 4, 3, 1],
}


def test_max_profit():
    prices = inputs["nominal"]

    assert max_profit(prices) == 7


def test_max_profit_increasing():
    prices = inputs["ascending"]

    assert max_profit(prices) == 4


def test_max_profit_no_profit():
    prices = inputs["no profit"]

    assert max_profit(prices) == 0


def test_max_profit_empty():
    prices = inputs["empty"]

    assert max_profit(prices) == 0


def test_max_profit_single_value():
    prices = inputs["single"]

    assert max_profit(prices) == 0


def test_max_profit_all_same_value():
    prices = inputs["same"]

    assert max_profit(prices) == 0
