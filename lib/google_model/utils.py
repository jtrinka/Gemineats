import textwrap
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def load_google_model(GOOGLE_API_KEY, model = 'gemini-pro'):
  genai.configure(api_key=GOOGLE_API_KEY)
  model = genai.GenerativeModel(model)
  return model