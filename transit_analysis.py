import numpy as np
import matplotlib.pyplot as plt

# ---  Public Transit Ridership Analysis Project ---

# Define the set of transit routes
route_names = np.array(['Route 101 (Downtown)', 'Route 202 (Suburban)', 
                        'Route 303 (University)', 'Route 404 (Industrial)', 
                        'Route 505 (Hospital)'])

# Simulate 7 days of passenger counts for the 5 routes.
# np.random.seed(42) ensures the random data is the same every time you run it.
np.random.seed(42) 
daily_ridership_data = np.array([
    np.random.randint(1500, 3000, 5), 
    np.random.randint(1400, 2800, 5), 
    np.random.randint(1600, 3100, 5), 
    np.random.randint(1300, 2700, 5), 
    np.random.randint(1800, 3500, 5), 
    np.random.randint(800, 1500, 5),  
    np.random.randint(600, 1200, 5)   
])

# Crucially, we artificially increase the load for Route 303 (index 2) 
# to simulate a high-demand route and ensure a meaningful result.
daily_ridership_data[:, 2] += 1500 

# ---  Data Analysis (NumPy) ---

# 1. Calculate the total ridership for each route over the week (sum along the days/axis=0)
total_ridership_per_route = np.sum(daily_ridership_data, axis=0)

# 2. Calculate the average daily ridership for each route
average_ridership_per_route = np.mean(daily_ridership_data, axis=0)

# 3. Identify the busiest route index
busiest_route_index = np.argmax(total_ridership_per_route)
busiest_route_name = route_names[busiest_route_index]
busiest_route_total = total_ridership_per_route[busiest_route_index]

# ---  Data Visualization (Matplotlib) ---

# Create a bar chart for average daily ridership
plt.figure(figsize=(10, 6))

bars = plt.bar(route_names, average_ridership_per_route, color='skyblue')

# Highlight the busiest route
bars[busiest_route_index].set_color('salmon')

plt.title('Average Daily Ridership Per Transit Route', fontsize=16)
plt.xlabel('Transit Route', fontsize=12)
plt.ylabel('Average Passengers', fontsize=12)

# Add value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 50, 
             f'{int(yval):,}', ha='center', va='bottom')

plt.xticks(rotation=15, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('screenshots/analysis_chart.png') # Saves the chart to the required directory!
plt.show() 

# --- Console Output ---
print(f"Busiest Route Identified: {busiest_route_name} (Total Weekly Passengers: {busiest_route_total:,})")
print(f"Saved visualization to: screenshots/analysis_chart.png")
