import discord
from character import Character
from inventory import Inventory
from spell import Spell


class Game:
    def __init__(self, client):
        self.client = client
        self.characters = {}
        self.inventories = {}
        self.spells = {}

    async def create_character(self, message, user_id):
        """
        To-do:
        - Implement character creation functionality
        - Prompt user for character information (e.g. name, race, class, abilities, etc.)
        - Validate user inputs to ensure they comply with game rules and restrictions
        - Calculate character statistics such as hit points, armor class, and proficiency bonus
        - Store character information in a data structure (e.g. dictionary, JSON object, etc.)
        - Return the character object
        """
        pass

    async def modify_character(self, message, user_id):
        """
        To-do:
        - Implement character modification functionality
        - Prompt user for the character information they wish to modify
        - Validate user inputs to ensure they comply with game rules and restrictions
        - Update the character statistics based on the modified information
        - Return the modified character object
        """
        pass

    async def delete_character(self, message, user_id):
        """
        To-do:
        - Implement character deletion functionality
        - Prompt user for the character they wish to delete
        - Remove the specified character from the characters data structure
        - Return a success/failure message to the user
        """
        pass


async def create_inventory(self, message, user_id):
    """
    To-do:
    - Implement inventory creation functionality
    - Prompt user for inventory information (e.g. name, items, etc.)
    - Validate user inputs to ensure they comply with game rules and restrictions
    - Store inventory information in a data structure (e.g. dictionary, JSON object, etc.)
    - Return the inventory object
    """
    pass


async def modify_inventory(self, message, user_id):
    """
    To-do:
    - Implement inventory modification functionality
    - Prompt user for the inventory information they wish to modify
    - Validate user inputs to ensure they comply with game rules and restrictions
    - Update the inventory items based on the modified information
    - Return the modified inventory object
    """
    pass


async def delete_inventory(self, message, user_id):
    """
    To-do:
    - Implement inventory deletion functionality
    - Prompt user for the inventory they wish to delete
    - Remove the specified inventory from the inventories data structure
    - Return a success/failure message to the user
    """
    pass
async def create_spell(self, message, user_id):
    """
    To-do:
    - Implement spell creation functionality
    - Prompt user for spell information (e.g. name, level, description, etc.)
    - Validate user inputs to ensure they comply with game rules and restrictions
    - Store spell information in a data structure (e.g. dictionary, JSON object, etc.)
    - Return the spell object
    """
    pass

async def modify_spell(self, message, user_id):
    """
    To-do:
    - Implement spell modification functionality
    - Prompt user for the spell information they wish to modify
    - Validate user inputs to ensure they comply with game rules and restrictions
    - Update the spell information based on the modified information
    - Return the modified spell object
    """
    pass

async def delete_spell(self, message, user_id):
    """
    To-do:
    - Implement spell deletion functionality
    - Prompt user for the spell they wish to delete
    - Remove the specified spell from the spells data structure
    - Return a success/failure message to the user
    """
    pass

async def use_spell(self, message, user_id):
    """
    To-do:
    - Implement spell usage functionality
    - Prompt user for the character and spell they wish to use
    - Validate user inputs to ensure they comply with game rules and restrictions
    - Calculate the effects of the spell on the specified character
    - Return the result of the spell usage to the user
    """
    pass

async def show_inventory(self, message, user_id):
    """
    To-do:
    - Implement inventory display functionality
    - Prompt user for the inventory they wish to display
    - Retrieve the specified inventory object
    - Format the inventory information in a user-friendly way
    - Return the formatted inventory information to the user
    """
    pass

async def show_character(self, message, user_id):
    """
    To-do:
    - Implement character display functionality
    - Prompt user for the character they wish to display
    - Retrieve the specified character object
    - Format the character information in a user-friendly way
    - Return the formatted character information to the user
    """
    pass

async def roll_dice(self, message, user_id):
    """
    To-do:
    - Implement dice rolling functionality
    - Prompt user for the type and number of dice to roll
    - Roll the specified dice and calculate the result
    - Return the result of the dice roll to the user
    """
    pass

async def help(self, message, user_id):
    """
    To-do:
    - Implement help functionality
    - Retrieve the list of available commands and their descriptions
    - Format the command information in a user-friendly way
    - Return the formatted command information to the user
    """
    pass
