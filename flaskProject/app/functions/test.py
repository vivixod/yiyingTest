import numpy as np
import pandas as pd
from KFRAD import KFRAD

# def generate_custom_dataset(num_samples=1000, num_attributes=2, noise_level=0.1, anomaly_fraction=0.05):
#     # Generate correlated attribute
#     correlated_attribute = np.random.rand(num_samples)
#
#     # Generate uncorrelated attribute
#     uncorrelated_attribute = np.random.rand(num_samples)
#
#     # Introduce correlation between attributes
#     correlated_attribute += 0.8 * uncorrelated_attribute
#
#     # Normalize attributes
#     correlated_attribute /= np.max(correlated_attribute)
#     uncorrelated_attribute /= np.max(uncorrelated_attribute)
#
#     # Add noise to the attributes
#     correlated_attribute += np.random.normal(0, noise_level, num_samples)
#     uncorrelated_attribute += np.random.normal(0, noise_level, num_samples)
#
#     # Create a DataFrame with the generated data
#     data = pd.DataFrame(
#         {'Correlated_Attribute': correlated_attribute, 'Uncorrelated_Attribute': uncorrelated_attribute})
#
#     # Introduce anomalies
#     num_anomalies = int(anomaly_fraction * num_samples)
#     anomaly_indices = np.random.choice(num_samples, num_anomalies, replace=False)
#
#     # Add anomalies by making correlated_attribute values higher
#     data.loc[anomaly_indices, 'Correlated_Attribute'] += 2 * noise_level
#
#     return data
#
#
# # Example usage:
# custom_dataset = generate_custom_dataset(num_samples=1000, num_attributes=2, noise_level=0.1, anomaly_fraction=0.05)
# print(custom_dataset.head())
data = np.array([
    [1.2, 2.3, 3.1],
    [4.5, 6.7, 5.4],
    [0.9, 1.8, 2.7],
    [3.2, 2.5, 4.8],
    [5.6, 4.3, 6.9]
])
print(data)
print(KFRAD(data, 0.02))
