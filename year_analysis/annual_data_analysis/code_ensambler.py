# encoding utf-8 #

import winsound
import numpy as np
from year_analysis.annual_data_analysis import read_files
from year_analysis.annual_data_analysis import annual_analysis
from year_analysis.annual_data_analysis import diagrams
from year_analysis.annual_data_analysis import output_files
from constants import *


def main_code():
    """"""

    # We initialize the variables containing the pollutant's names and years
    pollutants_names = [no2, ozone, pm_10, pm_2p5]
    pollutant_big_name = [NO2, OZONE, PM10, PM2P5]
    years = [first_year, second_year, third_year, fourth_year, fifth_year]

    # We search for the root folder containing the files
    root = read_files.path_finder()

    # We start the iterations to analyze all the data
    for x in range(0, 4):  # Number of pollutant's types to analyze
        # Pollutant which is going to be analyzed for the five years of data collected
        name = pollutants_names[x]
        big_name = pollutant_big_name[x]

        print('Analyzing the', name, ' data!\n')

        # We initialize the array which will hold all the pollutant's concentration for each year
        complete_pollution = np.array([[0] * 151428, [0] * 151428, [0] * 151428, [0] * 151428, [0] * 151428],
                                      dtype=float)

        # We initialize the arrays where all the statistical coefficients for each pollutant will be hold
        annual_median = np.array([], dtype=float)  # Median
        annual_iqr = np.array([], dtype=float)  # Inter quantile range
        annual_yule_kendall = np.array([], dtype=float)  # Yule Kendall index
        annual_robust_kurtosis = np.array([], dtype=float)  # Robust kurtosis

        for y in range(0, 5):  # Number of years for each pollutant
            # We establish the year we are analyzing
            year = years[y]

            # We read the file
            lon, lat, pollution = read_files.read(root, name, year)
            # We assign it to the array that holds all the pollutant's concentration for each year
            for i in range(0, len(pollution)):
                complete_pollution[y, i] = pollution[i]

            # We compute the statistical coefficients for each year
            median, iqr, yule_kendall, robust_kurtosis = annual_analysis.statistics(pollution)
            # We assign it to the arrays we've made for each coefficient
            annual_median = np.append(annual_median, round(median, 4))
            annual_iqr = np.append(annual_iqr, round(iqr, 4))
            annual_yule_kendall = np.append(annual_yule_kendall, round(yule_kendall, 4))
            annual_robust_kurtosis = np.append(annual_robust_kurtosis, round(robust_kurtosis, 4))

        # We plot the boxplots and histograms with the parametric curves
        pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient, e_mod_coefficient = \
            diagrams.diagrams_representation(complete_pollution, name, big_name, years)

        # We write the output files
        output_files.output_and_closing(annual_median, annual_iqr, annual_yule_kendall, annual_robust_kurtosis,
                                        pearson_coefficient, d_coefficient, e_coefficient, d_mod_coefficient,
                                        e_mod_coefficient, name, years)

    # We emit a beep when all the data has been analyzed
    winsound.Beep(2500, 500)
    print('All data analyzed!')

    return


if __name__ == '__main__':
    main_code()
