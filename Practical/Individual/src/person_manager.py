import pandas as pd
from datetime import datetime
import pyarrow as pa
import pyarrow.parquet as pq


def add_person(df, surname, name, phone, birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y")
    new_row = pd.DataFrame(
        [[surname, name, phone, birthdate]],
        columns=["Фамилия", "Имя", "Телефон", "Дата рождения"],
    )
    df = pd.concat([df, new_row], ignore_index=True)
    return df.sort_values(by=["Фамилия", "Имя"]).reset_index(drop=True)


def find_by_month(df, month):
    return df[df["Дата рождения"].dt.month == month]


def save_to_parquet(df, filename="people.parquet"):
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)


def load_from_parquet(filename="people.parquet"):
    table = pq.read_table(filename)
    return table.to_pandas()
