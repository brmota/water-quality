import pandas as pd
import os
from sqlalchemy import create_engine
import psycopg2

# Database connection details
db_user = 'postgres'
db_password = ' '
db_name = 'environment'
db_host = 'localhost'
db_port = '5432'

# Create a database engine
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# SQL query to export relevant data for Tableau
sql_query = """
select 
	physchem_results_id
	, organization_identifier
	, project_identifier
	, activity_start_date
	, monitoring_location_identifier
	, activity_location_latitude_measure
	, activity_location_longitude_measure
	, monitoring_location_name
	, salinity
	, optical_density
	, temperature_water
	, p_h
	, dissolved_oxygen_d_o
from transformed_water_quality.physchem_results
where (
	salinity is not null
	or optical_density is not null
	or temperature_water is not null 
	or p_h is not null
	or dissolved_oxygen_d_o is not null
)
order by activity_start_date
"""

# Fetch the data from the database
export_for_tableau = pd.read_sql(sql_query, engine)

# Export the data to a CSV file for Tableau
export_for_tableau.to_csv("data/tableau/water_quality_tableau.csv", index=False)

print("Data exported for Tableau.")