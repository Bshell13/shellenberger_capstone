"""
This will be used to clean the incoming data
"""

# import pandas as pd
# import csv
import pathlib

"""Setting up paths to extract data"""
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DATA_FOLDER = PROJECT_ROOT.joinpath('data')
TIME_SERIES_DATA = DATA_FOLDER.joinpath('zillow_time_series.csv')
HOUSE_PRICING_DATA = DATA_FOLDER.joinpath('kaggle_house_pricing.csv')


def cleaning_zillow_data(zillow_data):
    print(zillow_data.head(10))


def main():
    cleaning_zillow_data(TIME_SERIES_DATA)



if __name__ == "__main__":
    main()