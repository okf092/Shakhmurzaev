import csv


with open("history_mirror.csv", encoding="utf-8") as file:
    data = list(csv.DictReader(file))
    ans = []
    for i in range(len(data)):
        if data[i]["verdict"] == "Победа над смертью":
            ans.append(data[i])
            name = data[i]["username"].split()
    name = ans[0]["username"].split()
    fio = f"{name[0]} {name[1][0]}.{name[2][0]}"
    print(f"Сообщение было зафиксировано: {ans[0]["date"]} у пользователя {fio}")


with open("mirror_error.csv", "w", encoding="utf-8") as file:
    new = csv.DictWriter(file, fieldnames=['date','username','verdict'])
    new.writeheader()
    new.writerows(ans)


            
