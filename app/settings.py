import pathlib
import yaml
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / "config" / "config.yaml"


def get_config(path):
    with open(path) as f:
        parsed_config = yaml.safe_load(f)
        parsed_config["postgres"]["database_url"] = os.getenv("DATABASE_URL")
        return parsed_config


config = get_config(config_path)
