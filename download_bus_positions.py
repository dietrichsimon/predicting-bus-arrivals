'''Downloads GTFS realtime vehicle position data for all TRIMET buses of the
Portland transit system every 30 seconds and saves them into a postgres
database.'''

# Load packages
from google.transit import gtfs_realtime_pb2
import requests
import os
import time
import psycopg2
import config
from sqlalchemy import create_engine

# Define global variables
DATABASE_URL = config.DATABASE_URL

API_ID = config.API_KEY_TRIMET
FEED = gtfs_realtime_pb2.FeedMessage()

BUS_POSITION_URL = 'http://developer.trimet.org/ws/V1/VehiclePositions'+ '/appID/' + API_ID

# Define functions
def create_bus_positions_table():
    '''creates a db table for the gtfs rt bus vehicle positions feed'''
    engine.execute('''CREATE TABLE IF NOT EXISTS public.bus_positions (
                              id INT,
                              trip_id VARCHAR,
                              route_id VARCHAR,
                              latitude FLOAT,
                              longitude FLOAT,
                              bearing FLOAT,
                              current_stop_sequence VARCHAR,
                              current_status VARCHAR,
                              update_time INT,
                              stop_id VARCHAR,
                              vehicle_id VARCHAR,
                              vehicle_label VARCHAR
                            );
                            ''')

def extract_data(url):
    '''extracts data from GTFS API'''
    FEED = gtfs_realtime_pb2.FeedMessage()
    response = requests.get(url, allow_redirects=True)
    FEED.ParseFromString(response.content)
    data = FEED.entity
    return data

def load_bus_positions(data):
    '''Loads GTFS RT bus position data into database'''
    for i in data:
        engine.execute(f'''INSERT INTO bus_positions(id,
                                                    trip_id,
                                                    route_id,
                                                    latitude,
                                                    longitude,
                                                    bearing,
                                                    current_stop_sequence,
                                                    current_status,
                                                    update_time,
                                                    stop_id,
                                                    vehicle_id,
                                                    vehicle_label
                                                    )
                        VALUES ('{i.id}',
                                '{i.vehicle.trip.trip_id}',
                                '{i.vehicle.trip.route_id}',
                                '{i.vehicle.position.latitude}',
                                '{i.vehicle.position.longitude}',
                                '{i.vehicle.position.bearing}',
                                '{i.vehicle.current_stop_sequence}',
                                '{i.vehicle.current_status}',
                                '{i.vehicle.timestamp}',
                                '{i.vehicle.stop_id}',
                                '{i.vehicle.vehicle.id}',
                                '{i.vehicle.vehicle.label}'
                                );
                                ''')

# Connect to postgres database
engine = None
while not engine:
    try:
        engine = create_engine(DATABASE_URL, echo=False)
    except:
        print('Connection to database failed. Trying again in 30 seconds.')
        time.sleep(30)

# Create postgres table
create_bus_positions_table()

if __name__ == '__main__':

    # Extract and load every 30 seconds
    nexttime = time.time()

    while True:
        print(time.ctime()) # print time of request for debugging

        try:
            bus_data = extract_data(BUS_POSITION_URL)
            load_bus_positions(bus_data)
        except:
            print('Error while extracting or loading bus data. Trying again in 30 sec.')

        nexttime += 30
        sleeptime = nexttime - time.time()
        if sleeptime > 0:
            time.sleep(sleeptime)
