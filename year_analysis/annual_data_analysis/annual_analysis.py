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
    median = round(np.median(pollution), 2)
    # Interquartile range [ug/m^3]
    iqr = round(np.quantile(pollution, 0.75) - np.quantile(pollution, 0.25), 2)
    # Yule-Kendall index
    yule_kendall = \
        round((np.quantile(pollution, 0.75) + np.quantile(pollution, 0.25) - 2 * np.median(pollution)) / iqr, 2)
    # Robust kurtosis
    robust_kurtosis = round(iqr / (2 * (np.quantile(pollution, 0.9) - np.quantile(pollution, 0.1))), 2)

    return median, iqr, yule_kendall, robust_kurtosis
