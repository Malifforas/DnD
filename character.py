import
class Character:
    def __init__(self):
        pass

    def create_character(self):
        """
        Prompts the user for character information and validates inputs to ensure they comply with game rules and restrictions.
        Calculates character statistics such as hit points, armor class, and proficiency bonus.
        Stores character information in a data structure.
        Returns the character object.
        """

    def modify_character(self):
        """
        Prompts the user for the character information they wish to modify.
        Validates user inputs to ensure they comply with game rules and restrictions.
        Updates the character statistics based on the modified information.
        Returns the modified character object.
        """

    def get_character(self):
        """
        Prompts the user for the character information they wish to retrieve.
        Returns the requested character information.
        """

    def _validate_inputs(self, inputs):
        """
        Implements validation logic for character inputs.
        Returns True if inputs are valid, False otherwise.
        """

    def _calculate_statistics(self, character):
        """
        Implements logic for calculating character statistics such as hit points, armor class, and proficiency bonus.
        Updates the character object with the calculated statistics.
        """

    def _roll_dice(self, num_dice, num_sides):
        """
        Rolls a specified number of dice with a specified number of sides.
        Returns the sum of the rolls.
        """

    def _generate_ability_scores(self):
        """
        Generates ability scores for a new character through dice rolling.
        Returns the ability scores.
        """

    def _get_modifier(self, score):
        """
        Calculates the modifier for an ability score.
        Returns the modifier.
        """

    def _get_race_info(self, race):
        """
        Uses an external API to retrieve information about the specified race.
        Parses the API response and returns relevant information (e.g. ability score bonuses, size, speed, etc.).
        """

    def _get_class_info(self, class_name):
        """
        Uses an external API to retrieve information about the specified class.
        Parses the API response and returns relevant information (e.g. hit dice, proficiencies, spellcasting ability, etc.).
        """

    def _get_spell_info(self, spell_name):
        """
        Uses an external API to retrieve information about the specified spell.
        Parses the API response and returns relevant information (e.g. casting time, range, components, description, etc.).
        """

    def _get_ability_info(self, ability_name):
        """
        Uses an external API to retrieve information about the specified ability.
        Parses the API response and returns relevant information (e.g. description, effect, etc.).
        """
