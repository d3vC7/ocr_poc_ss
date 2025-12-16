import os
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv() # Load the API key from a .env file

# Configure the client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Open the image file
img = Image.open("bono_rayen.png")
#img = Image.open("boleta1.png")
#img = Image.open("escrito_a_mano.png")


# Define the prompt
prompt = "Extract all text from this image and return it as plain text."

# Call the Gemini API for vision tasks
response = client.models.generate_content(
    model="gemini-2.5-flash", # Use a model optimized for speed and document processing
    contents=[prompt, img]
)

print(response.text)
