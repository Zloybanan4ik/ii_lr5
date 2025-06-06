import pandas as pd
from src.person_manager import add_person


def test_add_person():
    df = pd.DataFrame(columns=["Фамилия", "Имя", "Телефон", "Дата рождения"])
    df = add_person(df, "Иванов", "Иван", "89101234567", "01.01.2000")
    assert len(df) == 1
    assert df.iloc[0]["Имя"] == "Иван"

