"""
Example showing how to use MailSender with internal/corporate SMTP servers
that don't require authentication.

This is common in corporate environments where the SMTP server is configured
to relay emails from trusted internal hosts without requiring authentication.
"""

from mailworks import MailSender, SendError

def main():
    print("=== Internal SMTP Server Example ===")

    try:
        # Example 1: Corporate SMTP server without authentication
        print("\n1. Using corporate SMTP server (no auth):")

        sender = MailSender(
            email="noreply@company.com",  # Sender email
            smtp_server="mail.company.com",  # Internal SMTP server
            smtp_port=25,  # Often port 25 for internal servers
            auth_required=False  # No authentication needed
        )

        print(f"✓ Configured sender: {sender.email}")
        print(f"✓ SMTP server: {sender.smtp_server}:{sender.smtp_port}")
        print(f"✓ Authentication required: {sender.auth_required}")

        # Test connection
        print("✓ Testing connection...")
        sender.test_connection()
        print("✓ Connection successful!")

        # Note: Uncomment the following to actually send an email
        # success = sender.send_simple_email(
        #     to_email="user@company.com",
        #     subject="Test from Internal Server",
        #     message="This email was sent from an internal SMTP server without authentication."
        # )
        #
        # if success:
        #     print("✓ Email sent successfully!")

    except SendError as e:
        print(f"✗ Connection failed: {e}")
        print("This is expected if you're not on the corporate network")
    except Exception as e:
        print(f"✗ Error: {e}")

    try:
        # Example 2: Using environment variables
        print("\n2. Using environment variables for no-auth setup:")
        print("Set these environment variables:")
        print("export EMAIL=noreply@company.com")
        print("export SMTP_SERVER=mail.company.com")
        print("export SMTP_PORT=25")
        print("export AUTH_REQUIRED=false")

        # This would work if environment variables are set
        # sender = MailSender()
        # print(f"✓ Auth required from env: {sender.auth_required}")

    except Exception as e:
        print(f"✗ Error: {e}")

    print("\n=== Common Internal SMTP Configurations ===")
    print("Port 25:  Traditional SMTP (often internal)")
    print("Port 587: SMTP with STARTTLS (submission)")
    print("Port 465: SMTP over SSL (legacy)")
    print("\nFor internal servers, port 25 is common and may not require TLS")

if __name__ == "__main__":
    main()
