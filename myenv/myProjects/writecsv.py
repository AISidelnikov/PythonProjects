import pandas as pd
import numpy as np
import click

@click.command()
@click.option("-f", default=1, help="The frequency of the signal")
@click.option("-fs", default=1, help="Sample rate")
def create_file(f, fs):
    x = np.arange(fs)
    y = np.sin(2*np.pi * f * (x/fs))

    df = pd.DataFrame.from_dict({'x': x, 'y': y})

    df.to_csv("sin.csv")

    df2 = pd.read_csv('sin.csv')
    print(df)


if __name__ == '__main__':
    create_file()