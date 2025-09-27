"""
Basic email sending example using environment variables.

Before running this example:
1. Set environment variables:
   export EMAIL="your.email@anyprovider.com"
   export PASSWORD="your_app_password"

   # Optional: Configure custom SMTP server (defaults to Gmail)
   export SMTP_SERVER="smtp.anyprovider.com"
   export SMTP_PORT="587"

2. Install the package:
   pip install -e .
"""

import os
from mailworks import MailSender, AuthenticationError, SendError

def main():
    try:
        # Create sender using environment variables
        # This will work with any SMTP provider that supports STARTTLS on port 587
        sender = MailSender()

        # Test connection first
        print(f"Testing connection to {sender.smtp_server}:{sender.smtp_port}...")
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
        print("Make sure you're using the correct credentials.")
        print("For Gmail, use an App Password: https://support.google.com/accounts/answer/185833")

    except SendError as e:
        print(f"✗ Failed to send email: {e}")

    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    main()
