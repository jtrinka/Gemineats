import json
from lib.google_model.google_model import GoogleModel

if __name__ == "__main__":
    with open(file="./configs/default.json") as f:
       config = json.load(f)
    GOOGLE_API_KEY = config["GOOGLE_API_KEY"]
    ai_model = GoogleModel(GOOGLE_API_KEY = GOOGLE_API_KEY, model = "gemini-pro")
    prompt = "Can you give me a recipe for General Tso's chicken?"
    ai_model.generate_recipe(prompt = prompt)
    print(ai_model.recipe)
   
