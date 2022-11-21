#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime

import altair as alt
import pandas as pd
import re
import requests
import requests_cache

# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()

# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1": "Oslo",
    "NO2": "Kristiansand",
    "NO3": "Trondheim",
    "NO4": "Tromsø",
    "NO5": "Bergen"
}


# task 5.1:
def zero_pad(n: str):
    """zero-pad a number string
        turns '2' into '02'
    args:
        n           (str): Number to be zero-padded

    returns:
        n           (str): Same number, now zero-padded
    """
    if len(n) == 2:
        return n
    else:
        n = "".join(("0",n))
        return n

def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    args:
        date            (datetime.date): datetime.date object with desired date to get electricy prices
        location                  (str): Which location to get prices from (see LOCATION CODES)

    returns:
        df              (pd.DataFrame): Pandas dataframe containing electricity prices, and time of day.

    """
    if date is None:
        date = datetime.date.today()
    year = str(date.year)
    month = zero_pad(str(date.month))
    day = zero_pad(str(date.day))

    assert float(month) >= 10 and float(day) >= 2 and float(year) >= 2022, "Date must be after 02.10.2022"

    url = "https://www.hvakosterstrommen.no/api/v1/prices/"+year+"/"+month+"-"+day+"_"+location+".json"
    json = requests.get(url).json()
    prices = []
    start_times = []

    for hour in range(24):
        price = json[hour]["NOK_per_kWh"]
        time = json[hour]["time_start"]
        start = pd.to_datetime(time,utc=True).tz_convert("Europe/Oslo").to_pydatetime()
        prices.append(price)
        start_times.append(start)


    time_start = pd.Series(start_times)
    NOK_per_kWh = pd.Series(prices)
    df = pd.DataFrame({"NOK_per_kWh":NOK_per_kWh, "time_start":time_start})

    return df



# task 1:


def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations=tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    Make sure to document arguments and return value...
    ...
    """
    if end_date is None:
        end_date = ...

    ...


# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    x-axis should be time_start
    y-axis should be price in NOK
    each location should get its own line

    Make sure to document arguments and return value...
    """
    ...


# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(
    df: pd.DataFrame, activity: str = "shower", minutes: float = 10
) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """

    ...


def main():
    """Allow running this module as a script for testing."""
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()


if __name__ == "__main__":
    fetch_day_prices(datetime.date(2022,10, 2), location="NO1")

    # main()
