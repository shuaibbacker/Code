#python Basics
# variables

p=12
v=13
result= p+v
print(result)

#examples
name = input(str("What is your name: "))
print(name)

# Conditions

# if
# if....else

X = 13
Y = 15
if (X>Y):
    print("X greater than Y")
else:
    print("Y is greater than X")


# if-elif statement

score= 99
if score>=92:
    print("grade A")
elif score>=82:
    print("grade B")
else:
    print("grade c")
# Loops 

# for Loops


fruits=["apple","banana","watermelon"]
for fruit in fruits:
    print (fruit)
    
# While Loop

i = 0
while i <= 5:
    i+=1
    print(i)

for i in range(1,10):
    print(i)    

# Break

for i in range(12):
    if i == 5:
        break
    print(i)

# Continue

for i in range(12):
    if i == 8:
        continue
    print(i)

# Nested loop

for i in range(5):
    for j in range(3):
        for k in range(2):
            print(f"({i},{j},{k})")  

# file operation

#setting path
file_path = "C:\\Users\\shuai\\myproject\\notes\\notes01_setup.md.txt"
with open(file_path, 'r') as file:
    content = file.read()
    print(content)     

#file write
with open(file_path, 'w')as file:   
    content = file.write("hi how are u?")   
    print(file)  

#testing variable mem
p=5
print(id(p))
p=3
print(p)
print(id(p))

############################################################################################

# pandas

import pandas as pd
df = pd.read_csv("C:\\Users\\shuai\\AppData\\Local\\Programs\\Thonny\\Iris.csv")
print(df)

#Load SQLite DB

import sqlite3 as sqlite
connect = sqlite.connect("C:\\Users\\shuai\\Downloads\\chinook\\chinook.db")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type= 'table';",connect)
print(tables)
#df=pd.read_sql_query('SELECT * FROM ',connect)

#close connection

