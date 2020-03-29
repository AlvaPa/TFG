# encoding utf-8 #

import winsound
import numpy as np
from year_analysis.annual_surface import read_files
from year_analysis.annual_surface import counter
from year_analysis.annual_surface import surface_maps
from year_analysis.annual_surface import output_files
from constants import *


def main_code():
    """"""

    # We initialize the variables containing the pollutant's names and years
    pollutants_names = [no2, ozone, pm_10, pm_2p5]
    pollutant_big_name = [NO2, OZONE, PM10, PM2P5]
    years = [first_year, second_year, third_year, fourth_year, fifth_year]

    # We search for the root folder containing the files
    root = read_files.path_finder()

    # We start the iterations to process the data
    for x in range(0, 4):
        name = pollutants_names[x]
        big_name = pollutant_big_name[x]
        # We initialize the variable which will hold the surface percentages of the whole year
        total_surface_percentage = np.array([[0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5,
                                             [0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5,
                                             [0] * 5, [0] * 5, [0] * 5, [0] * 5], dtype=float)

        print('Analyzing the surface data of', name, '!\n')
        for y in range(0, 5):
            # We establish the year we are analyzing
            year = years[y]

            # We read the file
            lon, lat, pollution = read_files.read(root, name, year)

            # We perform the calculations to classify the concentrations and study the surface distribution
            surface_percentage, classified_lon, classified_lat = counter.counter(lon, lat, pollution, name)

            # We plot the map
            surface_maps.maps_plotting(classified_lon, classified_lat, name, big_name, year)

            # We assign the surface percentage to the one that saves for the whole year
            for t in range(0, len(surface_percentage)):
                total_surface_percentage[t, y] = surface_percentage[t]

        # We save the data in the output
        output_files.output_and_closing(total_surface_percentage, name, years)

        # We make the color legend
        surface_maps.legend_maker(name, big_name)

    # We emit a beep to show that the code has ended
    winsound.Beep(2500, 500)

    return


if __name__ == '__main__':
    main_code()
