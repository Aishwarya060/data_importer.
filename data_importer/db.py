import psycopg2
import json
from psycopg2.extras import Json
from data_importer.logger import setup_logger

logger = setup_logger()

class Database:
    def __init__(self, config):
        self.conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['name'],
            user=config['user'],
            password=config['password']
        )
        self.cursor = self.conn.cursor()

    def insert_phone(self, phone_id, phone_name, phone_data):
        try:
            query = """
            INSERT INTO public.phone (phoneid, phone_name, phone_data)
            VALUES (%s, %s, %s)
            ON CONFLICT (phoneid) DO NOTHING;
            """
            self.cursor.execute(query, (phone_id, phone_name, Json(phone_data)))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error inserting data into DB: {e}")
            self.conn.rollback()
