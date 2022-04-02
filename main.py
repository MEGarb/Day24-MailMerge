
with open("./Input/Letters/starting_letter.txt") as file:
    text = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()


for name in names:
    s_name = name.strip()
    with open(f"./Output/ReadyToSend/letter_for_{s_name}.txt", 'w') as file:
        temp = text.replace("[name]", s_name)
        file.write(temp)


