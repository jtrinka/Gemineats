import json
from typing import List

class PromptData:
    def __init__(self):
        self.prompt_choice: str
        self.allergies: List[str]
        self.types_of_food: List[str]
    def set_prompt_data(self, prompt_data_config):
        self.prompt_choice = prompt_data_config["prompt_choice"]
        self.allergies = prompt_data_config["allergies"]
        self.types_of_food = prompt_data_config["types_of_food"]

class Prompt:

    def __init__(self, prompt_data: PromptData):
        self.base_prompt = 'You are a recipe recommendation engine whose job it is to give delicious food recipes.'
        self.prompt_choice = prompt_data.prompt_choice
        if self.prompt_choice == 'Recommended':
            self.allergies = prompt_data.allergies
            self.types_of_food = prompt_data.types_of_food
        self.prompt = None

    def construct_allergy_prompt(self):
        allergy_string = ""
        N_allergies = len(self.allergies)
        if N_allergies == 1:
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
        if N_types == 1:
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

    def construct_prompt(self, prompt = ""):
        if self.prompt_choice == "Recommended":
            self.prompt = self.base_prompt + " The recommendation cannot contain " + self.construct_allergy_prompt() + ". " + \
            "The recommendation should also have influences from " + self.construct_type_of_food_prompt() + " cuisines."
        elif self.prompt_choice == "Custom":
            self.prompt = self.base_prompt+prompt
    
if __name__ == "__main__":
    with open(file="./configs/default.json") as f:
       config = json.load(f)

    prompt_data_config = config["prompt_data_config"]
    prompt_data = PromptData()
    prompt_data.set_prompt_data(prompt_data_config=prompt_data_config)
    prompt = Prompt(prompt_data=prompt_data)
    prompt.construct_prompt()