from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from app import create_app
config_name = "development"
app = create_app(config_name)
