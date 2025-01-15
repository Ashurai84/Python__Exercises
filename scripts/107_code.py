#  109. Write a script that extracts all email addresses from a given string using the re module.
import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

# Example usage
text = "Contact us at support@example.com and info@example.org for more info."
emails = extract_emails(text)
print("Extracted email addresses:", emails)
