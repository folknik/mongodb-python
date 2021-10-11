import os
import random
import logging
import logging.handlers
from pymongo import MongoClient


handler = logging.handlers.RotatingFileHandler(
    filename=os.environ.get("LOGFILE", "./logs/logfile.log"),
    maxBytes=2*1024*1024
)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)


def main():
    connector = 'mongodb://root:secret@mongodb:27017/'
    client = MongoClient(connector)

    db = client['eco_db']

    adsb_records = db.adsb
    noise_records = db.noise

    i = 0
    while i < 100:
        adsb_record = {
            'id': str(i + 1),
            'value': random.randint(0, 100)
        }
        adsb_result = adsb_records.insert_one(adsb_record)
        logging.info(f"New adsb record insert to mongodb, id: {adsb_result.inserted_id}")

        noise_record = {
            'id': str(i + 1),
            'value': random.randint(0, 1000)
        }
        noise_result = noise_records.insert_one(noise_record)
        logging.info(f"New noise record insert to mongodb, id: {noise_result.inserted_id}")
        i = i + 1


if __name__ == "__main__":
    main()
