"""
Basic email sending example using environment variables.

Before running this example:
1. Set environment variables:
   export GMAIL_EMAIL="your.email@gmail.com"
   export GMAIL_PASSWORD="your_app_password"

2. Install the package:
   pip install -e .
"""

import os
from email_sender import GmailSender, AuthenticationError, SendError

def main():
    try:
        # Create sender using environment variables
        sender = GmailSender()
        
        # Test connection first
        print("Testing connection to Gmail...")
        sender.test_connection()
        print("✓ Connection successful!")
        
        # Send a simple email
        print("Sending email...")
        success = sender.send_simple_email(
            to_email="recipient@example.com",  # Replace with actual recipient
            subject="Test Email from Python",
            message="Hello! This is a test email sent from Python using the email-sender package."
        )
        
        if success:
            print("✓ Email sent successfully!")
        else:
            print("✗ Failed to send email")
            
    except AuthenticationError as e:
        print(f"✗ Authentication failed: {e}")
        print("Make sure you're using an App Password, not your regular Gmail password.")
        print("See: https://support.google.com/accounts/answer/185833")
        
    except SendError as e:
        print(f"✗ Failed to send email: {e}")
        
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    main()