#BMI Calculator

def bmi_calculator():
    weight = float(input("Enter your weight"))
    height = float(input("Enter your height"))
    bmi = weight/(height**2)
    return f"you weigh {weight} and are {height}'s tall, your bmi is {bmi}"

print(bmi_calculator())