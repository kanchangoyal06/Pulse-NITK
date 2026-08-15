import json

with open("backend/data.json", "r") as f:
    data = json.load(f)

demo_users = [
    ("Demo", "Student1", "demo1@example.com", "9000000001", "2440013", "Demo@123", "STUDENT"),
    ("Demo", "Organizer1", "organizer1@example.com", "9000000002", "2440015", "Demo@123", "ORGANIZER"),
    ("Demo", "Student2", "demo2@example.com", "9000000003", "2440033", "Demo@123", "STUDENT"),
    ("Demo", "Student3", "demo3@example.com", "9000000004", "2440044", "Demo@123", "STUDENT"),
    ("Demo", "Student4", "demo4@example.com", "9000000005", "2440014", "Demo@123", "STUDENT"),
    ("Demo", "Student5", "demo5@example.com", "9000000006", "2440022", "Demo@123", "STUDENT"),
    ("Demo", "Student6", "demo6@example.com", "9000000007", "2440023", "Demo@123", "STUDENT"),
    ("Demo", "Organizer2", "organizer2@example.com", "9000000008", "2440025", "Demo@123", "ORGANIZER"),
]

# Map original registration numbers to demo registration numbers
reg_map = {}

for user, demo in zip(data["users"], demo_users):
    name, surname, email, phone, reg, password, role = demo

    old_reg = user.get("regNumber")
    reg_map[old_reg] = reg

    user_id = user.get("id")

    user.clear()
    user.update({
        "id": user_id,
        "name": name,
        "surname": surname,
        "age": "21",
        "gender": "Other",
        "email": email,
        "phone": phone,
        "regNumber": reg,
        "password": password,
        "role": role
    })


def sanitize_data(obj):
    if isinstance(obj, dict):
        for key in obj:
            if key == "name":
                obj[key] = "Demo"
            elif key == "regNumber" and obj[key] in reg_map:
                obj[key] = reg_map[obj[key]]
            else:
                sanitize_data(obj[key])

    elif isinstance(obj, list):
        for item in obj:
            sanitize_data(item)


sanitize_data(data["events"])
sanitize_data(data["media"])
sanitize_data(data["notifications"])
sanitize_data(data["messages"])


with open("backend/data.example.json", "w") as f:
    json.dump(data, f, indent=2)

print("Created backend/data.example.json")
