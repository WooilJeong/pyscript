import random
number_input = Element("number_input")
result = Element("result")
def play_game(*args):
    user_guess = number_input.value
    machine_guess = random.randint(1, 50)
    if int(user_guess) == machine_guess:
        result.element.innerText = "일치"
    else:
        result.element.innerText = f"{machine_guess}"
    number_input.clear()