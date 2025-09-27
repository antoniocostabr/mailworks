# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-09-26

### Added
- **Internal SMTP Server Support**: New `auth_required` parameter to support corporate SMTP servers without authentication
- Environment variable `AUTH_REQUIRED` to control authentication requirements
- `internal_smtp_example.py` example for corporate environments
- Security warnings in documentation for no-auth configurations

### Security
- **Secure by default**: `auth_required=True` by default - authentication required unless explicitly disabled
- Clear documentation emphasizing security implications of disabling authentication

## [2.0.0] - 2025-09-26

### Added
- **Universal SMTP Provider Support**: Now works with any SMTP server with STARTTLS support
- Support for major email providers:
  - Gmail (default)
  - Outlook/Hotmail
  - Yahoo
  - ProtonMail
  - Zoho
  - SendGrid
  - Amazon SES
  - Custom SMTP servers
- Configurable SMTP server and port parameters
- Environment variables for SMTP configuration (`SMTP_SERVER`, `SMTP_PORT`)
- `smtp_providers_example.py` with examples for different providers
- Comprehensive provider support table in documentation

### Changed
- **BREAKING**: Package renamed from `email_sender` to `mailworks`
- **BREAKING**: Main class renamed from `GmailSender` to `MailSender`
- **BREAKING**: Module renamed from `gmail_sender.py` to `mail_sender.py`
- **BREAKING**: Environment variables changed from `GMAIL_*` to generic names:
  - `GMAIL_EMAIL` → `EMAIL` (old variables still supported for backward compatibility)
  - `GMAIL_PASSWORD` → `PASSWORD`
- Updated import statements: `from mailworks import MailSender`
- Enhanced constructor with configurable SMTP settings
- Improved error messages to be provider-neutral
- Updated documentation to reflect universal SMTP support

### Removed
- Gmail-specific email validation (no longer restricted to @gmail.com addresses)
- Hardcoded Gmail SMTP server and port values

### Backward Compatibility
- `GmailSender` class still available as an alias to `MailSender`
- Old `GMAIL_*` environment variables still supported alongside new generic ones
- Existing code continues to work without modifications

### Documentation
- Complete rewrite of README.md to reflect universal SMTP support
- Added migration guide for users upgrading from v1.x
- Enhanced examples showing different provider configurations
- Updated API reference with new parameters
- Added "What's New in v2.0" section

## [1.0.0] - 2025-09-26

### Added
- Initial release with Gmail-only support
- `GmailSender` class for sending emails via Gmail SMTP
- Support for plain text and HTML emails
- File attachment support
- Multiple recipient support
- Environment variable configuration (`GMAIL_EMAIL`, `GMAIL_PASSWORD`)
- Configuration file support
- Connection testing functionality
- Comprehensive error handling with custom exceptions:
  - `AuthenticationError`
  - `SendError`
  - `ConfigurationError`
  - `EmailSenderError`
- Gmail App Password setup documentation
- Example files:
  - `basic_example.py`
  - `advanced_example.py`
  - `config_example.py`
  - `complete_example.py`
- No external dependencies (Python standard library only)

### Features
- Send simple text emails
- Send HTML emails with attachments
- Multiple recipients support
- Secure SMTP with STARTTLS encryption
- Gmail App Password authentication
- Environment variable and direct parameter configuration
- Comprehensive error handling and validation

---

## Migration Guide

### From v1.x to v2.x

#### Package Import
```python
# Old (v1.x)
from email_sender import GmailSender

# New (v2.x) - Recommended
from mailworks import MailSender

# Backward compatible (still works)
from mailworks import GmailSender  # Alias to MailSender
```

#### Environment Variables
```bash
# Old (v1.x) - Still supported
export GMAIL_EMAIL="user@gmail.com"
export GMAIL_PASSWORD="app_password"

# New (v2.x) - Recommended
export EMAIL="user@anyprovider.com"
export PASSWORD="app_password"
export SMTP_SERVER="smtp.anyprovider.com"  # Optional
export SMTP_PORT="587"                     # Optional
```

#### Class Usage
```python
# Old (v1.x) - Still works
sender = GmailSender(email="user@gmail.com", password="password")

# New (v2.x) - More flexible
sender = MailSender(
    email="user@anyprovider.com",
    password="password",
    smtp_server="smtp.anyprovider.com",
    smtp_port=587
)

# New (v2.x) - Internal SMTP servers
sender = MailSender(
    email="noreply@company.com",
    smtp_server="mail.company.com",
    auth_required=False  # No authentication needed
)
```

### Deprecation Timeline
- v2.x: `GmailSender` and `GMAIL_*` environment variables supported for backward compatibility
- v3.x (future): `GmailSender` and `GMAIL_*` environment variables may be deprecated with warnings
- v4.x (future): `GmailSender` and `GMAIL_*` environment variables may be removed

For now, all existing code continues to work without modifications.
