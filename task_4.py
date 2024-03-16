import csv


with open("history_mirror.csv", encoding="utf-8") as file:
    data = list(csv.DictReader(file))
    ans = {}

    
    for i in range(len(data)):
        god = data[i]["date"].split("-")[0]
        ans[god] = 0

        
    for i in range(len(data)):
        ans[data[i]["date"].split("-")[0]] += 1

        
    for i in ans:
        print(f"В {i} году зеркало было использовано {ans[i]}")
