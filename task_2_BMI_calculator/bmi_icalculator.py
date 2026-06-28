def calculate_bmi(weight, height):
    return weight / (height ** 2)


while True:
    print("\n" + "=" * 45)
    print("         BMI CALCULATOR")
    print("=" * 45)

    try:
        name = input("Enter your name: ")

        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("\n❌ Weight and height must be greater than zero.")
            continue

        bmi = calculate_bmi(weight, height)

        print("\n========== RESULT ==========")
        print(f"Name     : {name}")
        print(f"BMI      : {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
            tip = "Increase healthy calorie intake and exercise regularly."

        elif bmi < 25:
            category = "Normal Weight"
            tip = "Great! Maintain your healthy lifestyle."

        elif bmi < 30:
            category = "Overweight"
            tip = "Regular exercise and a balanced diet are recommended."

        else:
            category = "Obese"
            tip = "Please consult a doctor and start a healthy fitness plan."

        print(f"Category : {category}")
        print(f"Health Tip: {tip}")

    except ValueError:
        print("\n❌ Please enter valid numeric values.")
        continue

    choice = input("\nDo you want to calculate again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using BMI Calculator 😊")
        break