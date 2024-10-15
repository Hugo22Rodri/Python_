import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile)
      data = dict(reader)
      valuesDict = data.values()

    total = 0
    for number in valuesDict:
       intNum = int(number)
       total += intNum
    return total

response = read_csv('Data.csv')
print(response)