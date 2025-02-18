# Download Mayland Water Quality data from the National Water Quality Monitoring Council
# https://www.waterqualitydata.us/#countrycode=US&statecode=US%3A24&countycode=US%3A24%3A003&countycode=US%3A24%3A005&countycode=US%3A24%3A027&countycode=US%3A24%3A031&countycode=US%3A24%3A033&countycode=US%3A24%3A510&sampleMedia=Water&characteristicType=Physical&startDateLo=01-01-2014&startDateHi=12-31-2024&mimeType=csv&dataProfile=resultPhysChem&providers=NWIS&providers=STORET

#call library = library(dataRetrieval)

# Data Profile - Organization Data:
organizations <- readWQPdata(service = "Organization"
                            , querySummary = FALSE
                            , tz = "America/New_York"
                            , countrycode = "US"
                            , statecode = "MD"
                            , countycode = "003"
                            , countycode = "US:24:005"
                            , countycode = "US:24:027"
                            , countycode = "US:24:031"
                            , countycode = "US:24:033"
                            , countycode = "US:24:510"
                            , sampleMedia = "Water"
                            , characteristicType = "Physical"
                            , startDateLo = "01-01-2014"
                            , startDateHi = "12-31-2024"
                            , providers = "NWIS"
                            , providers = "STORET")

write.csv(organizations, "raw_data/organizations.csv")

# Data Profile - Project Data:
projects <- readWQPdata(service = "Project"
                        , querySummary = FALSE
                        , tz = "America/New_York"
                        , countrycode = "US"
                        , statecode = "MD"
                        , countycode = "003"
                        , countycode = "US:24:005"
                        , countycode = "US:24:027"
                        , countycode = "US:24:031"
                        , countycode = "US:24:033"
                        , countycode = "US:24:510"
                        , sampleMedia = "Water"
                        , characteristicType = "Physical"
                        , startDateLo = "01-01-2014"
                        , startDateHi = "12-31-2024"
                        , providers = "NWIS"
                        , providers = "STORET")
            
write.csv(projects, "raw_data/projects.csv")

# Data Profile - Site Data Only:
sites <- readWQPdata(service = "Station"
                                 , querySummary = FALSE
                                 , tz = "America/New_York"
                                 , countrycode = "US"
                                 , statecode = "MD"
                                 , countycode = "003"
                                 , countycode = "US:24:005"
                                 , countycode = "US:24:027"
                                 , countycode = "US:24:031"
                                 , countycode = "US:24:033"
                                 , countycode = "US:24:510"
                                 , sampleMedia = "Water"
                                 , characteristicType = "Physical"
                                 , startDateLo = "01-01-2014"
                                 , startDateHi = "12-31-2024"
                                 , providers = "NWIS"
                                 , providers = "STORET")

write.csv(sites, "raw_data/sites.csv")

# Data Profile - Sample Results (physical/chemical metadata):
physical_chemistry_results <- readWQPdata(service = "Result"
                                , querySummary = FALSE
                                , tz = "America/New_York"
                                , countrycode = "US"
                                , statecode = "MD"
                                , countycode = "003"
                                , countycode = "US:24:005"
                                , countycode = "US:24:027"
                                , countycode = "US:24:031"
                                , countycode = "US:24:033"
                                , countycode = "US:24:510"
                                , sampleMedia = "Water"
                                , characteristicType = "Physical"
                                , startDateLo = "01-01-2014"
                                , startDateHi = "12-31-2024"
                                , providers = "NWIS"
                                , providers = "STORET"
                                , dataProfile = "resultPhysChem")

write.csv(physical_chemistry_results, "raw_data/physchem_results.csv")

