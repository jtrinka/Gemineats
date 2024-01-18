import streamlit as st
from pathlib import Path
import base64
from lib.google_model.google_model import GoogleModel
from lib.google_model.prompt import PromptData, Prompt


st.set_page_config(
     page_title='Gemineats',
     layout="wide",
     initial_sidebar_state="expanded",
)


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def cs_sidebar():

    st.sidebar.markdown('''<img src='data:image/jpeg;base64,{}' class='img-fluid' width=256 height=256>'''.format(img_to_bytes("robot_cooking_stock_photo.jpeg")), unsafe_allow_html=True)
    st.sidebar.header('Gemineats')

    st.sidebar.markdown('''
<small>Welcome to Gemineats! This app leverages Google's Gemini-pro large language multimodal AI model, custom prompt engineering, and streamlit to offer delicious, unique, and fun recipes sure to wow family and guests.</small>
    ''', unsafe_allow_html=True)
    prompt_choice = st.sidebar.radio("Choose a prompt style:", ["Recommended", "Custom"])
    if prompt_choice == "Recommended":
        allergies = st.sidebar.multiselect(label = "Select all relevant allergies (if any)", options = ["None", "Nuts", "Fruits", "Gluten", "Soy", "Dairy", "Honey"])
        if "None" in allergies:
            allergies = None
        types_of_food = st.sidebar.multiselect(label = "Select all styles of food (if any)", options = ["None","American", "Chinese", "Mexican", "Italian", "French", "Japanese", "Thai"])
        if "None" in types_of_food:
            types_of_food = None
        available_ingredients = st.sidebar.text_input(label = "Optional: List your available ingredients separated by a comma and space (ex: Beans, Tomatoes, Celery)")
        if available_ingredients == "None":
            available_ingredients = None
        drink_pairing = st.sidebar.toggle(label = "Request an alcoholic drink pairing")
        generate_recipe_bool = st.sidebar.button("Generate Recipe")
        prompt_data_config = {
            "prompt_choice": "Recommended",
            "allergies": allergies,
            "types_of_food": types_of_food,
            "available_ingredients": available_ingredients,
            "drink_pairing": drink_pairing
        }
    elif prompt_choice == "Custom":
        generate_recipe_bool = False
        prompt_data_config = {
            "prompt_choice": "Custom",
            "allergies": None,
            "types_of_food": None,
            "available_ingredients": None,
            "drink_pairing": False
        }
    return prompt_data_config, generate_recipe_bool

def cs_body(GOOGLE_API_KEY, prompt_data_config, generate_recipe_bool = False):

    col1, = st.columns(1)

   
    prompt_data = PromptData()
    prompt_data.set_prompt_data(prompt_data_config=prompt_data_config)
    prompt = Prompt(prompt_data=prompt_data)
    ai_model = GoogleModel(GOOGLE_API_KEY = GOOGLE_API_KEY, model = "gemini-pro")
    st.session_state.messages = []
    legal_disclaimer = "\n LEGAL DISCLAIMER: The creator(s) of Gemineats and creator(s) of services leveraged by Gemineats are not responsible \
        for any harm caused to users of Gemineats who leverage, in-part or in-full, any form of the recipe recommendations that are offered by the Gemineats app. \
            Users are advised to always double check the recipe recommendations of Gemineats prior to leveraging the recommendation, in-part or in-full; especially if the user has allergies. \
                In addition, by using the drink recommendation feature, the user confirms that they are 21 years of age or older and any recommended alcoholic drink that is made, in-part or in-full, is to be prepared for adults of age 21 years or older."
    
    if prompt_data.prompt_choice == "Recommended":
        if generate_recipe_bool is True:
            prompt.construct_prompt()
            ai_model.generate_recipe(prompt = prompt)
            message_placeholder = st.empty()
            message_placeholder.markdown(ai_model.recipe  + "\n" + legal_disclaimer + "▌")
            message_placeholder.markdown(ai_model.recipe  + "\n" + legal_disclaimer)
            st.session_state.messages.append({"role": "assistant", "content": ai_model.recipe})
            st.download_button("Save Recipe", data = ai_model.recipe  + "\n" + legal_disclaimer)
    elif prompt_data.prompt_choice == "Custom":
        # Display text
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if custom_prompt := st.chat_input("What are you hungry for?"):
            generate_recipe_bool = True
            prompt.construct_prompt(prompt=custom_prompt)
            st.session_state.messages.append({"role": "user", "content": custom_prompt})
            with st.chat_message("user"):
                st.markdown(custom_prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                ai_model.generate_recipe(prompt = prompt)
                message_placeholder.markdown(ai_model.recipe  + "\n" + legal_disclaimer + "▌")
                message_placeholder.markdown(ai_model.recipe  + "\n" + legal_disclaimer)
            st.session_state.messages.append({"role": "assistant", "content": ai_model.recipe})
            
            st.download_button("Save Recipe", data = ai_model.recipe  + "\n" + legal_disclaimer)
    if generate_recipe_bool is False:
        st.markdown(legal_disclaimer, unsafe_allow_html=True)


    return None

