def calculate_blood_alcohol_concentration(alcohol_amount, weight, gender):
    if gender.lower() == 'male':
        k = 0.7
    elif gender.lower() == 'female':
        k = 0.6
    else:
        raise ValueError("Gender should be either 'male' or 'female'.")

    p = (alcohol_amount * 0.789) / (k * weight)
    return p


if __name__ == '__main__':
    try:
        alcohol_amount = float(input("Enter the amount of pure alcohol drunk (in grams): "))
        weight = float(input("Enter the weight of the user in kilograms: "))
        gender = input("Enter the gender of the user (male/female): ")

        result = calculate_blood_alcohol_concentration(alcohol_amount, weight, gender)
        print(f"The calculated alcohol concentration in per mille is: {result:.2f}‰")
    except ValueError as e:
        print(f"Error: {e}")
