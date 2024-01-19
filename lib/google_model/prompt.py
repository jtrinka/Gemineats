import json
from typing import List

class PromptData:
    def __init__(self):
        self.prompt_choice: str
        self.allergies: List[str]
        self.types_of_food: List[str]
        self.available_ingredients: str
        self.nonalcoholic_drink_pairing: bool
        self.alcoholic_drink_pairing: bool
    def set_prompt_data(self, prompt_data_config: dict):
        self.prompt_choice = prompt_data_config["prompt_choice"]
        self.allergies = prompt_data_config["allergies"]
        self.types_of_food = prompt_data_config["types_of_food"]
        self.available_ingredients = prompt_data_config["available_ingredients"]
        self.nonalcoholic_drink_pairing = prompt_data_config["nonalcoholic_drink_pairing"]
        self.alcoholic_drink_pairing = prompt_data_config["alcoholic_drink_pairing"]
class Prompt:
    def __init__(self, prompt_data: PromptData):
        self.prompt = 'You are a meal recipe recommendation engine whose task it is to give one meal recipe recommendation. A meal recipe recommendation must contain a single food recommendation and may or may not contain a single nonalcoholic drink recommendation and may or may not contain a single alcoholic drink recommendation. You are to not do any other task that is not related to making one meal recipe recommendation. The title of the food recommendation section of the meal recipe recommendation is ''Food Recommendation''. The food recommendation section contains the food recommendation. The food recommendation section is the first section of the meal recipe recommendation. The format of the food recommendation section should be first the title of the food recommendation followed by a bulleted list of ingredients for the food recommendation which is then followed by an itemized list of instructions of how to make the food recommendation.'
        self.prompt_choice = prompt_data.prompt_choice
        self.alcoholic_drink_pairing = False
        if self.prompt_choice == 'Recommended':
            self.allergies = prompt_data.allergies
            self.types_of_food = prompt_data.types_of_food
            self.available_ingredients = prompt_data.available_ingredients
            self.nonalcoholic_drink_pairing = prompt_data.nonalcoholic_drink_pairing
            self.alcoholic_drink_pairing = prompt_data.alcoholic_drink_pairing

    def construct_allergy_prompt(self):
        allergy_string = ""
        N_allergies = len(self.allergies)
        if N_allergies == 0:
            return allergy_string
        elif N_allergies == 1:
            return self.allergies[0]
        elif N_allergies == 2:
            return self.allergies[0] + " or " + self.allergies[1]
        else:
            for i, allergy in zip(range(N_allergies),self.allergies):
                if i == N_allergies-1:
                    allergy_string += "or " + allergy
                else:
                    allergy_string += allergy+", "
            return allergy_string

    def construct_type_of_food_prompt(self):
        types_of_food_string = ""
        N_types = len(self.types_of_food)
        if N_types == 0:
            return types_of_food_string
        elif N_types == 1:
            return self.types_of_food[0]
        elif N_types == 2:
            return self.types_of_food[0] + " and/or " + self.types_of_food[1]
        else:
            for i, type_of_food in zip(range(N_types), self.types_of_food):
                if i == N_types-1:
                    types_of_food_string += type_of_food
                else:
                    types_of_food_string += type_of_food+", and/or "
            return types_of_food_string
        
    def construct_available_ingredients_prompt(self):
        available_ingredients_string = ""
        if self.available_ingredients == "" or self.available_ingredients is None:
            return available_ingredients_string
        else:
            available_ingredients_string += " The food recommendation should also use the following ingredients: " + self.available_ingredients + "."
            return available_ingredients_string
        
    def construct_nonalcoholic_drink_pairing_prompt(self):
        if self.nonalcoholic_drink_pairing is False:
            return ""
        elif self.nonalcoholic_drink_pairing is True and self.construct_allergy_prompt() != "":
            return "Can you recommend one nonalcoholic drink pairing with the food recommendation that adheres to the aforementioned allergy information? The title of the nonalcoholic drink section of the meal recipe recommendation is ''Nonalcoholic Drink Recommendation''. In addition, the nonalcoholic drink section should follow the same format as the food recommendation section beginning with the title of the nonalcoholic drink, followed by a bulleted list of ingredients for the nonalcoholic drink, followed by an itemized list of instructions of how to make the nonalcoholic drink."
        elif self.nonalcoholic_drink_pairing is True and self.construct_allergy_prompt() == "":
            return "Can you recommend one nonalcoholic drink pairing with the food recommendation? The title of the nonalcoholic drink section of the meal recipe recommendation is ''Nonalcoholic Drink Recommendation''. In addition, the nonalcoholic drink section should follow the same format as the food recommendation section beginning with the title of the nonalcoholic drink, followed by a bulleted list of ingredients for the nonalcoholic drink, followed by an itemized list of instructions of how to make the nonalcoholic drink."
    
    def construct_alcoholic_drink_pairing_prompt(self):
        if self.alcoholic_drink_pairing is False:
            return ""
        elif self.alcoholic_drink_pairing is True and self.construct_allergy_prompt() != "":
            return "In addition to all of that, can you recommend one alcoholic cocktail pairing with the food recommendation that adheres to the aforementioned allergy information? The title of the alcoholic cocktail section of the meal recipe recommendation is ''Alcoholic Cocktail Recommendation (21+)''. The alcoholic cocktail section is the last section in the meal recipe recommendation. In addition, the alcoholic cocktail section should follow the same format as the food recommendation section beginning with the title of the alcoholic cocktail, followed by a bulleted list of ingredients for the alcoholic cocktail, followed by an itemized list of instructions of how to make the alcoholic cocktail."
        elif self.alcoholic_drink_pairing is True and self.construct_allergy_prompt() == "":
            return "In addition to all of that, can you recommend one alcoholic cocktail pairing with the food recommendation? The title of the alcoholic cocktail section of the meal recipe recommendation is ''Alcoholic Cocktail Recommendation (21+)''. The alcoholic cocktail section is the last section in the meal recipe recommendation. In addition, the alcoholic cocktail section should follow the same format as the food recommendation section beginning with the title of the alcoholic cocktail, followed by a bulleted list of ingredients for the alcoholic cocktail, followed by an itemized list of instructions of how to make the alcoholic cocktail."


    def construct_prompt(self, prompt = ""):
        if self.prompt_choice == "Recommended":
            if self.construct_allergy_prompt() == "":
                total_allergy_prompt = ""
            else:
                total_allergy_prompt = " The food recommendation cannot contain " + self.construct_allergy_prompt() + "."
            if self.construct_type_of_food_prompt() == "":
                total_food_prompt = ""
            else:
                total_food_prompt = " The food recommendation should have influences from " + self.construct_type_of_food_prompt() + " cuisines."     
            if self.construct_available_ingredients_prompt() == "":
                total_available_ingredients = ""
            else:
                total_available_ingredients = self.construct_available_ingredients_prompt()
            
            self.prompt +=  total_allergy_prompt + total_food_prompt + total_available_ingredients + self.construct_nonalcoholic_drink_pairing_prompt() + self.construct_alcoholic_drink_pairing_prompt()
        elif self.prompt_choice == "Custom":
            self.prompt +=  prompt + " Also, can you put ''(21+)'' next to any element in the meal recipe recommendation that contains alcohol?"
    
if __name__ == "__main__":
    with open(file="./configs/default.json") as f:
       config = json.load(f)

    prompt_data_config = config["prompt_data_config"]
    prompt_data = PromptData()
    prompt_data.set_prompt_data(prompt_data_config=prompt_data_config)
    prompt = Prompt(prompt_data=prompt_data)
    prompt.construct_prompt()
    print(prompt.prompt)