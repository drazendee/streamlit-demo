import csv
import random
import os

output_root = os.getenv('VH_OUTPUTS_DIR', '.outputs')

possible_categories = [
    "promising",
    "loyal",
    "churn"
]

fields = ["customerid", "category"]
rows = []

customerids = random.sample(range(1000), 50)

for customerid in customerids:
    rows.append([customerid, random.choice(possible_categories)])

with open(os.path.join(output_root, "customer_loyalty.csv"), 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)