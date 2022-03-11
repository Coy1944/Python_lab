
# PROBLEM 2
data = open('../CupcakeInvoices.csv')

#PROBLEM 3
for row in data:
  print(row)

#PROBLEM 4
for row in data:
 values = row.split(',')
 print(values[2])

 #PROBLEM 5

for row in data:
 values = row.split(',')
 total = int(values[3]) * float(values[4])
 print(total)

 #Problem 6

 total = 0


for row in data:
 values = row.split(',')
 total = total + (int(values[3]) * float(values[4]))
   
print(total)


#PROBLEM 7
data.close()

# OR IF YOU HAVE IT OPEN BY OPEN_FILE
#open_file.close()

#GOING FURTHER
import matplotlib.pyplot as plt

data = open('CupcakeInvoices.csv')



chocolate = 0
vanilla = 0
strawberry = 0

for line in open_file:
    info = line.rstrip('\n').split(',')
    if info[2] == 'Chocolate':
        chocolate += float(info[4])
    elif info[2] == 'Vanilla':
        vanilla += float(info[4])
    elif info[2] == 'Strawberry':
        strawberry += float(info[4])

chocolate = round(chocolate, 4)
vanilla = round(vanilla, 4)
strawberry = round(strawberry, 4)

flavors = 'Chocolate', 'Vanilla', 'Strawberry'
sales = [chocolate, vanilla, strawberry]

fig1, ax1 = plt.subplots()
ax1.pie(sales, labels=flavors, autopct='%1.1f%%')
ax1.axis('equal')
plt.show()