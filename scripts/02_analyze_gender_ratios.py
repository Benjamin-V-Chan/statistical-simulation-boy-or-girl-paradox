import csv
from collections import Counter

def compute_gender_ratios():
    gender_counts = {}

    with open("outputs/families_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        
        for strategy, family in reader:
            males = family.count("B")
            females = family.count("G")
            if strategy not in gender_counts:
                gender_counts[strategy] = {"B": 0, "G": 0}
            gender_counts[strategy]["B"] += males
            gender_counts[strategy]["G"] += females

    with open("outputs/gender_ratios.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Strategy", "Total Boys", "Total Girls", "Ratio (Boys/Girls)"])
        for strategy, counts in gender_counts.items():
            ratio = counts["B"] / counts["G"] if counts["G"] else "inf"
            writer.writerow([strategy, counts["B"], counts["G"], ratio])

compute_gender_ratios()
