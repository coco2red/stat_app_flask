import statistics
import scipy.stats as stats
import math

def calculate_stats(ages):
    if not ages:
        return {
            'mean': None,
            'median': None,
            'mode': None,
            'range': None,
            'variance': None,
            'std_dev': None,
            'skewness': None,
            'kurtosis': None,
            'conf_interval': None,
            'ages': ages
        }

    mean_age = statistics.mean(ages)
    median_age = statistics.median(ages)

    try:
        mode_age = statistics.mode(ages)
    except statistics.StatisticsError:
        mode_age = "No mode"

    range_age = max(ages) - min(ages)
    variance_age = statistics.variance(ages)
    std_dev_age = statistics.stdev(ages)

    # Skewness (using scipy.stats)
    skewness_age = stats.skew(ages)

    # Kurtosis (using scipy.stats)
    kurtosis_age = stats.kurtosis(ages)

    # Confidence Interval for the mean (95% confidence level)
    n = len(ages)
    std_err = std_dev_age / math.sqrt(n)
    conf_interval = stats.norm.interval(0.95, loc=mean_age, scale=std_err)

    return {
        'mean': round(mean_age, 2),
        'median': median_age,
        'mode': mode_age,
        'range': range_age,
        'variance': round(variance_age, 2),
        'std_dev': round(std_dev_age, 2),
        'skewness': round(skewness_age, 2),
        'kurtosis': round(kurtosis_age, 2),
        'conf_interval': (round(conf_interval[0], 2), round(conf_interval[1], 2)),
        'ages': ages  # Pass the ages back for the table
    }
