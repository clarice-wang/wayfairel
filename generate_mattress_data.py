import pandas as pd
import numpy as np

current_suppliers_df = pd.read_csv('./mattress_suppliers.csv')

def generate_supplier_data(n):
    suppliers = []
    for i in range(n):
        avg_unit_price = np.random.randint(50, 15000)
        units_sold = np.random.randint(10, 10000)
        gross_revenue = units_sold * avg_unit_price
        total_costs = np.random.randint(5000, 1000000)
        gross_margin = (gross_revenue - total_costs) / gross_revenue
        supplier = {
            "Supplier": i,
            "Main Ship Speed": np.random.choice(["Large Parcel", "Small Parcel"]),
            "Lead Times": np.random.choice(["1-2 Weeks", "72 Hours", "2-3 Weeks", "24 Hours", "3-4 Weeks"]),
            "Average Unit Price": avg_unit_price,
            "# Units Sold": units_sold,
            "Gross Revenue": gross_revenue,
            "Total Costs": total_costs,
            "Gross Margin %": gross_margin,
            "Branded": np.random.choice(["Y", "N"]),
            "Brand Awareness": f"{int(np.clip(np.random.lognormal(mean=1.5, sigma=1.0), 0, 100))}%"
        }
        suppliers.append(supplier)
    return pd.DataFrame(suppliers)

example_suppliers_df = generate_supplier_data(1000)

example_suppliers_file_path = './mattress_suppliers_generated.csv'
example_suppliers_df.to_csv(example_suppliers_file_path, index=False)

example_suppliers_file_path
