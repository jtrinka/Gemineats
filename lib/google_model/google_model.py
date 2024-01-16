from lib.google_model.utils import load_google_model
from lib.google_model.prompt import Prompt

class GoogleModel:
    def __init__(self, GOOGLE_API_KEY: str, model: str):
        self.model = load_google_model(GOOGLE_API_KEY = GOOGLE_API_KEY, model = model)
    def generate_recipe(self, prompt: Prompt):
        self.recipe = self.model.generate_content(prompt.prompt).text

