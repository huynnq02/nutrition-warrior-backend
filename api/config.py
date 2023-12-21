from dotenv import load_dotenv
import os
from mongoengine import connect
import cloudinary

load_dotenv()

db_name = "nutritionwarrior"

# Define the default connection
connect(
    db=db_name,
    host=os.getenv("MONGO_URL"),
)

# Setup cloudinary
cloudinary.config( 
  cloud_name = os.getenv("CLOUD_NAME"), 
  api_key = os.getenv("API_KEY"), 
  api_secret = os.getenv("API_SECRET"), 
)