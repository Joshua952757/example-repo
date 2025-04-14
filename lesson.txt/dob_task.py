txt_file = "DOB.txt"
with open(txt_file, "r") as file:
    lines = file.readlines()

names = []
birthdates = []
for line in lines:
    parts = line.strip().split(maxsplit=2)
    names.append(f"{parts[0]} {parts[1]}")
    birthdates.append(parts[2])

print("Name")
print("\n".join(names))
print("\nBirthdate")
print("\n".join(birthdates))
