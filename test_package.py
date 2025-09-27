#!/usr/bin/env ptry:
    from mailworks import GmailSender, AuthenticationError, SendError, ConfigurationError
    from mailworks.config import ConfigManager
    print("✓ Package imported successfully!")
except ImportError as e:3
"""
Test script for the email-sender package.

This script demonstrates how to test the package functionality.
Before running, make sure you have:
1. A Gmail account with 2FA enabled
2. Generated an App Password for Gmail
3. Set the environment variables or update the credentials below
"""

import os
import sys
from pathlib import Path

# Test imports
try:
    from mailworks import GmailSender, AuthenticationError, SendError, ConfigurationError
    from mailworks.config import ConfigManager
    print("✓ Package imports successful")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    sys.exit(1)


def test_package_structure():
    """Test that all package components are accessible."""
    print("\n=== Testing Package Structure ===")

    # Test exception classes
    try:
        raise AuthenticationError("test")
    except AuthenticationError:
        print("✓ AuthenticationError works")

    try:
        raise SendError("test")
    except SendError:
        print("✓ SendError works")

    try:
        raise ConfigurationError("test")
    except ConfigurationError:
        print("✓ ConfigurationError works")

    # Test config manager
    try:
        ConfigManager()
        print("✓ ConfigManager class accessible")
    except Exception as e:
        print(f"✗ ConfigManager error: {e}")


def test_configuration_errors():
    """Test configuration error handling."""
    print("\n=== Testing Configuration Error Handling ===")

    # Clear environment variables for this test
    old_email = os.environ.get('GMAIL_EMAIL')
    old_password = os.environ.get('GMAIL_PASSWORD')

    if 'GMAIL_EMAIL' in os.environ:
        del os.environ['GMAIL_EMAIL']
    if 'GMAIL_PASSWORD' in os.environ:
        del os.environ['GMAIL_PASSWORD']

    try:
        # This should raise ConfigurationError
        sender = GmailSender()
        print("✗ Should have raised ConfigurationError")
    except ConfigurationError as e:
        print(f"✓ Configuration error handled correctly: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

    # Restore environment variables
    if old_email:
        os.environ['GMAIL_EMAIL'] = old_email
    if old_password:
        os.environ['GMAIL_PASSWORD'] = old_password


def test_config_manager():
    """Test the ConfigManager functionality."""
    print("\n=== Testing ConfigManager ===")

    # Test file configuration
    config_content = """# Test Gmail Configuration
GMAIL_EMAIL=test@gmail.com
GMAIL_PASSWORD=test_password
GMAIL_SMTP_SERVER=smtp.gmail.com
GMAIL_SMTP_PORT=587
"""

    config_file = Path("test_config.txt")
    try:
        with open(config_file, "w") as f:
            f.write(config_content)

        config_manager = ConfigManager.from_file("test_config.txt")
        config_manager.validate()

        print("✓ ConfigManager file loading works")
        print(f"  Email: {config_manager.config.email}")
        print(f"  SMTP Server: {config_manager.config.smtp_server}")
        print(f"  SMTP Port: {config_manager.config.smtp_port}")

    except Exception as e:
        print(f"✗ ConfigManager error: {e}")
    finally:
        if config_file.exists():
            config_file.unlink()

    # Test parameter configuration
    try:
        config_manager = ConfigManager.from_parameters(
            email="test@gmail.com",
            password="test_password"
        )
        config_manager.validate()
        print("✓ ConfigManager parameter configuration works")
    except Exception as e:
        print(f"✗ ConfigManager parameter error: {e}")


def test_gmail_sender_creation():
    """Test GmailSender creation with different methods."""
    print("\n=== Testing GmailSender Creation ===")

    # Test with direct parameters
    try:
        sender = GmailSender(email="test@gmail.com", password="test_password")
        print("✓ GmailSender creation with parameters works")
        print(f"  Email configured: {sender.email}")
        print(f"  SMTP Server: {sender.SMTP_SERVER}")
        print(f"  SMTP Port: {sender.SMTP_PORT}")
    except Exception as e:
        print(f"✗ GmailSender creation error: {e}")


def test_connection_with_real_credentials():
    """Test actual connection with real Gmail credentials (if provided)."""
    print("\n=== Testing Real Connection (Optional) ===")

    # Check for environment variables
    email = os.getenv('GMAIL_EMAIL')
    password = os.getenv('GMAIL_PASSWORD')

    if not email or not password:
        print("ℹ️  Skipping real connection test - credentials not provided")
        print("   To test with real credentials, set:")
        print("   export GMAIL_EMAIL='your.email@gmail.com'")
        print("   export GMAIL_PASSWORD='your_app_password'")
        return

    try:
        sender = GmailSender()
        print(f"✓ GmailSender created with email: {sender.email}")

        # Test connection
        print("🔄 Testing connection to Gmail SMTP server...")
        success = sender.test_connection()
        if success:
            print("✓ Connection test successful! Gmail credentials are working.")

            # Ask if user wants to send a test email
            response = input("📧 Do you want to send a test email to yourself? (y/N): ").strip().lower()
            if response in ['y', 'yes']:
                test_email_address = input(f"Enter recipient email (or press Enter to use {email}): ").strip() or email

                success = sender.send_simple_email(
                    to_email=test_email_address,
                    subject="Test Email from Python Email Sender Package",
                    message=f"""Hello!

This is a test email sent from the Gmail Email Sender Python package.

✅ Package installation: SUCCESS
✅ Gmail authentication: SUCCESS
✅ Email sending: SUCCESS

The package is working correctly!

Sent from: {email}
Timestamp: {__import__('datetime').datetime.now()}
"""
                )

                if success:
                    print(f"✅ Test email sent successfully to {test_email_address}!")
                    print("   Check your inbox to confirm delivery.")
                else:
                    print("❌ Failed to send test email")

    except AuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        print("💡 Tips:")
        print("   - Make sure you're using a Gmail App Password, not your regular password")
        print("   - Enable 2-Factor Authentication on your Gmail account")
        print("   - Generate a new App Password: https://myaccount.google.com/apppasswords")

    except Exception as e:
        print(f"❌ Connection test failed: {e}")


def test_attachment_functionality():
    """Test attachment functionality with a dummy file."""
    print("\n=== Testing Attachment Functionality ===")

    # Create a test attachment
    test_file = Path("test_attachment.txt")
    try:
        with open(test_file, "w") as f:
            f.write("This is a test attachment file for the email sender package.")

        # Test attachment validation (without actually sending)
        sender = GmailSender(email="test@gmail.com", password="test_password")

        # Test that attachment file checking works
        try:
            from email.mime.multipart import MIMEMultipart
            msg = MIMEMultipart()
            sender._add_attachment(msg, test_file)
            print("✓ Attachment functionality works")
        except Exception as e:
            print(f"✗ Attachment error: {e}")

        # Test non-existent file handling
        try:
            sender._add_attachment(MIMEMultipart(), "non_existent_file.txt")
            print("✗ Should have raised error for non-existent file")
        except SendError:
            print("✓ Non-existent file error handling works")

    finally:
        if test_file.exists():
            test_file.unlink()


def main():
    """Run all tests."""
    print("🧪 Email Sender Package Test Suite")
    print("=" * 50)

    test_package_structure()
    test_configuration_errors()
    test_config_manager()
    test_gmail_sender_creation()
    test_attachment_functionality()
    test_connection_with_real_credentials()

    print("\n" + "=" * 50)
    print("✅ Test suite completed!")
    print("\n💡 Next steps:")
    print("   1. Set your Gmail credentials:")
    print("      export GMAIL_EMAIL='your.email@gmail.com'")
    print("      export GMAIL_PASSWORD='your_app_password'")
    print("   2. Run the test again to test real connections")
    print("   3. Try the example scripts in the examples/ directory")
    print("   4. Check the README.md for detailed usage instructions")


if __name__ == "__main__":
    main()
