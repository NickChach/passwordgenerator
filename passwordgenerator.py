from random import randint

user_input = input("With your help we are going to create a password you can easily remember.\nEnter a word or phrase: ")

def clean_input():
    cleaned_user_input1 = user_input.title()
    cleaned_user_input2 = cleaned_user_input1.replace(" ", "")
    return cleaned_user_input2

def create_password(clean_input):
    password1 = f"{clean_input}"
    index_special1 = randint(0, len(password1))
    password2 = password1[:index_special1] + "@" + password1[index_special1 + 1:]
    index_special2 = randint(0, len(password2))
    while index_special2 == index_special1:
        index_special2 = randint(0, len(password2))
    password3 = password2[:index_special2] + "/" + password2[index_special2 + 1:]
    number = randint(10, 99)
    password4 = password3 + str(number)
    return password4

print(f"Your password is:\n{create_password(clean_input())}")