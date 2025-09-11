# view_cycle.py

import xarray as xr
import sys
import pymysql
import json
import numpy as np
from datetime import datetime



def view_cycle_file(file_path):
    # Open NetCDF file
    ds = xr.open_dataset(file_path)

    print("\n📂 Variables in this cycle file:")
    print(list(ds.variables.keys()))

    print("\n📐 Dimensions:")
    print(ds.dims)

    latitude=0
    longitude =0
    date = 0
    param = []

    # Metadata
    print("\n🌍 Location & Time info:")
    if "LATITUDE" in ds:
        print("Latitude :", ds["LATITUDE"].values)
        latitude = ds["LATITUDE"].values
    if "LATITUDE" in ds:
        print("platform num :", ds["PLATFORM_NUMBER"].values)
        print("project name :", ds["PROJECT_NAME"].values)
        print("PI_NAME name :", ds["PI_NAME"].values)
        print("STATION_PARAMETERS :", ds["STATION_PARAMETERS"].values)
        print("DIRECTION :", ds["DIRECTION"].values)
    if "LONGITUDE" in ds:
        print("Longitude:", ds["LONGITUDE"].values)
        longitude = ds["LONGITUDE"].values
    if "JULD" in ds:
        print("Julian Date:", ds["JULD"].values)
        date = ds["JULD"].values

    # Core parameters
    for var in ["PRES", "TEMP", "PSAL"]:
        # if var in ds:
            print(f"\n🔹 {var} data (first 10 values):")
            print(ds[var].values[0])
        # print([float(ds["PRES"].values[0][var]), float(ds["TEMP"].values[0][var]), float(ds["PSAL"].values[0][var])])
        # param.append([float(ds["PRES"].values[0][var]), float(ds["TEMP"].values[0][var]), float(ds["PSAL"].values[0][var])])

    ds.close()
    return (latitude, longitude, date, param)


def save_cycle(latitude, longitude, date, params):
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="ANUprajwal",
            database="netcdf"
        )
        cursor = conn.cursor()

        query = """
        INSERT INTO cycles (date, latitude, longitude, params)
        VALUES (%s, %s, %s, %s)
        """

        # if isinstance(date, str):
        #     try:
        #         # Adjust format if your date string is different
        #         date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        #     except ValueError:
        #         print("⚠️ Date format mismatch. Expected YYYY-MM-DD.")
        #         return

        # Ensure JSON string
        params_json = json.dumps(params)

        values = (date, latitude, longitude, params_json)

        cursor.execute(query, values)
        conn.commit()

        print("✅ Cycle saved successfully!")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



if __name__ == "__main__":
    
    latitude, longitude, date, param = view_cycle_file("D1900121_001.nc")
    # print(float(latitude[0]), float(longitude[0]), str(date[0]), param)
    # save_cycle(float(latitude[0]), float(longitude[0]), str(date[0]), param)
