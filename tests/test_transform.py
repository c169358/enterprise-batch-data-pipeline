import pandas as pd
from scripts.transform import remove_duplicate_transactions
from scripts.transform import validate_positive_amount
from scripts.transform import classify_transaction_amount


def test_remove_duplicates():
    data = {
        "transaction_id": [1, 1, 2],
        "amount": [100, 100, 200],
        "status": ["COMPLETED", "COMPLETED", "COMPLETED"],
        "transaction_date": ["2026-01-01", "2026-01-01", "2026-01-02"]
    }

    df = pd.DataFrame(data)
    result = remove_duplicate_transactions(df)

    assert len(result) == 2


def test_positive_amount():
    data = {
        "transaction_id": [1, 2],
        "amount": [100, -50],
        "status": ["COMPLETED", "COMPLETED"],
        "transaction_date": ["2026-01-01", "2026-01-02"]
    }

    df = pd.DataFrame(data)
    result = validate_positive_amount(df)

    assert len(result) == 1


def test_classification():
    data = {
        "transaction_id": [1, 2],
        "amount": [100, 6000],
        "status": ["COMPLETED", "COMPLETED"],
        "transaction_date": ["2026-01-01", "2026-01-02"]
    }

    df = pd.DataFrame(data)
    result = classify_transaction_amount(df)

    assert result.loc[0, "transaction_category"] == "NORMAL"
    assert result.loc[1, "transaction_category"] == "HIGH_VALUE"