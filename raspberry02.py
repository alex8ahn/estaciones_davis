import sqlite3
import pandas as pd
import datetime


def fahr_to_celsius(temp_fahr):
    """Convierte farenhait a celsius
    
    Returna en grados celsius"""
    temp_celsius = (temp_fahr - 32) * 5 / 9
    return temp_celsius


def bar_in_to_hPa(bar_in):
    """convierte la presion atmosferica de pulgadas de mercurio a milibare Hpa"""
    bar_hPa = bar_in * 33.8638
    return bar_hPa
    
con = sqlite3.connect('/home/weewx/archive/weewx.sdb')

df = pd.read_sql_query('SELECT rain, inTemp, outTemp, barometer, windDir, windSpeed, dewpoint, inHumidity, outHumidity, datetime from archive order by datetime', con)

df["dateTime"] = pd.to_datetime(df['dateTime'], unit="s", utc=True, ).dt.tz_convert('America/Costa_Rica')

df["inTemp"] = fahr_to_celsius(df["inTemp"])

df["outTemp"] = fahr_to_celsius(df["outTemp"])

df["barometer"] = bar_in_to_hPa(df["barometer"]) 

df = df.round({'rain': 2, 'inTemp': 2, 'outTemp': 2, 'barometer': 2, 'windDir': 2, 'windSpeed': 2})

df.to_csv('datos.csv', index=False)

print(df.head())

con.close()
