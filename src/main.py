from __future__ import annotations
from typing import Literal


class Location:
    name: str 
    connections: list[Location]
    items: list[Item]
    characters: list[Character]

    def __init__(self, name: str, connections: list[Location] = [], items: list[Item] = [], characters: list[Character] = []):
        self.name = name
        self.connections = connections
        self.items = items
        self.characters = characters

    def connect(self, other: Location, bidirectional: bool = True):
        self.connections.append(other)
        if bidirectional:
            other.connections.append(self)

class Item:
    name: str
    rarity: Literal['Common', 'Uncommon', 'Rare', 'Legendary']
    worth: float

class Character:
    name: str
    health: float
    inventory: list[Item]
    location: Location | None

    def __init__(self, name: str, health: float, inventory: list[Item] = [], location: Location | None = None):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.location = location

def gameloop(player: Character) -> None:
    command = input("Please enter a command\n>").split(' ')
    if (command[0] == "help"):
        print("commands available are: where, inventory, goto...")
    elif (command[0] == "where"):
        if (player.location == None):
            print("You are nowhere!"); return gameloop(player)
        print("You are at:")
        print(player.location.name)
        print("You may travel to:")
        for connection in player.location.connections:
            print(connection.name) 
    elif (command[0] == "goto"): # "goto roomB"
        if (player.location == None):
            print("You are nowhere!"); return gameloop(player)
        for connection in player.location.connections:
            if(command[1] == connection.name):
                player.location = connection
                print("You went:")
                print(connection.name); return gameloop(player)
        print("You can't goto:")
        print(command[1] + " was not found near your current location!")
    elif (command[0] == "inv"): # "inv" (shows inventory items)
        print("your items are:")
        ...
    elif (command[0] == "pickup"): # "pickup sword" (pickups item if found in location)
        ...
    elif (command[0] == "drop"): # "drop sword" (drops item from inventory, into location you are standing in)
        ...
        # probably a smart idea to make pickup and drop methods on the character clas.

    gameloop(player)


def main():

    roomA = Location("RoomA")
    roomB = Location("RoomB")
    roomA.connect(roomB)

    player = Character("player", 100, [], roomA)
    characterB = Character("B", 50, [], roomB)

    gameloop(player)

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