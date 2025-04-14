swimming_time = int(input("Enter swimming your time.\n"))
cycling_time = int(input("Enter your cycling time.\n"))
running_time = int(input("Enter your running time.\n"))

total_time = swimming_time + cycling_time + running_time

if (total_time > 0) and (total_time <= 100):
    print("Award: Provinvial colours")
elif (total_time >= 101) and (total_time <= 105):
    print("Award: Provincial half colours")
elif (total_time >= 106) and (total_time <= 110):
    print("Award: Provincial scroll")
elif total_time > 111:
    print("Award: No award")