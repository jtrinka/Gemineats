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
        self.prompt = 'You are a recipe recommendation engine whose job it is to give delicious food recipes.'
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
            available_ingredients_string += " The recipe recommendation should also use the following ingredients: " + self.available_ingredients + "."
            return available_ingredients_string
        
    def construct_nonalcoholic_drink_pairing_prompt(self):
        if self.nonalcoholic_drink_pairing is False:
            return ""
        elif self.nonalcoholic_drink_pairing is True and self.construct_allergy_prompt() != "":
            return "Can you recommend a nonalcoholic drink pairing with the recommended meal that adheres to the aforementioned allergy information?"
        elif self.nonalcoholic_drink_pairing is True and self.construct_allergy_prompt() == "":
            return "Can you recommend a nonalcoholic drink pairing with the recommended meal?"
    
    def construct_alcoholic_drink_pairing_prompt(self):
        if self.alcoholic_drink_pairing is False:
            return ""
        elif self.alcoholic_drink_pairing is True and self.construct_allergy_prompt() != "":
            return "In addition to all of that, can you recommend an alcoholic drink pairing with the recommended meal that adheres to the aforementioned allergy information?"
        elif self.alcoholic_drink_pairing is True and self.construct_allergy_prompt() == "":
            return "In addition to all of that, can you recommend an alcoholic drink pairing with the recommended meal?"


    def construct_prompt(self, prompt = ""):
        if self.prompt_choice == "Recommended":
            if self.construct_allergy_prompt() == "":
                total_allergy_prompt = ""
            else:
                total_allergy_prompt = " The recipe recommendation cannot contain " + self.construct_allergy_prompt() + "."
            if self.construct_type_of_food_prompt() == "":
                total_food_prompt = ""
            else:
                total_food_prompt = " The recipe recommendation should have influences from " + self.construct_type_of_food_prompt() + " cuisines."     
            if self.construct_available_ingredients_prompt() == "":
                total_available_ingredients = ""
            else:
                total_available_ingredients = self.construct_available_ingredients_prompt()
            
            self.prompt +=  total_allergy_prompt + total_food_prompt + total_available_ingredients + self.construct_nonalcoholic_drink_pairing_prompt() + self.construct_alcoholic_drink_pairing_prompt()
        elif self.prompt_choice == "Custom":
            self.prompt += prompt
    
if __name__ == "__main__":
    with open(file="./configs/default.json") as f:
       config = json.load(f)

    prompt_data_config = config["prompt_data_config"]
    prompt_data = PromptData()
    prompt_data.set_prompt_data(prompt_data_config=prompt_data_config)
    prompt = Prompt(prompt_data=prompt_data)
    prompt.construct_prompt()
    print(prompt.prompt)