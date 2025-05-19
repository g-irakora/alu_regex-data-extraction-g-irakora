# Regex Data Extractor

## Overview

**Regex Data Extractor** is a Python script that extracts specific types of data from text using regular expressions (regex).

- Email addresses
- Phone numbers
- Time formats (12-hour and 24-hour)
- Hashtags
- Currency amounts in USD

The script defines and uses regular expressions to search for these patterns in a given input string, then displays the results in a readable format.

---

## Features

Extracts and displays:
- **Emails** (e.g., `example@domain.com`)  
- **Phone Numbers** (e.g., `(123) 456-7890`, `123-456-7890`)  
- **Times** in both 12-hour (e.g., `10:30 AM`) and 24-hour (e.g., `14:45`) formats  
- **Hashtags** (e.g., `#TechLaunch2025`)  
- **Currency** in USD format with commas and decimals (e.g., `$1,299.99`)  

---

## Setup Instructions

### 1. Clone the Repository

You can clone the repository using Git:

```bash
git clone https://github.com/g-irakora/alu_regex-data-extraction-g-irakora.git
cd alu_regex-data-extraction-g-irakora/

```
### 2. Run the Script

```bash
python My_Regex_project.py
```

### 3. Sample
These are the Extracted patterns from our testing text: 

Emails:
  - john.doe123@example.com
  - jane_doe@company.co.uk

Phone Numbers:
  - (123) 456-7890
  - 987-654-3210

Times:
  - 10:30 AM
  - 14:45

Hashtags:
  - #TechLaunch2025
  - #Innovation_Hub

Currency Amounts:
  - $1,299.99