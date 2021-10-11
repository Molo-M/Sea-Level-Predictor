import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import stats


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(22, 18))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    sec_yr = list()
    for i in range(1880, 2051):
        sec_yr.append(i)
    sec_yr = pd.Series(sec_yr)
    plt.plot(sec_yr, res.intercept + res.slope * sec_yr, 'r')

    # Create second line of best fit
    mask = df['Year'] >= 2000
    n_df = df[mask]

    res_2 = stats.linregress(n_df['Year'], n_df['CSIRO Adjusted Sea Level'])

    thrd_yr = list()
    for i in range(2000, 2051):
        thrd_yr.append(i)
    thrd_yr = pd.Series(thrd_yr)

    plt.plot(thrd_yr, res_2.intercept + res_2.slope * thrd_yr, 'black')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    plt.title("Rise in Sea Level")

    plt.legend(['Prediction: 1880-2050', 'Prediction: 2000-2050', 'Original Data: 1880-2013'])

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


print(draw_plot())
