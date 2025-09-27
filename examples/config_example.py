"""
Configuration-based email sending example.

This example demonstrates using the ConfigManager for different
configuration sources.
"""

from mailworks import GmailSender
from mailworks.config import ConfigManager

def example_with_env_config():
    """Example using environment variables."""
    print("=== Using Environment Variables ===")
    try:
        config_manager = ConfigManager.from_env()
        config_manager.validate()

        sender = GmailSender(
            email=config_manager.config.email,
            password=config_manager.config.password
        )

        success = sender.send_simple_email(
            to_email="recipient@example.com",
            subject="Config Example - Environment Variables",
            message="This email was sent using configuration from environment variables."
        )

        print("✓ Email sent using environment config!" if success else "✗ Failed to send email")

    except Exception as e:
        print(f"✗ Error with environment config: {e}")

def example_with_file_config():
    """Example using configuration file."""
    print("\n=== Using Configuration File ===")

    # Create a sample config file
    config_content = """# Gmail Configuration
GMAIL_EMAIL=your.email@gmail.com
GMAIL_PASSWORD=your_app_password
GMAIL_SMTP_SERVER=smtp.gmail.com
GMAIL_SMTP_PORT=587
"""

    config_file = "gmail_config.txt"
    with open(config_file, "w") as f:
        f.write(config_content)

    try:
        config_manager = ConfigManager.from_file(config_file)
        config_manager.validate()

        sender = GmailSender(
            email=config_manager.config.email,
            password=config_manager.config.password
        )

        success = sender.send_simple_email(
            to_email="recipient@example.com",
            subject="Config Example - File Configuration",
            message="This email was sent using configuration from a file."
        )

        print("✓ Email sent using file config!" if success else "✗ Failed to send email")

    except Exception as e:
        print(f"✗ Error with file config: {e}")
        print("Note: Update the config file with your actual credentials")

    finally:
        # Clean up
        import os
        if os.path.exists(config_file):
            os.remove(config_file)

def example_with_parameter_config():
    """Example using direct parameters."""
    print("\n=== Using Direct Parameters ===")

    # Replace with your actual credentials
    EMAIL = "your.email@gmail.com"
    PASSWORD = "your_app_password"

    try:
        config_manager = ConfigManager.from_parameters(
            email=EMAIL,
            password=PASSWORD
        )
        config_manager.validate()

        sender = GmailSender(
            email=config_manager.config.email,
            password=config_manager.config.password
        )

        success = sender.send_simple_email(
            to_email="recipient@example.com",
            subject="Config Example - Direct Parameters",
            message="This email was sent using direct parameter configuration."
        )

        print("✓ Email sent using parameter config!" if success else "✗ Failed to send email")

    except Exception as e:
        print(f"✗ Error with parameter config: {e}")
        print("Note: Update the EMAIL and PASSWORD variables with your actual credentials")

def main():
    print("Email Sender Configuration Examples")
    print("=" * 40)

    example_with_env_config()
    example_with_file_config()
    example_with_parameter_config()

    print("\nDone! Remember to update the examples with your actual Gmail credentials.")

if __name__ == "__main__":
    main()
