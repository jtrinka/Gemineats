from lib.google_model.utils import load_google_model

class GoogleModel:
    def __init__(self, GOOGLE_API_KEY: str, model: str):
        self.model = load_google_model(GOOGLE_API_KEY = GOOGLE_API_KEY, model = model)
        self.base_prompt = "You are a recipe recommendation engine whose job it is to give delicious food recipes."
    def generate_recipe(self, prompt: str):
        self.recipe = self.model.generate_content(self.base_prompt + " " + prompt).text
    def set_base_prompt(self, prompt: str):
        self.base_prompt = prompt

