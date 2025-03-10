# statistical-simulation-boy-or-girl-paradox

# Boy or Girl Paradox Simulation

## Project Overview

This project simulates and analyzes the Boy or Girl Paradox, a famous probability problem exploring how stopping rules influence gender distributions in families. We implement multiple family-planning strategies and examine their statistical properties using Monte Carlo simulations, chi-square tests, and data visualization.

### **Mathematical Foundation**

Let $X$ represent a child's gender, where:
- $P(X = B) = p$
- $P(X = G) = 1 - p$

Typically, $p \approx 0.512$ due to biological birth biases.

#### **Expected Gender Ratio**

Given a stopping rule $S$, the expected number of boys and girls follows:
$$\[E[B] = \sum_{n=1}^{\infty} n P(B_n | S)\]$$
$$\[E[G] = \sum_{n=1}^{\infty} n P(G_n | S)\]$$
where $P(B_n | S)$ and $P(G_n | S)$ denote the probability of the $n$-th child being a boy or girl under stopping rule $S$.

#### **Stopping Rule Effects**

Consider the stopping rule **"Stop at first boy"**:

If each child is independently born male with probability $p$, the probability mass function (PMF) of family size follows a geometric distribution:
$$\[P(N = k) = (1 - p)^{k-1} p\]$$
with an expected family size of:
$$\[E[N] = \frac{1}{p}\]$$

This leads to an expected gender ratio of:
$$\[E[B] = 1, \quad E[G] = \frac{1-p}{p}\]$$

For **"Stop at first girl"**, symmetry yields:
$$\[E[G] = 1, \quad E[B] = \frac{p}{1-p}\]$$

### **Statistical Testing**

We use a **Chi-Square Goodness of Fit Test** to compare observed gender distributions to expected values:
$$\[\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}\]$$
where $O_i$ and $E_i$ are observed and expected frequencies for gender counts.

If $p < 0.05$, we reject the null hypothesis that the observed ratios follow expected distributions.

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_simulate_families.py   # Runs the family simulation
│   ├── 02_analyze_gender_ratios.py # Analyzes gender ratios
│   ├── 03_visualize_results.py  # Generates graphs and visualization
│   ├── 04_statistical_tests.py  # Runs statistical significance tests
│   ├── 05_compare_strategies.py  # Compares different stopping strategies
├── outputs/  # Stores CSVs and graphs
│   ├── families_data.csv
│   ├── gender_ratios.csv
│   ├── visualization.png
│   ├── statistical_tests.txt
│   ├── strategy_comparison.csv
├── requirements.txt
└── README.md
```

## Usage

### **1. Setup the Project:**

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```sh
pip install -r requirements.txt
```

### **2. Simulate Families**
Generate synthetic family data based on different stopping rules.
```sh
python scripts/01_simulate_families.py
```
Output: `outputs/families_data.csv`

### **3. Analyze Gender Ratios**
Compute gender distributions and birth ratios.
```sh
python scripts/02_analyze_gender_ratios.py
```
Output: `outputs/gender_ratios.csv`

### **4. Visualize Results**
Generate bar charts comparing gender ratios.
```sh
python scripts/03_visualize_results.py
```
Output: `outputs/visualization.png`

### **5. Perform Statistical Tests**
Test whether observed gender ratios significantly differ from expected distributions.
```sh
python scripts/04_statistical_tests.py
```
Output: `outputs/statistical_tests.txt`

### **6. Compare Stopping Strategies**
Compare average family sizes across strategies.
```sh
python scripts/05_compare_strategies.py
```
Output: `outputs/strategy_comparison.csv`

## Requirements
- Python 3.x
- Required libraries (install via `pip install -r requirements.txt`):
  - `numpy`
  - `matplotlib`
  - `scipy`
  - `pandas`