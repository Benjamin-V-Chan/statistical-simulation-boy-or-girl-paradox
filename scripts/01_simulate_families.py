import random
import csv

def simulate_families(num_families=10000):
    strategies = {
        "first_child": lambda family: len(family) == 1,
        "stop_at_boy": lambda family: "B" in family,
        "two_children": lambda family: len(family) == 2,
        "stop_at_girl": lambda family: "G" in family,
    }
    
    results = {strategy: [] for strategy in strategies}

    for _ in range(num_families):
        for strategy, stop_condition in strategies.items():
            family = []
            while not stop_condition(family):
                family.append(random.choice(["B", "G"]))
            results[strategy].append(family)

    with open("outputs/families_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Strategy", "Family"])
        for strategy, families in results.items():
            for family in families:
                writer.writerow([strategy, "".join(family)])

simulate_families()
