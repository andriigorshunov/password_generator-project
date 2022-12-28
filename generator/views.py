import random

from django.shortcuts import render, redirect, reverse

LOWER_CASE_LETTERS = list('abcdefghijklopqrstuvwxyz')
UPPER_CASE_LETTERS = list('ABCDEFGHIJKLOPQRSTUVWXYZ')
NUMBERS = list("1234567890")
SPECIAL_CHARACTERS = list("!@#$%^&*()_-+=")


def home(request):
    # pass_length, has_upper_case, has_numbers, has_special_characters = None, None, None, None
    if request.method == "POST":

        pass_length = int(request.POST.get('length'))
        has_upper_case = request.POST.get('upper_case', 'off')  # on or off
        has_numbers = request.POST.get('numbers', 'off')
        has_special_characters = request.POST.get("special_characters", 'off')
        print("---------------------------------")
        print(
            f"Pass length: {pass_length}, UpperCase: {has_upper_case}, Numbers: {has_numbers}, Special Characters: {has_special_characters}")
        print(type(has_upper_case), type(has_numbers), type(has_special_characters))
        print("---------------------------------")
        password = generate_pass(pass_length, has_upper_case, has_numbers, has_special_characters)

        return render(request, "generator/home.html", {"password": password})
    else:
        return render(request, "generator/home.html")


def generate_pass(length, has_upper_case, has_numbers, has_special_characters):
    password_characters_list = list()
    password_characters_list += LOWER_CASE_LETTERS
    password = ""
    if str(has_upper_case) == "on":
        password_characters_list += UPPER_CASE_LETTERS
    else:
        pass

    if str(has_numbers) == "on":
        password_characters_list += NUMBERS
    else:
        pass

    if str(has_special_characters) == "on":
        password_characters_list += SPECIAL_CHARACTERS
    else:
        pass

    print(f"Password list final {password_characters_list}")
    for _ in range(length):
        password += str(random.choice(password_characters_list))
    return password
