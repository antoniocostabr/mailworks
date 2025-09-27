"""
Example showing how to use different SMTP providers.

This example demonstrates how to configure the MailSender for various email providers.
"""

from mailworks import MailSender, AuthenticationError, SendError

def send_via_gmail():
    """Send email using Gmail SMTP (default configuration)."""
    print("=== Sending via Gmail ===")
    try:
        sender = MailSender(
            email="your.email@gmail.com",
            password="your_app_password",
            smtp_server="smtp.gmail.com",  # This is the default
            smtp_port=587  # This is the default
        )

        sender.test_connection()
        print("✓ Gmail connection successful!")

    except Exception as e:
        print(f"✗ Gmail failed: {e}")

def send_via_outlook():
    """Send email using Outlook/Hotmail SMTP."""
    print("\n=== Sending via Outlook ===")
    try:
        sender = MailSender(
            email="your.email@outlook.com",
            password="your_password",
            smtp_server="smtp-mail.outlook.com",
            smtp_port=587
        )

        sender.test_connection()
        print("✓ Outlook connection successful!")

    except Exception as e:
        print(f"✗ Outlook failed: {e}")

def send_via_yahoo():
    """Send email using Yahoo SMTP."""
    print("\n=== Sending via Yahoo ===")
    try:
        sender = MailSender(
            email="your.email@yahoo.com",
            password="your_app_password",  # Yahoo also requires app passwords
            smtp_server="smtp.mail.yahoo.com",
            smtp_port=587
        )

        sender.test_connection()
        print("✓ Yahoo connection successful!")

    except Exception as e:
        print(f"✗ Yahoo failed: {e}")

def send_via_custom_provider():
    """Send email using a custom SMTP provider."""
    print("\n=== Sending via Custom Provider ===")
    try:
        # Example with a generic business email provider
        sender = MailSender(
            email="your.email@yourdomain.com",
            password="your_password",
            smtp_server="mail.yourdomain.com",  # Your custom SMTP server
            smtp_port=587
        )

        sender.test_connection()
        print("✓ Custom provider connection successful!")

    except Exception as e:
        print(f"✗ Custom provider failed: {e}")

def main():
    print("Email Provider Configuration Examples")
    print("=" * 50)
    print("Note: Update the credentials before running!")

    # Test different providers
    send_via_gmail()
    send_via_outlook()
    send_via_yahoo()
    send_via_custom_provider()

    print("\n" + "=" * 50)
    print("Common SMTP Settings:")
    print("Gmail:        smtp.gmail.com:587")
    print("Outlook:      smtp-mail.outlook.com:587")
    print("Yahoo:        smtp.mail.yahoo.com:587")
    print("ProtonMail:   mail.protonmail.ch:587")
    print("Zoho:         smtp.zoho.com:587")
    print("SendGrid:     smtp.sendgrid.net:587")
    print("Amazon SES:   email-smtp.region.amazonaws.com:587")

if __name__ == "__main__":
    main()
