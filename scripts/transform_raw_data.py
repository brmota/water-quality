import pandas as pd
import os
import re

# File paths
orgs_file = 'data/raw/organizations.csv'
trans_orgs_file = 'data/transformed/organizations.parquet'
projs_file = 'data/raw/projects.csv'
trans_projs_file = 'data/transformed/projects.parquet'
sites_file = 'data/raw/sites.csv'
trans_sites_file = 'data/transformed/sites.parquet'
physchem_results_file = 'data/raw/physchem_results.csv'
trans_physchem_results_file = 'data/transformed/physchem_results.parquet'

def to_snake_case(column_name):
    column_name = column_name.replace('.', '')  # Remove dots from column names
    column_name = column_name.replace('(', '')  # Remove open parenthesis from column names
    column_name = column_name.replace(')', '')  # Remove close parenthesis from column names
    column_name = column_name.replace(',', '')  # Remove comma from column names
    column_name = column_name.replace('-', '_')  # Replace dash with an underscore
    column_name = column_name.replace('/', '_')  # Replace slash with an underscore    
    column_name = column_name.replace(' ', '_')  # Replace spaces with an underscore
    column_name = re.sub(r'(?<!^)(?=[A-Z])', '_', column_name).lower()  # Add underscore before capital letters and convert to lowercase
    column_name = column_name.replace('__', '_')  # Remove double underscores
    return column_name

# Function to transform the organizations data
def transform_orgs():
    if os.path.exists(orgs_file):
        orgs = pd.read_csv(orgs_file)
        # Define the columns to be converted to string
        columns_to_string = ['OrganizationIdentifier', 'OrganizationFormalName','OrganizationDescriptionText', 'OrganizationType', 
                             'TribalCode', 'ProviderName']
        # Convert the columns to string
        orgs[columns_to_string] = orgs[columns_to_string].astype(str) 
        # Define the columns to be converted to integer
        columns_to_integer = ['Unnamed: 0']     
        # Convert the columns to integer
        orgs[columns_to_integer] = orgs[columns_to_integer].astype(int)
        # Drop the columns that are not needed
        orgs = orgs.drop(columns=[col for col in orgs.columns if 'Address' in col])
        orgs = orgs.drop(columns=['Telephonic'])          
        # Update column name 'Unnamed: 0' to 'organization_id'
        orgs.rename(columns={'Unnamed: 0': 'organization_id'}, inplace=True) 
        # Convert all column names to snake_case
        orgs.columns = [to_snake_case(col) for col in orgs.columns]
        # Save the transformed data to a new file       
        #orgs.to_csv('data/transformed/organizations.csv', index=False)
        orgs.to_parquet(trans_orgs_file, index=False)
        #df_loaded = pd.read_parquet(trans_orgs_file)
        #print(df_loaded.dtypes)  # Data types are preserved
        print(f"Transformed data saved to: {trans_orgs_file}")
    else:
        print(f"File {orgs_file} does not exist")

# Function to transform the projects data
def transform_projs():
    if os.path.exists(projs_file):
        projs = pd.read_csv(projs_file)
        # Define the columns to be converted to string
        columns_to_string = ['OrganizationIdentifier', 'OrganizationFormalName', 'ProjectIdentifier', 'ProjectName', 
                             'ProjectDescriptionText', 'SamplingDesignTypeCode', 'QAPPApprovalAgencyName', 'ProjectFileUrl', 
                             'ProjectMonitoringLocationWeightingUrl']
        # Convert the columns to string
        projs[columns_to_string] = projs[columns_to_string].astype(str)
        # Define the columns to be converted to integer
        columns_to_integer = ['Unnamed: 0']     
        # Convert the columns to integer
        projs[columns_to_integer] = projs[columns_to_integer].astype(int)
        # Define the columns to be converted to boolean
        columns_to_boolean = ['QAPPApprovedIndicator']
        # Convert the columns to boolean
        projs[columns_to_boolean] = projs[columns_to_boolean].astype(bool)
        # Update column name 'Unnamed: 0' to 'project_id'
        projs.rename(columns={'Unnamed: 0': 'project_id'}, inplace=True)
        # Convert all column names to snake_case
        projs.columns = [to_snake_case(col) for col in projs.columns]
        # Save the transformed data to a new file       
        #projs.to_csv('data/transformed/projects.csv', index=False)
        projs.to_parquet(trans_projs_file, index=False)
        #df_loaded = pd.read_parquet(trans_projs_file)
        #print(df_loaded.dtypes)  # Data types are preserved
        print(f"Transformed data saved to: {trans_projs_file}")
    else:
        print(f"File {projs_file} does not exist")        

# Function to transform the projects data
def transform_sites():
    if os.path.exists(sites_file):
        sites = pd.read_csv(sites_file)
        # Define the columns to be converted to string
        columns_to_string = ['OrganizationIdentifier', 'OrganizationFormalName', 'MonitoringLocationIdentifier', 
                             'MonitoringLocationName', 'MonitoringLocationTypeName', 'MonitoringLocationDescriptionText', 
                             'DrainageAreaMeasure.MeasureUnitCode', 'ContributingDrainageAreaMeasure.MeasureUnitCode', 
                             'HorizontalAccuracyMeasure.MeasureUnitCode', 'HorizontalCollectionMethodName', 
                             'HorizontalCoordinateReferenceSystemDatumName', 'VerticalMeasure.MeasureUnitCode', 'VerticalAccuracyMeasure.MeasureUnitCode', 
                             'VerticalCollectionMethodName', 'VerticalCoordinateReferenceSystemDatumName', 'CountryCode', 'AquiferName', 'LocalAqfrName', 
                             'FormationTypeText', 'AquiferTypeName', 'ConstructionDateText', 'WellDepthMeasure.MeasureUnitCode', 
                             'WellHoleDepthMeasure.MeasureUnitCode', 'ProviderName']
        # Convert the columns to string
        sites[columns_to_string] = sites[columns_to_string].astype(str)
        # Define the columns to be converted to integer
        columns_to_integer = ['Unnamed: 0', 'HUCEightDigitCode', 'StateCode', 'CountyCode']     
        # Convert the columns to integer
        sites[columns_to_integer] = sites[columns_to_integer].astype(int)
        # Define the columns to be converted to float
        columns_to_float = ['DrainageAreaMeasure.MeasureValue', 'ContributingDrainageAreaMeasure.MeasureValue', 'LatitudeMeasure', 
                            'LongitudeMeasure', 'SourceMapScaleNumeric', 'HorizontalAccuracyMeasure.MeasureValue', 
                            'VerticalMeasure.MeasureValue', 'VerticalAccuracyMeasure.MeasureValue', 'WellDepthMeasure.MeasureValue', 
                            'WellHoleDepthMeasure.MeasureValue']
        # Convert the columns to float
        sites[columns_to_float] = sites[columns_to_float].astype(float)
        # Update column name 'Unnamed: 0' to 'project_id'
        sites.rename(columns={'Unnamed: 0': 'site_id'}, inplace=True)
        # Convert all column names to snake_case
        sites.columns = [to_snake_case(col) for col in sites.columns]
        # Save the transformed data to a new file       
        #sites.to_csv('data/transformed/sites.csv', index=False)
        sites.to_parquet(trans_sites_file, index=False)
        #df_loaded = pd.read_parquet(trans_sites_file)
        #print(df_loaded.dtypes)  # Data types are preserved
        print(f"Transformed data saved to: {trans_sites_file}")
    else:
        print(f"File {sites_file} does not exist")           

# Function to transform the projects data
def transform_physchem_results():
    if os.path.exists(physchem_results_file):
        physchem_results = pd.read_csv(physchem_results_file, low_memory=False)
        # Define the columns to be converted to string
        columns_to_string = ['OrganizationIdentifier', 'OrganizationFormalName', 'ActivityIdentifier', 'ActivityTypeCode', 
                             'ActivityMediaName', 'ActivityMediaSubdivisionName', 'ActivityStartTime.TimeZoneCode', 
                             'ActivityEndTime.TimeZoneCode', 'ActivityRelativeDepthName', 'ActivityDepthHeightMeasure.MeasureUnitCode', 
                             'ActivityDepthAltitudeReferencePointText', 'ActivityTopDepthHeightMeasure.MeasureUnitCode', 
                             'ActivityBottomDepthHeightMeasure.MeasureUnitCode', 'ProjectIdentifier', 'ProjectName', 
                             'ActivityConductingOrganizationText', 'MonitoringLocationIdentifier', 'MonitoringLocationName', 
                             'ActivityCommentText', 'SampleAquifer', 'HydrologicCondition', 'HydrologicEvent', 
                             'SampleCollectionMethod.MethodIdentifier', 'SampleCollectionMethod.MethodIdentifierContext', 
                             'SampleCollectionMethod.MethodName', 'SampleCollectionMethod.MethodDescriptionText', 
                             'SampleCollectionEquipmentName', 'ResultIdentifier', 'ResultDetectionConditionText', 'MethodSpeciationName', 
                             'CharacteristicName', 'ResultSampleFractionText', 'ResultMeasure.MeasureUnitCode', 'MeasureQualifierCode', 
                             'ResultStatusIdentifier', 'StatisticalBaseCode', 'ResultValueTypeName', 'ResultWeightBasisText', 
                             'ResultTimeBasisText', 'ResultTemperatureBasisText', 'ResultParticleSizeBasisText', 
                             'DataQuality.ConfidenceIntervalValue', 'DataQuality.UpperConfidenceLimitValue', 
                             'DataQuality.LowerConfidenceLimitValue', 'ResultCommentText', 'ResultDepthHeightMeasure.MeasureUnitCode', 
                             'ResultDepthAltitudeReferencePointText', 'BinaryObjectFileName', 'BinaryObjectFileTypeCode', 'ResultFileUrl', 
                             'ResultAnalyticalMethod.MethodIdentifier', 'ResultAnalyticalMethod.MethodIdentifierContext', 
                             'ResultAnalyticalMethod.MethodName', 'ResultAnalyticalMethod.MethodDescriptionText', 'LaboratoryName', 
                             'ResultLaboratoryCommentText', 'ResultDetectionQuantitationLimitUrl', 'DetectionQuantitationLimitTypeName', 
                             'DetectionQuantitationLimitMeasure.MeasureUnitCode', 'LastUpdated', 'ProviderName']
        # Convert the columns to string
        columns_to_string = [col for col in columns_to_string if col in physchem_results.columns]
        physchem_results[columns_to_string] = physchem_results[columns_to_string].astype(str)
        # Define the columns to be converted to integer
        columns_to_integer = ['USGSPCode', 'ActivityStartTime.TimeZoneCode_offset', 'ActivityEndTime.TimeZoneCode_offset']     
        columns_to_integer = [col for col in columns_to_integer if col in physchem_results.columns]
        # Handle non-finite values before converting to integer
        physchem_results[columns_to_integer] = physchem_results[columns_to_integer].fillna(0).astype(int)
        # Define the columns to be converted to float
        columns_to_float = ['ActivityDepthHeightMeasure.MeasureValue', 'ActivityTopDepthHeightMeasure.MeasureValue', 
                            'ActivityBottomDepthHeightMeasure.MeasureValue', 'ResultMeasureValue', 
                            'DetectionQuantitationLimitMeasure.MeasureValue', 'ActivityLocation.LatitudeMeasure', 
                            'ActivityLocation.LongitudeMeasure', 'ResultDepthHeightMeasure.MeasureValue']
        columns_to_float = [col for col in columns_to_float if col in physchem_results.columns]
        # Handle non-numeric values before converting to float
        for col in columns_to_float:
            physchem_results[col] = pd.to_numeric(physchem_results[col], errors='coerce')
        # Define the columns to be converted to date
        columns_to_date = ['ActivityStartDate', 'ActivityEndDate', 'AnalysisStartDate']
        columns_to_date = [col for col in columns_to_date if col in physchem_results.columns]
        # Convert the columns to date
        physchem_results[columns_to_date] = physchem_results[columns_to_date].apply(pd.to_datetime, format='%Y-%m-%d')
        # Define the columns to be converted to time
        columns_to_time = ['ActivityStartTime.Time', 'ActivityEndTime.Time']
        columns_to_time = [col for col in columns_to_time if col in physchem_results.columns]
        # Convert the columns to time
        for col in columns_to_time:
            physchem_results[col] = pd.to_datetime(physchem_results[col], format='%H:%M:%S').dt.time
        # Define the columns to be converted to datetime
        columns_to_datetime = ['LastUpdated', 'ActivityStartDateTime', 'ActivityEndDateTime']
        columns_to_datetime = [col for col in columns_to_datetime if col in physchem_results.columns]
        # Convert the columns to datetime
        for col in columns_to_datetime:
            physchem_results[col] = pd.to_datetime(physchem_results[col], format='ISO8601')
        # Pivot the data to create separate columns for each result value type
        physchem_results = pd.pivot_table(
            physchem_results, 
            index=[
                'Unnamed: 0',
                'OrganizationIdentifier',
                'ProjectIdentifier',
                'ActivityStartDate',
                'MonitoringLocationIdentifier',
                'ActivityLocation.LatitudeMeasure', 
                'ActivityLocation.LongitudeMeasure',
                'MonitoringLocationName'
            ],
            columns='CharacteristicName', 
            values='ResultMeasureValue'
        ).reset_index()
        # Update column name 'Unnamed: 0' to 'project_id'
        physchem_results.rename(columns={'Unnamed: 0': 'physchem_results_id'}, inplace=True)
        # Convert all column names to snake_case
        physchem_results.columns = [to_snake_case(col) for col in physchem_results.columns]
        # Save the transformed data to a new file       
        #physchem_results.to_csv('data/transformed/physchem_results.csv', index=False)
        physchem_results.to_parquet(trans_physchem_results_file, index=False)
        #df_loaded = pd.read_parquet(trans_physchem_results_file)
        #print(df_loaded.dtypes)  # Data types are preserved
        print(f"Transformed data saved to: {trans_physchem_results_file}")
    else:
        print(f"File {physchem_results_file} does not exist") 

# Call the functions to transform the data
transform_orgs()
transform_projs()
transform_sites()
transform_physchem_results()