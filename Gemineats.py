from lib.streamlit.streamlit import cs_body, cs_sidebar
import streamlit as st

if __name__ == "__main__":
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    prompt_data_config, generate_recipe_bool=cs_sidebar()
    cs_body(GOOGLE_API_KEY=GOOGLE_API_KEY, 
            prompt_data_config=prompt_data_config,
            generate_recipe_bool=generate_recipe_bool)
   
