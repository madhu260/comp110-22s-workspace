courses: dict[int, str] = dict()
courses[110] = "Intro to Programming"
courses[210] = "Data Structures"


schools = {"UNC": 19400, "Duke": 6700, "NCSU": 26100}


# Example looping over the keys of a dict
# for key in schools:
#     print(f"Key: {key} -> Value: {schools[key]}")


points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100

print(points["Kaki"])