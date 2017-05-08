"""
python <script_name.py> <start_year> <end_year> <name_of_html_file>

sys.argv       0            1            2               3
"""

import pandas as pd
import sys, html5lib, lxml

#years = [x for x in range(int(sys.argv[1]), int(sys.argv[2]))]
#table_name =  sys.argv[3]y
table_race = ["race-result","fastest-laps","pit-stop-summary","starting-grid",
              "qualifying","practice-3","practice-2","practice-1"]

races_2016 = ["bahrain","china","russia","spain", "monaco","canada","austria",
              "great-britain","hungary","germany","belgium","italy","singapore",
              "malaysia","japan","united-states","mexico","brazil","abu-dhabi","europe"]

races_2015 = ["australia","malaysia","china", "bahrain","spain", "monaco","canada","austria",
              "great-britain","hungary","belgium","italy","singapore",
              "japan", "russia","united-states","mexico","brazil","abu-dhabi","europe"]

def race_weekend(races_2015, table_race):
    """
    The number is associated with the race in the url.
    This number should be added to the array.
    """
    number = 917
    for i in races_2015:
        print("Getting results for race: {}".format(i))
        for x in table_race:
            print("Getting results for table: {}".format(x))
            url = "https://www.formula1.com/en/results.html/2015/races/{}/{}/{}.html".format(number,i,x)
            df = pd.read_html(url)
            df = df[0]
            print("Frame: {}".format(df))
            df.to_csv("f1_{}_{}.csv".format(i,x), sep=",")
        number += 1


def get_results(years, table_name):
  """
  This function is for grabing tables from the "yearly" section. table_name = races, driver, team, fastest-lap.
  """
    for i in years:
        print("Getting results for year: {}".format(i))
        url = "https://www.formula1.com/en/results.html/{}/{}.html".format(i, table_name)
        df = pd.read_html(url)
        df = df[0]
        #df = df.drop("Unnamed: 0", 1)
        #df = df.drop("Unnamed: 5", 1)
        df.to_csv("f1_{}_{}.csv".format(table_name, i), sep=",")


if __name__ == "__main__":
    #get_results(years, table_name)
    race_weekend(races_2015, table_race)
