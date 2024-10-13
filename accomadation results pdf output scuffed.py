import pandas as pd

# Data for the table
data = {
    "Rank": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Accommodation Name": [
        "Beached At Straddie", 
        "Wighty's Beach House", 
        "Katrina's Place at South Stradbroke Island Waters", 
        "Beach Odyssey South Stradbroke Island", 
        "The Islander", 
        "Stylish Waterfront Escape: The Shed on South Stradbroke", 
        "Relaxing Waterfront Home with Beach Vibe", 
        "South Stradbroke Island Award Winning Luxury Holiday Rental", 
        "Quiet Island Paradise"
    ],
    "Adjusted Sleeps": [8.0, 8.0, 8.0, 10.0, 10.0, 8.0, 8.0, 10.0, 8.0],
    "Bedrooms": [4.0, 4.0, 4.0, 5.0, 5.0, 4.0, 4.0, 5.0, 4.0],
    "Bathrooms": [2, 2, 2, 3, 3, 3, 2, 3, 4],
    "Avg. per Night ($)": [341.0, 400.0, 550.0, 819.0, 874.0, 760.0, 777.0, 1354.0, 1680.0],
    "Sleep-to-Bed Ratio": [2.00] * 9,
    "Cost Ratio": [42.62, 50.00, 68.75, 81.90, 87.40, 95.00, 97.12, 135.40, 210.00],
    "Overall Score": [44.62, 52.00, 70.75, 83.90, 89.40, 97.00, 99.12, 137.40, 212.00]
}

# Create DataFrame
df = pd.DataFrame(data)

# Placeholder for file location
file_location = r"file_location_for_excelfile_output"


# Write DataFrame to Excel file
df.to_excel(file_location, index=False)

print(f"Table written to {file_location}")
