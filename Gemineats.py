import json
from lib.streamlit.streamlit import cs_body, cs_sidebar
import streamlit as st

if __name__ == "__main__":
    prompt_data_config, generate_recipe_bool=cs_sidebar()
    cs_body(prompt_data_config=prompt_data_config,
            generate_recipe_bool=generate_recipe_bool)
   
