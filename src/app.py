import os
import random
import logging
import logging.handlers
import pymongo
from pymongo import MongoClient

import pytz
from datetime import datetime


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
    while i < 10:
        adsb_record = {
            'uid': str(i + 1),
            'time_stamp': datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S"),
            'value': random.randint(0, 100)
        }
        adsb_result = adsb_records.insert_one(adsb_record)
        logging.info(f"New adsb record insert to mongodb, id: {adsb_result.inserted_id}")

        noise_record = {
            'uid': str(i + 1),
            'time_stamp': datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime("%Y-%m-%d %H:%M:%S"),
            'value': random.randint(0, 1000)
        }
        noise_result = noise_records.insert_one(noise_record)
        logging.info(f"New noise record insert to mongodb, id: {noise_result.inserted_id}")
        i = i + 1

    last_adsb_record = db.adsb.find().sort([("time_stamp", pymongo.DESCENDING)]).limit(1)[0]
    last_noise_record = db.noise.find().sort([("time_stamp", pymongo.DESCENDING)]).limit(1)[0]
    logging.info(f"Last adsb record:: {last_adsb_record}")
    logging.info(f"Last noise record:: {last_noise_record}")


if __name__ == "__main__":
    main()
