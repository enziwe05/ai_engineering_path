#project 1 - Calorie Tracker

#my data
daily_goal = 0 
meals = []

#set goals
def set_goals():
    goal = float(input("Enter your daily calorie goal"))
    return goal 


def add_meals():
    meal = {}
    meal["name"] = input("Enter a meal")
    meal["calories"] = float(input("How many calories is it"))
    meal["protein"] =  int(input("How much protien does it have"))
    return meal



#3
def view_meals():
    for meal in meals:
        print(f"{meal['name']} - {meal['calories']} calories - {meal['protein']}g protein")


def remaining_calories():
    total = 0
    for meal in meals:
        total += meal["calories"]
    return daily_goal - total

def total_protein():
    total = 0
    for meal in meals:
        total += meal["protein"]        
    return total

while True:
    print("\n==========================")
    print("   CALORIE TRACKER")
    print("==========================")
    print("1. Set daily goal")
    print("2. Add meal")
    print("3. View meals")
    print("4. Remaining calories")
    print("5. Total protein")
    print("6. Quit")
    print("==========================")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        daily_goal= set_goals()
    elif choice == "2":
        meals.append(add_meals())
    elif choice == "3":
        view_meals()
    elif choice == "4":
        print(f"Remaining calories: {remaining_calories()}")  
    elif choice == "5":
        print(f"Total protein: {total_protein()}g") 
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
