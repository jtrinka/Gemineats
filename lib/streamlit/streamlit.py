import streamlit as st
from pathlib import Path
import base64
from lib.google_model.google_model import GoogleModel
from lib.google_model.prompt import PromptData, Prompt

LEGAL_DISCLAIMER = "LEGAL DISCLAIMER: The creator of Gemineats and creator(s) of services leveraged by Gemineats are not responsible for any harm caused to users of Gemineats who leverage, in-part or in-full, any form of the recipe recommendations that are offered by the Gemineats app. Users are advised to always double check the recipe recommendations of Gemineats prior to leveraging the recommendation, in-part or in-full; especially if the user has allergies or can experience any other harmful effect from ingesting food or drink. In addition, by using the alcoholic drink recommendation feature, the user confirms that they are 21 years of age or older and any recommended alcoholic drink that is made, in-part or in-full, is to be prepared for and consumed only by adults of age 21 years or older."

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
        allergies = st.sidebar.multiselect(label = "Select all relevant allergies (if any)", options = ["None", "Tree Nuts", "Peanuts", "Crustecean Shellfish", "Fish", "Gluten", "Wheat", "Soy", "Soybeans", "Dairy", "Honey", "Sesame"])
        if "None" in allergies:
            allergies = None
        types_of_food = st.sidebar.multiselect(label = "Select all styles of food (if any)", options = ["None","American", "Chinese", "Mexican", "Spanish", "Italian", "French", "Japanese", "Thai", "German", "Scandinavian", "Polish", "Ethiopian", "Nigerian", "South African", "Egyptian"])
        if "None" in types_of_food:
            types_of_food = None
        available_ingredients = st.sidebar.text_input(label = "Optional: List all or some of your available ingredients separated by a comma and space (ex: Beans, Tomatoes, Celery)")
        if available_ingredients == "None":
            available_ingredients = None
        nonalcoholic_drink_pairing = st.sidebar.toggle(label = "Request a nonalcoholic drink pairing")
        alcoholic_drink_pairing = st.sidebar.toggle(label = "Request an alcoholic drink pairing (by selecting this option, the user confirms that they are 21 years of age or older)")
        generate_recipe_bool = st.sidebar.button("Generate Recipe")
        prompt_data_config = {
            "prompt_choice": "Recommended",
            "allergies": allergies,
            "types_of_food": types_of_food,
            "available_ingredients": available_ingredients,
            "nonalcoholic_drink_pairing": nonalcoholic_drink_pairing,
            "alcoholic_drink_pairing": alcoholic_drink_pairing
        }
    elif prompt_choice == "Custom":
        generate_recipe_bool = False
        prompt_data_config = {
            "prompt_choice": "Custom",
            "allergies": None,
            "types_of_food": None,
            "available_ingredients": None,
            "nonalcoholic_drink_pairing": False,
            "alcoholic_drink_pairing": False
        }
    creator_information = st.sidebar.toggle(label = "Show Gemineats Creator Information")
    if creator_information is True:
        url = "https://github.com/jtrinka"
        st.sidebar.markdown("Dr. Jordan Christopher Trinka, Ph.D. is a data scientist with a background in applied statistics and machine/deep learning. Dr. Trinka created Gemineats to offer a quick and tasty solution to the problem of finding the perfect recipe. When not developing new and exciting technologies, he enjoys cooking, hiking, and fishing with his wife. His personal GitHub can be found at [https://github.com/jtrinka](%s)" % url)
    st.sidebar.text(LEGAL_DISCLAIMER)
    return prompt_data_config, generate_recipe_bool

def cs_body(GOOGLE_API_KEY, prompt_data_config, generate_recipe_bool = False):

    col1, = st.columns(1)
   
    prompt_data = PromptData()
    prompt_data.set_prompt_data(prompt_data_config=prompt_data_config)
    prompt = Prompt(prompt_data=prompt_data)
    st.session_state.messages = []
    if prompt_data.prompt_choice == "Recommended":
        if generate_recipe_bool is True:
            def recommended_prompt():
                try:
                    ai_model = GoogleModel(GOOGLE_API_KEY = GOOGLE_API_KEY, model = "gemini-pro")
                    prompt.construct_prompt()
                    ai_model.generate_recipe(prompt = prompt)
                    message_placeholder = st.empty()
                    message_placeholder.markdown("The Gemineats recipe recommendation is as follows: \n \n" + ai_model.recipe + "▌")
                    message_placeholder.markdown("The Gemineats recipe recommendation is as follows: \n \n" + ai_model.recipe)
                    st.session_state.messages.append({"role": "assistant", "content": ai_model.recipe})
                    st.download_button("Save Recipe", file_name="gemineats_recipe_recommendation.txt", data = "The Gemineats recipe recommendation is as follows: \n \n" + ai_model.recipe  + "\n \n" + LEGAL_DISCLAIMER)
                except:
                    recommended_prompt()
            recommended_prompt()
    elif prompt_data.prompt_choice == "Custom":
        # Display text
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if custom_prompt := st.chat_input("What are you hungry for?"):
            prompt.construct_prompt(prompt=custom_prompt)
            st.session_state.messages.append({"role": "user", "content": custom_prompt})
            with st.chat_message("user"):
                st.markdown(custom_prompt)

            with st.chat_message("assistant"):
                def recommended_prompt():
                    try:
                        message_placeholder = st.empty()
                        ai_model = GoogleModel(GOOGLE_API_KEY = GOOGLE_API_KEY, model = "gemini-pro")
                        ai_model.generate_recipe(prompt = prompt)
                        message_placeholder.markdown("The Gemineats recipe recommendation is as follows: \n \n" + ai_model.recipe  + "▌")
                        message_placeholder.markdown("The Gemineats recipe recommendation is as follows: \n \n" + ai_model.recipe)
                        st.session_state.messages.append({"role": "assistant", "content": ai_model.recipe})
                        st.download_button("Save Recipe", file_name="gemineats_recipe_recommendation.txt",data = "The Gemineats recipe recommendation is as follows: \n \n" + ai_model.recipe  + "\n \n" + LEGAL_DISCLAIMER)
                    except:
                        recommended_prompt()
            recommended_prompt()
            
    return None

