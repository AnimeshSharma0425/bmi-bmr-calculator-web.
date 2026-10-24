def calorie_calculator():

    print("DAILY CALORIE CALCULATOR")

    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    height_m=height/100
    bmi=weight/(height_m**2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"


    print("\nActivity Levels:")
    print("1. Sedentary - Little or no exercise")
    print("2. Lightly Active - Exercise 1-3 days/week")
    print("3. Moderately Active - Exercise 3-5 days/week")
    print("4. Very Active - Exercise 6-7 days/week")

    activity = int(input("Choose activity level (1-4): "))

    if gender == "male":
        bmr = (10*weight)+(6.25*height)-(5*age)+5

    elif gender == "female":
        bmr = (10*weight)+(6.25*height)-(5*age)-161

    else:
        print("Invalid gender!")
        return

    if activity == 1:
        calories = bmr * 1.2

    elif activity == 2:
        calories = bmr * 1.375

    elif activity == 3:
        calories = bmr * 1.55

    elif activity == 4:
        calories = bmr * 1.725

    else:
        print("Invalid activity level!")
        return


    print("\n===== RESULT =====")
    print(f"your BMI is:{bmi}\ncategory:{category}")
    print(f"Your BMR: {bmr:.2f} calories/day")
    print(f"Estimated daily calorie requirement: {calories:.2f} calories/day")


calorie_calculator()
