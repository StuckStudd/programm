import json
import time
import os
from colorama import Style, Fore


print("Welcome!")
time.sleep(2)

print("Loading..")

with open("database.json", "r") as f:
    data = json.load(f)

def save_data():
    with open('database.json', "w") as f:
        json.dump(data, f, indent=4)

if not data['login'] or not data['password']:
    print("Time to register.")

    register = input("Write your login -->> ")
    data['login'] = register

    password = input("Write new password -->> ")
    data['password'] = password

    save_data()

    print(f"Name : {data['login']}, Password : {data['password']}")
else:
    print(f"Welcome back, {data['login']}!")