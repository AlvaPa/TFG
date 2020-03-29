# encoding utf-8 #

import numpy as np


def statistics(pollution):
    """
    This function computes the statistical variables of the pollutant.
    :param pollution: Mean of each pollutant per location [ug/m^3]
    :return: median, iqr, yule_kendall, robust_kurtosis
    """

    # We compute the statistical variables
    # Median [ug/m^3]
    median = np.median(pollution)
    # Interquartile range [ug/m^3]
    iqr = np.quantile(pollution, 0.75) - np.quantile(pollution, 0.25)
    # Yule-Kendall index
    yule_kendall = \
        (np.quantile(pollution, 0.75) + np.quantile(pollution, 0.25) - 2 * np.median(pollution)) / iqr
    # Robust kurtosis
    robust_kurtosis = iqr / (2 * (np.quantile(pollution, 0.9) - np.quantile(pollution, 0.1)))

    return median, iqr, yule_kendall, robust_kurtosis
