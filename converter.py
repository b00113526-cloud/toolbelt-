while True:
    kms_dis = input('Enter distance in kilometers: ')
    try:
        km= float(kms_dis)
        if km < 0:
            print('Distance cannot be negative. Please enter a positive number.')
        else:
            break
    except ValueError:
        print('Please enter a valid number for kilometers.')

miles = km * 0.621371
print(round(miles,2))



