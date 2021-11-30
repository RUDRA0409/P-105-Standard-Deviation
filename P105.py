import math
import csv
with open("105data.csv") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#mean
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total += int(x)

    mean=total/n
    return mean

#squaring and getting the values
squared_lists=[]
for number in data:
    a=int(number) -  mean(data)
    a=a**2 
    squared_lists.append(a)   

#getting sum
sum=0
for i in squared_lists:
    sum = sum +i    

#dividing the sum by the total values
result = sum/ (len(data)-1)

std_dev= math.sqrt(result)
print(f" std deviation is : {std_dev}")