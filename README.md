# EGB273-Accommadation Solver (!!warning!! code is trash, don't @me)
### Just copy and paste whole python code and run it, idk what I am doing here lol
---

# Accommodation Analysis

This Python script performs an analysis of accommodation options based on a set of criteria, calculating scores that help determine the best choices for staying. The script processes a JSON dataset containing various accommodation attributes such as Sleeps(number of people staying), Bedrooms, Bathrooms, and Average nightly price.

## Functionality

### 1. **Score Calculation**
- **Overall Score:** The script calculates an overall score for each accommodation option based on two main metrics:
  - **Sleep-to-Bed Ratio:** This ratio is calculated as `Sleeps / Bedrooms`. It measures how well the accommodation can accommodate guests relative to the number of available beds.
  - **Cost Ratio:** This is calculated as `Average per night / Sleeps`, representing the cost per person for the accommodation.

### 2. **Adjustments for Analysis**
- If an accommodation's sleep-to-bed ratio exceeds 2.0, the script adjusts the number of Sleeps to ensure the ratio is at most 2.0. This is done by setting `Sleeps` to `2 * Bedrooms`.
- After adjusting Sleeps, the cost ratio and overall score are recalculated to reflect the new values.

### 3. **Results Output**
- Finally, the script sorts the accommodations based on their original and adjusted scores and prints detailed information for all options, including:
  - Accommodation ID
  - Adjusted Sleeps
  - Number of Bedrooms and Bathrooms
  - Average price per night
  - Sleep-to-Bed ratio
  - Cost ratio
  - Overall score
    

## Usage
Copy and paste all code into Visual Studio. Run that shit. 

---


