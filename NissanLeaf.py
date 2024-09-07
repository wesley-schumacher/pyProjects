import numpy as np
import matplotlib.pyplot as plt

# Costs data
years = np.arange(0, 6, 1)  # 10-year period

# Nissan Leaf costs
nissan_leaf_purchase_price = 2500  # USD
nissan_leaf_maintenance = 50  # USD/year
nissan_leaf_insurance = 800  # USD/year
nissan_leaf_electricity_cost = 0.12  # USD/kWh
nissan_leaf_miles_per_kwh = 4  # Miles/kWh
nissan_leaf_annual_miles = 8000  # Miles driven per year
nissan_leaf_annual_electricity_cost = (nissan_leaf_annual_miles / nissan_leaf_miles_per_kwh) * nissan_leaf_electricity_cost

# Cumulative costs for Nissan Leaf (yearly)
nissan_leaf_cumulative_cost = [nissan_leaf_purchase_price]  # Initial purchase price
for i in range(1, len(years)):
    annual_cost = nissan_leaf_maintenance + nissan_leaf_insurance + nissan_leaf_annual_electricity_cost
    nissan_leaf_cumulative_cost.append(nissan_leaf_cumulative_cost[-1] + annual_cost)

# Another car costs (e.g., a Toyota Corolla)
corolla_purchase_price = 0  # USD
corolla_maintenance = 800  # USD/year
corolla_insurance = 800  # USD/year
corolla_gas_price_per_gallon = 3.50  # USD/gallon
corolla_miles_per_gallon = 20  # Miles/gallon
corolla_annual_miles = 6000  # Miles driven per year
corolla_annual_gas_cost = (corolla_annual_miles / corolla_miles_per_gallon) * corolla_gas_price_per_gallon

# Cumulative costs for Toyota Corolla (yearly)
corolla_cumulative_cost = [corolla_purchase_price]  # Initial purchase price
for i in range(1, len(years)):
    annual_cost = corolla_maintenance + corolla_insurance + corolla_annual_gas_cost
    corolla_cumulative_cost.append(corolla_cumulative_cost[-1] + annual_cost)

# Plotting the costs
plt.figure(figsize=(10, 6))
plt.plot(years, nissan_leaf_cumulative_cost, label="Nissan Leaf", marker='o')
plt.plot(years, corolla_cumulative_cost, label="Nissa Frontier", marker='s')

# Add labels and title
plt.title("Cumulative Cost Comparison: Nissan Leaf vs Toyota Corolla (10 years)")
plt.xlabel("Years")
plt.ylabel("Cumulative Cost (USD)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

