#  Public Transit Ridership Analysis and Visualization

##  Problem Definition
This project addresses the real-world need of a city's public transit authority to **analyze passenger demand** across various routes. Understanding which routes are busiest (peak demand) is crucial for efficient resource allocation, scheduling, and infrastructure planning.

##  Objectives
1.  **Simulate** weekly passenger data for five distinct transit routes using **NumPy**.
2.  **Calculate** the total and average daily ridership for each route.
3.  **Identify** the single busiest route based on weekly totals.
4.  **Visualize** the average daily ridership using a **Matplotlib** bar chart for clear decision-making.

##  Applied Concepts
| Course Concept | Library/Implementation |
| :--- | :--- |
| Data Representation | NumPy arrays (`daily_ridership_data`) |
| Data Manipulation | NumPy functions (`np.sum`, `np.mean`, `np.argmax`) |
| Visualization | Matplotlib (`plt.bar`, `plt.title`) |
| Algorithm Development | Structured calculation and decision logic |

##  Execution Steps
1.  **Install** the necessary libraries: `pip install numpy matplotlib`
2.  **Run** the script: `python transit_analysis.py`
3.  The script will generate the bar chart and save it automatically to the `./screenshots` directory.

##  Key Findings
The analysis, based on simulated but realistic data, identified **Route 303 (University)** as the busiest route. This finding suggests that this route requires the highest priority for additional frequency or capacity upgrades to better serve the public.


OUTPUT IMAGES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

<img width="797" height="503" alt="Screenshot 2025-11-25 205615" src="https://github.com/user-attachments/assets/9e0e4ebb-926b-4ed0-9cf5-2986dfd75f5c" />
<img width="1308" height="740" alt="image" src="https://github.com/user-attachments/assets/f7358fe9-ad4f-42a5-8c02-9e8283ab97cf" />

