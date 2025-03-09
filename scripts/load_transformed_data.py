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

# Create the schema if it does not exist
with engine.connect() as connection:
    connection.execute("CREATE SCHEMA IF NOT EXISTS transformed_water_quality")

# File paths
trans_orgs_file = 'data/transformed/organizations.parquet'
trans_projs_file = 'data/transformed/projects.parquet'
trans_sites_file = 'data/transformed/sites.parquet'
trans_physchem_results_file = 'data/transformed/physchem_results.parquet'

# Function to load the organizations data
def load_orgs():
    if os.path.exists(trans_orgs_file):
        orgs = pd.read_parquet(trans_orgs_file)
        orgs.to_sql('orgs', engine, schema='transformed_water_quality', if_exists='replace', index=False)
    else:
        print(f"File {trans_orgs_file} does not exist")

# Function to load the projects data
def load_projs():
    if os.path.exists(trans_projs_file):
        projs = pd.read_parquet(trans_projs_file)
        projs.to_sql('projs', engine, schema='transformed_water_quality', if_exists='replace', index=False)
    else:
        print(f"File {trans_projs_file} does not exist")

# Function to load the sites data
def load_sites():
    if os.path.exists(trans_sites_file):
        sites = pd.read_parquet(trans_sites_file)
        sites.to_sql('sites', engine, schema='transformed_water_quality', if_exists='replace', index=False)
    else:
        print(f"File {trans_sites_file} does not exist")        

# Function to load the physical results data
def load_physchem_results():
    if os.path.exists(trans_physchem_results_file):
        physchem_results = pd.read_parquet(trans_physchem_results_file)
        physchem_results.to_sql('physchem_results', engine, schema='transformed_water_quality', if_exists='replace', index=False)
    else:
        print(f"File {trans_physchem_results_file} does not exist")

# Call the functions to load data into the database
load_orgs()
load_projs()
load_sites()
load_physchem_results()