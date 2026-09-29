import json

import pandas as pd
import yaml

# Step 1: Read settings
with open("config.yml") as f:
    config = yaml.safe_load(f)

max_days = config["max_days_since_calibration"]
output_file = config["output_file"]

# Step 2: Read data
calibrations = pd.read_csv("calibrations.csv")
sensors = pd.read_excel("sensors.xlsx")

# Step 3: Merge the data
merged_data = sensors.merge(calibrations, on="sensor_id")

# Step 4: Filter sensors that have not been calibrated within the max_days
overdue_sensors = merged_data[merged_data["days_since_calibration"] > max_days]

# Step 5: Save the result to a JSON file
records = overdue_sensors.to_dict(orient="records")
with open(output_file, "w") as f:
    json.dump(records, f, indent=2)
    






