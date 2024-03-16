import csv

def sortir(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

with open("history_mirror.csv", encoding="utf-8") as file:
    data = list(csv.DictReader(file))
    
