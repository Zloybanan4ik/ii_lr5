from src.person_manager import *

df = pd.DataFrame(columns=["Фамилия", "Имя", "Телефон", "Дата рождения"])

# Пример
df = add_person(df, "Иванов", "Петр", "89101234567", "01.03.1990")
df = add_person(df, "Сидорова", "Анна", "89001112233", "25.03.1995")

print(find_by_month(df, 3))

save_to_parquet(df)

