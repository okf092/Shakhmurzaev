import csv


with open("history_mirror.csv", encoding="utf-8") as file:
    data = list(csv.DictReader(file))
    while True:
        fio = input()
        if fio == "stop":
            break
        else:
            for i in range(len(data)):
                if fio in data[i]["username"]:
                    print(data[i]["verdict"])
                    break
            
                    


