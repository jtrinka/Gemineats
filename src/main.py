import json
from lib.google_model.google_model import GoogleModel
from lib.google_model.prompt import PromptData, Prompt

if __name__ == "__main__":
    with open(file="./configs/default.json") as f:
       config = json.load(f)

    prompt_data_config = config["prompt_data_config"]
    prompt_data = PromptData()
    prompt_data.set_prompt_data(prompt_data_config=prompt_data_config)
    prompt = Prompt(prompt_data=prompt_data)
    prompt.construct_prompt()
    GOOGLE_API_KEY = config["GOOGLE_API_KEY"]
    ai_model = GoogleModel(GOOGLE_API_KEY = GOOGLE_API_KEY, model = "gemini-pro")
    ai_model.generate_recipe(prompt = prompt)
    print(ai_model.recipe)
   
