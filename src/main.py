class Character:
    ...

class Location:
    ...

class Item:
    ...


def main():
    command = input("Please enter a command").split(' ')

    if (command[0] == "help"):
        print("commands available are: where, inventory, goto...")
    elif (command[0] == "inventory"):
        ...
    elif (command[0] == "goto"):
        # if (command[1] is a real location):
        ...

    # a terminal text game. rpg, role playing game
    # like skyrim or fallout or the witcher

    # you can type in commands like
    # >where # tell the player what location he is in
    # >inventory # tell the player what items he owns
    # >goto <somelocation> # teleport the player to a new location
    # >attack <person> <weapon> # attack a person near you with a weapon
    # >drop <item> # drop your item from your inventory
    # >pickup <item> # add item to your inventory


main()