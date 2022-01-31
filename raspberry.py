import sqlite3
import pandas as pd
import datetime


def fahr_to_celsius(temp_fahr):
    """Convierte farenhait a celsius
    
    Returna en grados celsius"""
    temp_celsius = (temp_fahr - 32) * 5 / 9
    return temp_celsius

con = sqlite3.connect('/home/weewx/archive/weewx.sdb')

df = pd.read_sql_query('SELECT rain, inTemp, outTemp, datetime from archive order by datetime', con)

df["dateTime"] = pd.to_datetime(df['dateTime'], unit="s", utc=True, ).dt.tz_convert('America/Costa_Rica')

df["inTemp"] = fahr_to_celsius(df["inTemp"])

df["outTemp"] = fahr_to_celsius(df["outTemp"])

df = df.round({'rain': 2, 'inTemp': 2, 'outTemp': 2})

df.to_csv('datos.csv', index=False)

print(df.head())

con.close()
