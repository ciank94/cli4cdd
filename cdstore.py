import cdsapi

dataset = "satellite-sea-level-global"
request = {
    "variable": ["daily"],
    "year": ["2017"],
    "month": ["01"],
    "day": ["01"],
    "version": "vdt2021",
    "data_format": "netcdf",
    "download_format": "unarchived"
    }
target = 'SLA_2017.nc'
client = cdsapi.Client()
client.retrieve(dataset, request, target).download()

# dataset = "reanalysis-era5-single-levels"
# request = {
#         "product_type": ["reanalysis"],
#         "variable": [
#                     "10m_u_component_of_wind",
#                     "10m_v_component_of_wind",
#                     "2m_dewpoint_temperature",
#                     "2m_temperature",
#                     "mean_sea_level_pressure",
#                     "surface_pressure",
#                     "mean_total_precipitation_rate",
#                     "mean_surface_downward_short_wave_radiation_flux",
#                     "mean_surface_downward_long_wave_radiation_flux",
#                     "mean_snowfall_rate"
#                 ],
#         "year": ["2009"],
#         "month": ["06"],
#         "day": [
#                     "01", "02", "03",
#                     "04", "05", "06",
#                     "07", "08", "09",
#                     "10", "11", "12",
#                     "13", "14", "15",
#                     "16", "17", "18",
#                     "19", "20", "21",
#                     "22", "23", "24",
#                     "25", "26", "27",
#                     "28", "29", "30",
#                     "31"
#                 ],
#         "time": [
#                     "00:00", "03:00", "06:00",
#                     "09:00", "12:00", "15:00",
#                     "18:00", "21:00"
#                 ],
#         "data_format": "netcdf",
#         "download_format": "unarchived"
#     }
# target = 'output_rates_2009.nc'
# client = cdsapi.Client()
# client.retrieve(dataset, request, target)


# dataset = "reanalysis-era5-single-levels"
# request = {
#         "product_type": ["reanalysis"],
#         "variable": [
#                     "10m_u_component_of_wind",
#                     "10m_v_component_of_wind",
#                     "2m_dewpoint_temperature",
#                     "2m_temperature",
#                     "mean_sea_level_pressure",
#                     "surface_pressure",
#                     "total_precipitation",
#                     "surface_solar_radiation_downwards",
#                     "surface_thermal_radiation_downwards",
#                     "snowfall"
#                 ],
#         "year": ["2009"],
#         "month": ["06"],
#         "day": ["01"],
#         "time": [
#                     "00:00", "03:00", "06:00",
#                     "09:00"
#                 ],
#         "data_format": "netcdf",
#         "download_format": "unarchived"
#     }
# target = 'example_2009.nc'

# client = cdsapi.Client()
# client.retrieve(dataset, request, target)
# dataset = "reanalysis-era5-single-levels"
# request = {
#         "product_type": ["reanalysis"],
#         "variable": [
#                     "10m_u_component_of_wind",
#                     "10m_v_component_of_wind",
#                     "2m_dewpoint_temperature",
#                     "2m_temperature",
#                     "mean_sea_level_pressure",
#                     "surface_pressure",
#                     "total_precipitation",
#                     "surface_solar_radiation_downwards",
#                     "surface_thermal_radiation_downwards",
#                     "snowfall"
#                 ],
#         "year": ["2009"],
#         "month": ["06"],
#         "day": ["01"],
#         "time": [
#                     "00:00", "03:00", "06:00",
#                     "09:00"
#                 ],
#         "data_format": "netcdf",
#         "download_format": "unarchived"
#     }
# target = 'example_2009.nc'

# client = cdsapi.Client()
# client.retrieve(dataset, request, target)