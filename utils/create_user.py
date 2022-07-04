import requests

URL = "http://127.0.0.1:500/"

def create_user(first, last, hobbies):
    user_data = {
        "first_name" : first,
        "last_name" : last, 
        "hobbies" : hobbies
    }

    response = request.post(URL, json=user_data)
    if response.status_code == 204:
        print("User successfully created.")
    else:
        print("Error: User was not created.")

if __name__ == "__main__":
    print("CREATE USER")
    print("-" * 20)
    first = input("First name: ")
    last = input("Last name: ")
    hobbies = input("Hobbies: ")

    create_user(first, last, hobbies)