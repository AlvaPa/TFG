# encoding utf-8 #

import winsound
import numpy as np
from month_analysis.month_surface import read_files
from month_analysis.month_surface import counter
from month_analysis.month_surface import surface_maps
from month_analysis.month_surface import output_surface_files
from constants import *


def main_code():
    """"""

    # We initialize the variables containing the pollutant's names and years
    pollutants_names = [no2, ozone, pm_10, pm_2p5]
    pollutant_big_name = [NO2, OZONE, PM10, PM2P5]
    years = [first_year, second_year, third_year, fourth_year, fifth_year]
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # We search for the root folder containing the files
    root = read_files.path_finder()

    # We start the iterations to process the data
    for x in range(0, 4):
        name = pollutants_names[x]
        big_name = pollutant_big_name[x]
        for y in range(0, 5):
            # We establish the year we are analyzing
            year = years[y]
            # We initialize the variable which will hold the surface percentages of the whole year
            total_surface_percentage = np.array([[0] * 12, [0] * 12, [0] * 12, [0] * 12, [0] * 12, [0] * 12,
                                                 [0] * 12, [0] * 12, [0] * 12, [0] * 12, [0] * 12, [0] * 12,
                                                 [0] * 12, [0] * 12, [0] * 12, [0] * 12], dtype=float)

            print('Analyzing the surface data of', name, 'in the year', year, '!\n')

            for z in range(0, 12):
                # We establish the month we are processing
                month = months[z]

                # We read the file
                lon, lat, pollution = read_files.read(root, name, year, month)

                # We perform the calculations to classify the concentrations and study the surface distribution
                surface_percentage, classified_lon, classified_lat = counter.counter(lon, lat, pollution, name)

                # We plot the map
                surface_maps.maps_plotting(classified_lon, classified_lat, name, big_name, year, z)

                # We assign the surface percentage to the one that saves for the whole year
                for t in range(0, len(surface_percentage)):
                    total_surface_percentage[t, z] = surface_percentage[t]

            # We save the data in the output
            output_surface_files.output_and_closing(total_surface_percentage, name, year, months)

        # We emit a beep to show that this pollutant in the selected year has been analyzed
        winsound.Beep(2500, 500)

    return


if __name__ == '__main__':
    main_code()
