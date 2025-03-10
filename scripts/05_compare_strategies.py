import csv

def compare_strategies():
    data = {}

    with open("outputs/families_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for strategy, family in reader:
            if strategy not in data:
                data[strategy] = []
            data[strategy].append(len(family))

    with open("outputs/strategy_comparison.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Strategy", "Average Family Size"])
        for strategy, families in data.items():
            writer.writerow([strategy, sum(families) / len(families)])

compare_strategies()
