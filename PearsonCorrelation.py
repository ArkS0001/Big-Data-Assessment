import numpy as np
from scipy.stats import pearsonr

# Coffee consumption data
coffee_consumption = np.array([6.05, 4.20, 6.52, 3.15, 5.36])

# Liver cancer occurrences data
liver_cancer_occurrences = np.array([78.1, 6.3, 20.6, 73.1, 22.7])

# Calculate Pearson correlation coefficient
correlation_coefficient, _ = pearsonr(coffee_consumption, liver_cancer_occurrences)
print("Pearson Correlation Coefficient:", correlation_coefficient)

    # 1 indicates a perfect positive linear relationship,
    # -1 indicates a perfect negative linear relationship,
    # 0 indicates no linear relationship.
