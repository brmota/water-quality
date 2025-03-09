import pandas as pd
import os
import numpy as np
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

# File paths
orgs_file = '/Users/MoMoney/Documents/GitHub/water_quality_md/raw/organizations.csv'
projs_file = '/Users/MoMoney/Documents/GitHub/water_quality_md/raw/projects.csv'
sites_file = '/Users/MoMoney/Documents/GitHub/water_quality_md/raw/sites.csv'
physchem_results_file = '/Users/MoMoney/Documents/GitHub/water_quality_md/raw/physchem_results.csv'

# Function load organizations data to database
def load_orgs():
    if os.path.exists(orgs_file):
        orgs = pd.read_csv(orgs_file)
        orgs.to_sql('orgs', engine, schema='raw', if_exists='replace', index=False)
    else:
        print(f"File {orgs_file} does not exist")

# Function load projects data to database
def load_projs():
    if os.path.exists(projs_file):
        projs = pd.read_csv(projs_file)
        projs.to_sql('projs', engine, schema='raw', if_exists='replace', index=False)
    else:
        print(f"File {projs_file} does not exist")

# Function load sites data to database
def load_sites():
    if os.path.exists(sites_file):
        sites = pd.read_csv(sites_file)
        sites.to_sql('sites', engine, schema='raw', if_exists='replace', index=False)
    else:
        print(f"File {sites_file} does not exist")

# Function load physical chemistry results data to database
def load_physchem_results():
    if os.path.exists(physchem_results_file):
        physchem_results = pd.read_csv(physchem_results_file)
        physchem_results.to_sql('physchem_results', engine, schema='raw', if_exists='replace', index=False)
    else:
        print(f"File {physchem_results_file} does not exist")

# Call the functions to load the raw data into the database
load_orgs()
load_projs()
load_sites()
load_physchem_results()
