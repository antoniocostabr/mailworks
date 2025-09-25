from email_sender import GmailSender
import dotenv
import os

def set_env_variables():
    # Method 1: Using environment variables
    # Set environment variables:
    # export GMAIL_EMAIL="your.email@gmail.com"
    # export GMAIL_PASSWORD="your_app_password"

    # Method 2: Using a .env file
    dotenv.load_dotenv()  # Load environment variables from .env file if present

    return

def main():
    # Send a simple email

    set_env_variables()
    print("Sending a simple email...")
    sender = GmailSender()

    success = sender.send_simple_email(
        to_email=os.getenv("TO_EMAIL", "recipient@example.com"),
        subject="Hello from Python!",
        message="This is a test email sent from Python."
    )

    if success:
        print("Email sent successfully!")
    else:
        print("Failed to send simple email.")


    print("Sending an advanced email...")
    # Sending an email with HTML content and attachments
    success = sender.send_email(
        to_emails=["recipient1@example.com",
                   "recipient2@example.com",
                   os.getenv("TO_EMAIL", "recipient@example.com")],
        subject="Advanced Email Example",
        message="Plain text version of the email.",
        html_message="""
        <html>
            <body>
                <h2>Hello!</h2>
                <p>This is an <b>HTML email</b> with formatting.</p>
            </body>
        </html>
        """,
        attachments=["examples/file1.txt", "examples/file2.txt"]
    )

    if success:
        print("Advanced email sent successfully!")
    else:
        print("Failed to send advanced email.")

if __name__ == "__main__":
    main()
