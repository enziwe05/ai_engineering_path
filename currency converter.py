```python
import json
import requests

#stage 1
response = requests.get("https://open.er-api.com/v6/latest/USD")
print (response.status_code)

#stage 2/3
def convert(amount, target):

    rate = response.json()["rates"]

    if not isinstance(amount, float):
        return "sorry thats not a number"
    if target not in rate:
        return "that is not a currency"
    else:
        result = amount * rate[target]
        print(f"{amount} USD = {round(result,2)} {target}")
        history.append({"from": "USD", "to": target, "amount": amount, "result": round(result, 2)})

#stage 4

def save_history():
    with open("history.json", "w") as file:
        json.dump(history, file)

def load_history():
    with open("history.json", "r") as file:
        return json.load(file)


try:
    history = load_history()
except:
    history = []

#stage 6

while True:
    print("\n==========================")
    print("   converter")
    print("==========================")
    print("1. convert")
    print("2. see history")
    print("3. quit")
    print("==========================")

    choice = input("Enter choice")

    if choice == "1" :
        to = input("FROM USD to:")
        amount = input("Amount")
        try:
            amount = float(amount)
        except ValueError:
            print("thats not a number")
            continue
        convert(amount, to)
        save_history()
    elif choice == "2":
        for hist in history:
            print(hist)
    elif choice == "3": 
        break
    else:
        print("that is not a valid choice")
