import requests


def delete_user(id):
    reponse = requests.delet(f"{URL}/{id}")
    if reponse.status_code == 204:
        print("User deleted!")
    else:
        print("Error: User was not deleted")


if __name__ == "__main__":
    print("DELETE USER")
    print("-" * 20)

    id = input("User id: ")
    if not id:
        print("Error, please provide an id")

    delete_user(id)
