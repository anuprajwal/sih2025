import netCDF4 as nc

# Open file
ds = nc.Dataset("1900121_prof.nc")

# List variables
print(ds.variables.keys())

# Example: get temperature, salinity, pressure
temp = ds.variables['TEMP'][:]
sal  = ds.variables['PSAL'][:]
pres = ds.variables['PRES'][:]

# Dimensions
print(ds.dimensions.keys())
print(temp.shape)   # e.g., (n_profiles, n_levels)
