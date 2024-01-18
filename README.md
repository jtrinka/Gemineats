# Gemineats

Gemineats is a user-friendly app that leverages Google's Gemini-pro large language multimodal AI model, custom prompt engineering, and streamlit to offer delicious, unique, and fun recipes sure to wow family and guests. This repository contains the software that is used for prompt engineering, standing up the Google API, and defining the streamlit app. The app is hosted at (insert the link here when deployed throught streamlit)

# Summary

The app begins with prompt engineering to prepare the Gemini-pro model to act as a recipe recommendation engine. After theis small bit of prompt engineering, the prompt can be specified further using two core features:

    1. Recommended Prompt - Leverages user inputs and further prompt engineering to make a recipe recommendations
    2. Custom Prompt - Leverages exact user input in the recipe recommendation

Once the prompt is formed, the Gemini-pro model ingests the whole prompt and returns a recipe recommendation.

# Updates

    - The app has been updated with a recommended prompt feature that constructs a good input prompt for the user which leverages user allergy information, types of cuisine the user desires, available ingredients, and whether or not the user requests an alcoholic drink pairing
    - The app has been updated with a custom prompt feature that leverages minimal prompt engineering (prepending user input to prepare the model to act as a recipe recommendation engine)
    - The app leverages streamlit to deliver the experience in a user-friendly fashion

# Installation Instructions

To launch the app on your computer and local area network you will need to first download and install Anaconda and miniconda. Then in a bash shell or Anaconda interpreter, you should run `conda create -n gemineats python=3.9` After you create the environment with python version 3.9.x, you need to activate it and install the dependencies using `pip install -r requirements.txt`. You'll also need to obtain a google API key and install the Google SDK to leverage the Gemini-pro model. Once all dependencies are installed and the Google API key is leveraged in the `default.json` config, you can run `streamlit run Gemineats.py` to launch the app.

# Legal Disclaimer

The creator(s) of Gemineats and creator(s) of services leveraged by Gemineats are not responsible
for any harm caused to users of Gemineats who leverage, in-part or in-full, any form of the recipe recommendations that are offered by the Gemineats app. Users are advised to always double check the recipe recommendations of Gemineats prior to leveraging the recommendation, in-part or in-full; especially if the user has allergies or can experience any other harmful effect from ingesting food or drink. In addition, by using the drink recommendation feature, the user confirms that they are 21 years of age or older and any recommended alcoholic drink that is made, in-part or in-full, is to be prepared for adults of age 21 years or older.