import matplotlib.pyplot as plt
import csv

def visualize_ratios():
    strategies = []
    boys = []
    girls = []

    with open("outputs/gender_ratios.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            strategies.append(row[0])
            boys.append(int(row[1]))
            girls.append(int(row[2]))

    x = range(len(strategies))
    plt.bar(x, boys, label="Boys", alpha=0.7)
    plt.bar(x, girls, label="Girls", alpha=0.7, bottom=boys)
    plt.xticks(x, strategies, rotation=45)
    plt.ylabel("Total Children")
    plt.title("Gender Ratios by Stopping Strategy")
    plt.legend()
    plt.savefig("outputs/visualization.png")

visualize_ratios()
