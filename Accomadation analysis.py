import json
from operator import itemgetter

# Load the data from the JSON string
data = json.loads('''[
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9553704?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816859&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=65561995&propertyName=Wighty%E2%80%99s+Beach+House",
        "Sleeps": "12",
        "Bedrooms": "4",
        "bathrooms": "2",
        "Avg per night": "400",
        "sleep to bed ratio": "3",
        "cost ratio": "33.33333333"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9631444?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816860&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=73117614&propertyName=Relaxing+Waterfront+Home+with+Beach+Vibe",
        "Sleeps": "10",
        "Bedrooms": "4",
        "bathrooms": "2",
        "Avg per night": "777",
        "sleep to bed ratio": "2.5",
        "cost ratio": "77.7"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9192169?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816859&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=32625546&propertyName=Charming+Island+Escape+Gold+Coast",
        "Sleeps": "10",
        "Bedrooms": "4",
        "bathrooms": "2",
        "Avg per night": "141",
        "sleep to bed ratio": "2.5",
        "cost ratio": "14.1"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9018585?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816859&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=33567031&propertyName=Beached+At+Straddie.",
        "Sleeps": "10",
        "Bedrooms": "4",
        "bathrooms": "2",
        "Avg per night": "341",
        "sleep to bed ratio": "2.5",
        "cost ratio": "34.1"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9027355?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816864&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=33942785&propertyName=Katrina%27s+Place+at+South+Stradbroke+Island+Waters",
        "Sleeps": "8",
        "Bedrooms": "4",
        "bathrooms": "2",
        "Avg per night": "550",
        "sleep to bed ratio": "2",
        "cost ratio": "68.75"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9100885?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816865&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=33908940&propertyName=Beach+Odyssey+South+Stradbroke+Island",
        "Sleeps": "12",
        "Bedrooms": "5",
        "bathrooms": "3",
        "Avg per night": "819",
        "sleep to bed ratio": "2.4",
        "cost ratio": "68.25"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p20001038?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816865&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=108311180&propertyName=Stylish+Waterfront+Escape%3A+The+Shed+on+South+Stradbroke+Island",
        "Sleeps": "11",
        "Bedrooms": "4",
        "bathrooms": "3",
        "Avg per night": "760",
        "sleep to bed ratio": "2.75",
        "cost ratio": "69.09090909"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9608249?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816866&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=71030051&propertyName=The+Islander",
        "Sleeps": "12",
        "Bedrooms": "5",
        "bathrooms": "3",
        "Avg per night": "874",
        "sleep to bed ratio": "2.4",
        "cost ratio": "72.83333333"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9929986?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816866&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=102505307&propertyName=South+Stradbroke+Island+Award+Winning+Luxury+Holiday+Rental",
        "Sleeps": "10",
        "Bedrooms": "5",
        "bathrooms": "3",
        "Avg per night": "1354",
        "sleep to bed ratio": "2",
        "cost ratio": "135.4"
    },
    {
        "accomadation ID in URL form": "https://www.stayz.com.au/holiday-rental/p9828875?dateless=true&x_pwa=1&rfrr=HSR&pwa_ts=1728618816859&referrerUrl=aHR0cHM6Ly93d3cuc3RheXouY29tLmF1L0hvdGVsLVNlYXJjaA%3D%3D&useRewards=false&adults=2&regionId=180064&destination=Gold+Coast%2C+Queensland%2C+Australia&destType=BOUNDING_BOX&latLong=-27.82575%2C153.41379&privacyTrackingState=CAN_TRACK&searchId=acfa2c8c-8537-49a0-937b-47b94d22ba00&sort=RECOMMENDED&userIntent=&expediaPropertyId=94651004&propertyName=Quiet+Island+Paradise%21",
        "Sleeps": "11",
        "Bedrooms": "4",
        "bathrooms": "4",
        "Avg per night": "1680",
        "sleep to bed ratio": "2.75",
        "cost ratio": "152.7272727"
    }
]''')


from operator import itemgetter

# Function to calculate the overall score (lower is better)
def calculate_score(item):
    sleep_to_bed_ratio = float(item['sleep to bed ratio'])
    cost_ratio = float(item['cost ratio'])
    return sleep_to_bed_ratio + cost_ratio

# Calculate original scores
for item in data:
    # Convert relevant fields to float
    item['Sleeps'] = float(item['Sleeps'])
    item['Bedrooms'] = float(item['Bedrooms'])
    item['Avg per night'] = float(item['Avg per night'])

    # Calculate current sleep to bed ratio
    current_sleep_to_bed_ratio = item['Sleeps'] / item['Bedrooms']
    item['original_sleep_to_bed_ratio'] = current_sleep_to_bed_ratio  # Store original ratio
    item['original_Sleeps'] = item['Sleeps']  # Store original Sleeps

    # Calculate original cost ratio
    item['original_cost_ratio'] = item['Avg per night'] / item['Sleeps']

    # Calculate original overall score
    item['original_score'] = calculate_score(item)

# Adjust Sleeps to ensure the sleep to bed ratio is 2.0 or lower and recalculate scores
for item in data:
    # Adjust Sleeps to ensure the sleep to bed ratio is 2.0 or lower
    if item['original_sleep_to_bed_ratio'] > 2.0:
        item['Sleeps'] = item['Bedrooms'] * 2.0
        item['sleep to bed ratio'] = item['Sleeps'] / item['Bedrooms']
    else:
        item['Sleeps'] = item['original_Sleeps']  # Keep original if already <= 2.0
        item['sleep to bed ratio'] = item['original_sleep_to_bed_ratio']

    # Calculate new cost ratio based on adjusted Sleeps
    item['cost ratio'] = item['Avg per night'] / item['Sleeps']

    # Calculate the overall score with adjusted values
    item['score'] = calculate_score(item)

# Sort data based on original and adjusted scores
sorted_original_data = sorted(data, key=itemgetter('original_score'))
sorted_adjusted_data = sorted(data, key=itemgetter('score'))

# Print all results based on original scores
print("All Accommodation Options (Original Scores):")
for i, item in enumerate(sorted_original_data, 1):
    print(f"\n{i}. {item['accomadation ID in URL form'].split('propertyName=')[-1].replace('+', ' ')}")
    print(f"   Sleeps: {item['original_Sleeps']}")
    print(f"   Bedrooms: {item['Bedrooms']}")
    print(f"   Bathrooms: {item['bathrooms']}")
    print(f"   Average per night: ${item['Avg per night']}")
    print(f"   Sleep-to-bed ratio: {item['original_sleep_to_bed_ratio']:.2f}")
    print(f"   Cost ratio: {item['original_cost_ratio']:.2f}")
    print(f"   Overall score: {item['original_score']:.2f}")

# Print all results based on adjusted scores
print("\nAll Accommodation Options (Adjusted Scores):")
for i, item in enumerate(sorted_adjusted_data, 1):
    print(f"\n{i}. {item['accomadation ID in URL form'].split('propertyName=')[-1].replace('+', ' ')}")
    print(f"   Adjusted Sleeps: {item['Sleeps']}")
    print(f"   Bedrooms: {item['Bedrooms']}")
    print(f"   Bathrooms: {item['bathrooms']}")
    print(f"   Average per night: ${item['Avg per night']}")
    print(f"   Adjusted Sleep-to-bed ratio: {item['sleep to bed ratio']:.2f}")
    print(f"   Adjusted Cost ratio: {item['cost ratio']:.2f}")
    print(f"   Overall score: {item['score']:.2f}")

# Calculate the average adjusted cost ratio
total_adjusted_cost_ratio = sum(item['cost ratio'] for item in data)
average_adjusted_cost_ratio = total_adjusted_cost_ratio / len(data)

# Print the average adjusted cost ratio
print(f"\nAverage Adjusted Cost per Worker for all properties: {average_adjusted_cost_ratio:.2f}")

# Calculate the total number of adjusted Sleeps
total_adjusted_sleeps = sum(item['Sleeps'] for item in data)

# Print the total number of adjusted Sleeps
print(f"\nTotal Adjusted Sleeps (number of available spaces for workers) for all properties: {total_adjusted_sleeps:.2f}")

# Calculate the median adjusted cost ratio
adjusted_cost_ratios = [item['cost ratio'] for item in data]
adjusted_cost_ratios.sort()

# Calculate the median
n = len(adjusted_cost_ratios)
if n % 2 == 0:
    median_adjusted_cost_ratio = (adjusted_cost_ratios[n // 2 - 1] + adjusted_cost_ratios[n // 2]) / 2
else:
    median_adjusted_cost_ratio = adjusted_cost_ratios[n // 2]

# Print the median adjusted cost ratio
print(f"\nMedian Adjusted Cost per worker for all properties: {median_adjusted_cost_ratio:.2f}")
