import io
import json

# try:                            # blok koda koji može prouzročiti error
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["fnjn"])
# except FileNotFoundError:       # ono što se izvršava ako try blok prouzrokuje error
#     file = open("a_file.txt", "w")
#     file.write("Something.")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist.")
# else:                           # ono što se izvršava ako try blok uspije
#     content = file.read()
#     print(content)
# finally:                        # ono što se izvršava bez obzira na ishod
#     file.close()
#     print("File closed.")



# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")



# fruits = ["Apple", "Pear", "Orange"]
# TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("There is no such fruit.")
#     else:
#         print(fruit + " pie")
# make_pie(4)



# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
# print(total_likes)


new_data_dict = {
    "Google": {
        "E-mail/Username": "martin.petracic@gmail.com",
        "Password": "Bn6_082792"
    }
}

# data_file = open("data.json", "r")

try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        data.update(new_data_dict)
    with open("data.json", "w") as data_file:
        json.dump(data, data_file)
    print("try executed")
except FileNotFoundError:
    with open("data.json", "w") as data_file:
        json.dump(new_data_dict, data_file)
    print("except executed")

