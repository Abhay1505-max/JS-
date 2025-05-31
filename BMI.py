height=int(input("Enter your height in cm: "))
weight=int(input("Enter your weight in kg: "))
height=height/100
bmi=weight/(height)**2
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi or bmi < 24.9:
    print("You are normal weight")
elif 25 <= bmi or bmi < 29.9:
    print("You are overweight")
elif(bmi>=30):
    print("You are obese")