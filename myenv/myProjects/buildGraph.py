import matplotlib.pyplot as plt
from openpyxl import load_workbook
import click

@click.command()
@click.option("--file", default="sin.xlsx", help="Read file")
def build_graph(file):
    x = list()
    y = list()
    wb = load_workbook(file)
    sheet_ranges = wb['sin']
    column_a = sheet_ranges['A']
    column_b = sheet_ranges['B']
    for i in range(len(column_a)-1):
        x.append(column_a[i+1].value)
    for i in range(len(column_b)-1):
        y.append(column_b[i+1].value)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('t')
    ax.set_ylabel('U')
    plt.show()

if __name__ == "__main__":
    build_graph()