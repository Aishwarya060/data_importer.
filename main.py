import yaml
from data_importer.api_client import APIClient
from data_importer.db import Database

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()

    # Initialize API client and database
    api_client = APIClient(config["api"]["url"])
    db = Database(config["database"])

    # Fetch and store data
    data = api_client.fetch_data()
    for item in data:
        phone_id = item.get("id")
        phone_name = item.get("name")
        phone_data = item.get("data", {})
        db.insert_phone(phone_id, phone_name, phone_data)

    print("Data import completed.")

if __name__ == "__main__":
    main()
