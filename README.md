# Gemineats

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemineats.streamlit.app/)

Gemineats is a user-friendly app that leverages custom prompt engineering, Google's Gemini-pro large language multimodal AI model, and streamlit to offer delicious, unique, and fun recipes sure to wow family and guests. This repository contains the software that is used for prompt engineering, standing up the Google API, and defining the streamlit app. The app is hosted [here](https://gemineats.streamlit.app/).

## Core Features

The base prompt that is leveraged in Gemineats specifies that the Gemini-pro model is to act as a meal recommendation engine and should return an answer in a template form. The app then offers the following two types of prompting that accompany the base prompt:

    1. Recommended Prompt - Leverages user selections and under-the-hood prompt engineering to make a meal recommendation
    2. Custom Prompt - Leverages exact user input with the base prompt in the meal recommendation

### Recommended Prompt Features

The recommended prompt feature offers the following options to the user:

    * Relevant Allergies - Causes Gemineats to make a meal recommendation that avoids the specified food allergies
    * Food Styles - Causes Gemineats to make a meal recommendation that leverages certain styles of food
    * List of Available Ingredients - Causes Gemineats to make a meal recommendation that leverages specified ingredients
    * Requesting a Nonalcoholic Drink Pairing - Causes Gemineats to make a meal recommendation that includes a nonalcoholic drink pairing that goes with the food
    * Requesting an Alcoholic Drink Pairing - Causes Gemineats to make a meal recommendation that includes an alcoholic drink pairing that goes with the food

### Custom Prompt Features

The custom prompt feature simply leverages the base prompt and the user input to make a meal recommendation.

## Installation Instructions

To install and launch the Gemineats app on your local area network, first follow steps:&nbsp;
    1. Create a [Google account](https://www.google.com/)
    2. Obtain a [Google API key](https://developers.google.com/maps/documentation/embed/get-api-key)
    3. Install the [Google SDK](https://cloud.google.com/sdk)
    4. Install [miniconda](https://docs.anaconda.com/free/miniconda/)

Then execute the following commands in a terminal from your directory of choice.

```bash
git clone https://github.com/jtrinka/Gemineats.git
cd gemineats
conda create -n gemineats python=3.9
conda activate gemineats
pip install -r requirements.txt
```

Then add your Google API key to the ```secrets.toml``` and ```default.json``` files found in ```.streamlit```. From here, you can run the service in the terminal by leveraging ```main.py``` or you can launch the app on your local area network by running ```streamlit run Gemineats.py```. 


#### Legal Disclaimer
The creator of Gemineats and creator(s) of services leveraged by Gemineats are not responsible for any harm caused to users of Gemineats who leverage, in-part or in-full, any form of the meal recommendations that are offered by the Gemineats app. Users are advised to always double check the meal recommendations of Gemineats prior to leveraging the recommendation, in-part or in-full; especially if the user has allergies or can experience any other harmful effect from ingesting food or drink. In addition, by using the alcoholic drink pairing recommendation feature, or requesting an alcoholic drink by itself or as a pairing in the custom prompt feature, the user confirms that they are 21 years of age or older and any recommended alcoholic drink that is made, in-part or in-full, is to be prepared for and consumed only by adults of age 21 years or older.

Copyright © 2023 Jordan Christopher Trinka. All Rights Reserved.