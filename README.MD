# Faza Mail

Faza Mail is a Python library that provides a simple interface for generating temporary email addresses and checking emails for specific content.

## Installation

Install Faza Mail using `pip`:

```bash
pip install fazamail
```

# Quick Start

```python
import fazamail

# Generate a temporary email address
address, token = fazamail.mail()

# Check email content
email_body = fazamail.check_mail(auth=token, url=1)
print(email_body)

# Check the first URL in the email
first_url = fazamail.check_mail(auth=token, url=2)
print("First URL in the email:", first_url)

# List all URLs in the email
all_urls = fazamail.check_mail(auth=token, url=3)
print("All URLs in the email:", all_urls)
```

# Features

- Email Generation: Quickly generate a temporary email address.
- Email Checking: Check emails for specific content, extract the first URL, or list all URLs.

# Usage

## Generating a temporary Email

```python
import fazamail

# Generate a temporary email address
address, token = fazamail.mail()

print("Temporary Email Address:", address)
print("Authentication Token:", token)
```

## Checking Email Content

```python
import fazamail

# Use the authentication token to check email content
email_body = fazamail.check_mail(auth=token, url=1)
print("Email Body:", email_body)

# Check the first URL in the email
first_url = fazamail.check_mail(auth=token, url=2)
print("First URL in the email:", first_url)

# List all URLs in the email
all_urls = fazamail.check_mail(auth=token, url=3)
print("All URLs in the email:", all_urls)
```