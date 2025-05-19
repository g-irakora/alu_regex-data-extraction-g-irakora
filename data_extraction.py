#!/usr/bin/env python3
import re
# Regex patterns for various data types
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-\.]\d{3}[-\.]\d{4})'
time_pattern = r'(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s?(?:AM|PM|am|pm)|(?:2[0-3]|[01]?[0-9]):[0-5][0-9])'
hashtag_pattern = r'#[a-zA-Z0-9_]+'
currency_pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}'


def extract_data(text):

    results = {
        'emails': re.findall(email_pattern, text),
        'phone_numbers': re.findall(phone_pattern, text),
        'times': re.findall(time_pattern, text),
        'hashtags': re.findall(hashtag_pattern, text),
        'currency_amounts': re.findall(currency_pattern, text)
    }
    return results



# Testing the function

testing_text = """
Hi John,

Please email me at g.irakora@alustudent.com or irakoragasana@techlaunch.co.rw if you have any questions.  
You can also reach out by phone at (035) 456-7890 or 790-349-9200.

The meeting is scheduled for 10:30 AM, and the backup session will be at 14:45.  
Remember to bring the receipts, especially the one that shows the $1,299.99 laptop purchase.

Also, don’t forget to tag us using #TechLaunch2025 and #Innovation_Hub in your posts!

Best regards,  
Des
"""

results = extract_data(testing_text)

# Display the results
print("These are the Extracted patterns from our testing text: \n")
for data_type, items in results.items():
    print(f"\n{data_type.replace('_', ' ').title()}:")
    for item in items:
        print(f"  - {item}")