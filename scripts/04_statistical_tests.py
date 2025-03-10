import scipy.stats as stats
import csv

def chi_square_test():
    observed = []
    strategies = []

    with open("outputs/gender_ratios.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            strategies.append(row[0])
            observed.append([int(row[1]), int(row[2])])  # [Boys, Girls]

    expected_ratio = 1.05  # Expected slight bias for boys
    expected = [[sum(pair) * expected_ratio / (1 + expected_ratio), sum(pair) / (1 + expected_ratio)] for pair in observed]

    chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)

    with open("outputs/statistical_tests.txt", "w") as file:
        file.write("Chi-Square Test Results:\n")
        for i, strategy in enumerate(strategies):
            file.write(f"{strategy}: Chi2={chi2_stat[i]:.4f}, p={p_value[i]:.4f}\n")

chi_square_test()
