"""
Advanced email sending example with HTML content and attachments.

This example demonstrates:
- Sending HTML emails
- Adding attachments
- Sending to multiple recipients
- Using direct credentials (not environment variables)
"""

from email_sender import GmailSender
from pathlib import Path

def main():
    # Replace with your actual credentials
    EMAIL = "your.email@gmail.com"
    PASSWORD = "your_app_password"
    
    try:
        # Create sender with direct credentials
        sender = GmailSender(email=EMAIL, password=PASSWORD)
        
        # HTML email content
        html_content = """
        <html>
          <body>
            <h2>Welcome to Email Sender!</h2>
            <p>This is an <b>HTML email</b> sent from Python.</p>
            <p>Features demonstrated:</p>
            <ul>
              <li>HTML formatting</li>
              <li>Multiple recipients</li>
              <li>File attachments</li>
            </ul>
            <p>Best regards,<br>
            <i>Your Python Email Sender</i></p>
          </body>
        </html>
        """
        
        # Plain text version (fallback)
        text_content = """
        Welcome to Email Sender!
        
        This is a plain text email sent from Python.
        
        Features demonstrated:
        - HTML formatting
        - Multiple recipients  
        - File attachments
        
        Best regards,
        Your Python Email Sender
        """
        
        # Multiple recipients
        recipients = [
            "recipient1@example.com",
            "recipient2@example.com"
        ]
        
        # Create a sample attachment (optional)
        sample_file = Path("sample_attachment.txt")
        if not sample_file.exists():
            with open(sample_file, "w") as f:
                f.write("This is a sample attachment created by the email sender example.")
        
        print("Sending advanced email...")
        
        success = sender.send_email(
            to_emails=recipients,
            subject="Advanced Email Example - HTML & Attachments",
            message=text_content,
            html_message=html_content,
            attachments=[sample_file]
        )
        
        if success:
            print("✓ Advanced email sent successfully!")
            print(f"  Recipients: {', '.join(recipients)}")
            print(f"  Attachments: {sample_file.name}")
        else:
            print("✗ Failed to send email")
            
    except Exception as e:
        print(f"✗ Error: {e}")
        
    finally:
        # Clean up sample file
        if sample_file.exists():
            sample_file.unlink()

if __name__ == "__main__":
    main()