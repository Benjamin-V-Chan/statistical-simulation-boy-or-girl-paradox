# statistical-simulation-boy-or-girl-paradox

# Boy or Girl Paradox Simulation

## Project Overview

This project simulates and analyzes the Boy or Girl Paradox, a famous probability problem exploring how stopping rules influence gender distributions in families. We implement multiple family-planning strategies and examine their statistical properties using Monte Carlo simulations, chi-square tests, and data visualization.



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