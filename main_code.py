# encoding utf-8 #

import winsound
import read_files
import monthly_analysis
import diagrams
import output_files
from constants import *


def main_code():
    """
    Main code of this program, where all the other scripts are called in order to perform the statistical analysis of
    the pollutant's concentration in England and Wales in the years interval 2007-2011.
    :return:
    """

    # We initialize the variables containing the pollutant's names and years
    pollutants_names = [no2, ozone, pm_10, pm_2p5]
    pollutant_big_name = [NO2, OZONE, PM10, PM2P5]
    years = [first_year, second_year, third_year, fourth_year, fifth_year]

    # We search for the root folder containing the files
    root = read_files.path_finder()

    # We start the iterations to analyze all the data
    for x in range(2, 4):
        # Pollutant which is going to be analyzed for the five years of data collected
        name = pollutants_names[x]
        big_name = pollutant_big_name[x]
        for y in range(0, 5):
            # We establish the year we are analyzing
            year = years[y]
            # We establish the days we have according to the year being leap or not
            if year == second_year:
                days = 366
            else:
                days = 365

            print('Analyzing the concentration of', name, 'in the year', year, '!\n')

            # We read the file
            data_index, data_lon, data_lat, data_month, data_pollutant = read_files.read(root, name, year)

            # We sort the data and compute the statistical variables
            sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution, monthly_median, monthly_iqr, \
                monthly_yule_kendall, monthly_robust_kurtosis = \
                monthly_analysis.monthly_analysis(data_index, data_lon, data_lat, data_month, data_pollutant, days)

            # We plot the boxplots and histograms
            diagrams.diagrams_representation(sorted_pollution, name, big_name, year)

            # We create the output files
            output_files.output_and_closing(sorted_index, sorted_lon, sorted_lat, sorted_month, sorted_pollution,
                                            monthly_median, monthly_iqr, monthly_yule_kendall, monthly_robust_kurtosis,
                                            name, year)

            # We emit a beep to show that this pollutant in the selected year has been analyzed
            winsound.Beep(2500, 500)

    # When the iterations have finished, the data analysis is finished as well
    print('All data analyzed!')

    return


if __name__ == '__main__':
    main_code()
