# view_cycle.py

import xarray as xr
import sys, os
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
    float_id = 0
    cycle = 0
    project_name = ''
    researcherName = ''
    param = []

    # Metadata
    print("\n🌍 Location & Time info:")
    if "LATITUDE" in ds:
        print("Latitude :", ds["LATITUDE"].values)
        latitude = ds["LATITUDE"].values
    if "LATITUDE" in ds:
        print("platform num :", ds["PLATFORM_NUMBER"].values)
        float_id = ds["PLATFORM_NUMBER"].values
        print("project name :", ds["PROJECT_NAME"].values)
        project_name = ds["PROJECT_NAME"].values
        print("PI_NAME name :", ds["PI_NAME"].values)
        researcherName = ds["PI_NAME"].values
        print("CYCLE_NUMBER :", ds["CYCLE_NUMBER"].values)
        cycle = ds["CYCLE_NUMBER"].values
        print("DIRECTION :", ds["DIRECTION"].values)
    if "LONGITUDE" in ds:
        print("Longitude:", ds["LONGITUDE"].values)
        longitude = ds["LONGITUDE"].values
    if "JULD" in ds:
        print("Julian Date:", ds["JULD"].values)
        date = ds["JULD"].values

    # Core parameters
    for var in range(0,45):
        # if var in ds:
            # print(f"\n🔹 {var} data (first 10 values):")
            # print(ds[var].values[0])
        # print()
        # print([float(ds["PRES"].values[0][var]), float(ds["TEMP"].values[0][var]), float(ds["PSAL"].values[0][var])])
        param.append([float(ds["PRES"].values[0][var]), float(ds["TEMP"].values[0][var]), float(ds["PSAL"].values[0][var])])
    ds.close()
    return (latitude, longitude, date, float_id, cycle, project_name, researcherName, param)


def save_cycle(latitude, longitude, date, float_id, cycle, project_name, researcherName, params):
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="ANUprajwal",
            database="netcdf"
        )
        cursor = conn.cursor()

        query = """
        INSERT INTO cycles (date, latitude, longitude, float_id, cycle, project_name, researcherName, params)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        # Ensure JSON string
        params_json = json.dumps(params)

        values = (date, latitude, longitude, float_id, cycle, project_name, researcherName, params_json)

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
    folder_path = "chroma_db"
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    print(files)

    for i in files:
        latitude, longitude, date, float_id, cycle, project_name, researcherName, param = view_cycle_file("D1900121_001.nc")


        float_id = str(float_id[0])
        float_id = float_id[2:-1].strip()

        project_name = str(project_name[0])
        project_name = project_name[2:-1].strip()

        researcherName = str(researcherName[0])
        researcherName = researcherName[2:-1].strip()
        print(int(cycle[0])  )
        # save_cycle(float(latitude[0]), float(longitude[0]), str(date[0]), float_id, int(cycle[0]), project_name, researcherName, param)
