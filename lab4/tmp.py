weight_in_kilogram = float(input('Enter your weight in kg:'))
height_in_meters = float(input('Enter your height in meters:'))

BMI = weight_in_kilogram / (height_in_meters*height_in_meters)

print(round(BMI,2))

