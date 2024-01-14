import json
from lib.streamlit.streamlit import cs_body, cs_sidebar

if __name__ == "__main__":
    with open(file="./configs/default.json") as f:
       config = json.load(f)

    GOOGLE_API_KEY = config["GOOGLE_API_KEY"]
    cs_sidebar()
    cs_body(GOOGLE_API_KEY=GOOGLE_API_KEY)
   
