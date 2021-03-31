users = [
  { "user_id": 1, "first_name": "Margaret", "last_name": "Chicken" },
  { "user_id": 2, "first_name": "Bill", "last_name": "Gates" },
  { "user_id": 3, "first_name": "Steve", "last_name": "Jobs" },
  { "user_id": 4, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 5, "first_name": "Brendan", "last_name": "Eich" },
]

def find_user(list, user_id):
  user = None
  for user in users:    
    if user["user_id"] == user_id:
        return user["first_name"]

print(find_user(users, 4))

# Is there a way to get last name too?

def find_user(list, user_id):
  user = None
  for user in users:    
    if user["user_id"] == user_id:
        return user["first_name"]["last_name"]

print(find_user(users, 4))