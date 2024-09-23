users = [
    {"name": "Kamil", "country": "Poland"},
    {"name": "John", "country": "USA"},
    {"name": "Yeti"}
]

polish_users = [{"name": user["name"]} for user in users if user.get("country") == "Poland"]

print(polish_users)