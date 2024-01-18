import json
from lib.streamlit.streamlit import cs_body, cs_sidebar
import streamlit as st

if __name__ == "__main__":
    with open(file="./configs/default.json") as f:
       config = json.load(f)

    prompt_data_config = config["prompt_data_config"]
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    prompt_data_config, generate_recipe_bool=cs_sidebar()
    cs_body(GOOGLE_API_KEY=GOOGLE_API_KEY, 
            prompt_data_config=prompt_data_config,
            generate_recipe_bool=generate_recipe_bool)
   
