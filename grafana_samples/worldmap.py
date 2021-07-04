import pandas as pd
from influxdb import InfluxDBClient


client = InfluxDBClient(host="localhost", port="8086")
client.switch_database("covid19")

df = pd.read_csv("countries.csv") 
df.dropna(inplace=True)


for rw_idx, row in df.iloc[1:].iterrows():
    json_body = [{
        "measurement": "CovidMap",
        "tags": {"country": row[0]},
        "fields": {
            "name": row[0],
            "latitude": row[2],
            "longitude": row[3],
            "metric": row[4]
        }
    }]
    client.write_points(json_body)