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

def rain_in_to_mm(rain_mm):
    """convierte la lluvia de pulgadas a milimetros"""
    r_mm = rain_mm * 24.5
    return r_mm

con = sqlite3.connect('/var/lib/weewx/weewx.sdb')

df = pd.read_sql_query('SELECT datetime, rain, outTemp, barometer, windDir, windSpeed, dewpoint, inHumidity from archive order by datetime', con)

df["dateTime"] = pd.to_datetime(df['dateTime'], unit="s", utc=True, ).dt.tz_convert('America/Costa_Rica')


df["outTemp"] = fahr_to_celsius(df["outTemp"])

df["dewpoint"] = fahr_to_celsius(df["dewpoint"])

df["barometer"] = bar_in_to_hPa(df["barometer"])

df["rain"] = rain_in_to_mm(df["rain"])

df = df.round({'rain': 2, 'inTemp': 2, 'outTemp': 2, 'barometer': 2, 'windDir': 2, 'windSpeed': 2, 'dewpoint': 2, 'inHumidity': 2})

df.to_csv('datos.csv', index=False)

print(df.head())

con.close()
