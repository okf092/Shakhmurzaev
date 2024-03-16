import csv


def new_fio(s: str): ## ф-ция хэша
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l:i for i, l in enumerate(alphabet, 1)}
    p = 67
    m = 10**9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = hash_value + (d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)

with open("history_mirror.csv", encoding="utf-8") as file: ## создание id
    data = list(csv.DictReader(file))
    for i in range(len(data)):
        has = new_fio(data[i]["username"])
        data[i]["ID"] = has


with open("users_with_hash.csv", "w", encoding="utf-8") as file: ## запись в файл
    new = csv.DictWriter(file, fieldnames=['date','username','verdict', 'ID'])
    new.writeheader()
    new.writerows(data)
    
    

