#!/usr/bin/env python3
"""
SMTP Connectivity Test Script
Run this script to diagnose SMTP connectivity issues
"""

import socket
import smtplib
import sys
from datetime import datetime

def test_basic_connectivity():
    """Test basic internet connectivity"""
    print("=== Testing Basic Internet Connectivity ===")
    try:
        sock = socket.create_connection(('www.google.com', 80), timeout=10)
        sock.close()
        print("✓ Basic internet connectivity: OK")
        return True
    except Exception as e:
        print(f"✗ Basic internet connectivity: FAILED - {e}")
        return False

def test_smtp_ports():
    """Test SMTP ports for Gmail"""
    print("\n=== Testing SMTP Ports ===")
    smtp_configs = [
        ('smtp.gmail.com', 587, 'STARTTLS'),
        ('smtp.gmail.com', 465, 'SSL/TLS'),
        ('smtp.gmail.com', 25, 'Plain (usually blocked)'),
    ]
    
    results = []
    for host, port, description in smtp_configs:
        try:
            print(f"Testing {host}:{port} ({description})...")
            sock = socket.create_connection((host, port), timeout=10)
            sock.close()
            print(f"✓ {host}:{port} - Connection successful")
            results.append(True)
        except Exception as e:
            print(f"✗ {host}:{port} - Connection failed: {e}")
            results.append(False)
    
    return any(results)

def test_smtp_handshake():
    """Test SMTP handshake if connection is possible"""
    print("\n=== Testing SMTP Handshake ===")
    try:
        print("Attempting SMTP connection and handshake...")
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=10) as server:
            server.set_debuglevel(1)  # Enable debug output
            server.starttls()
            print("✓ SMTP handshake successful")
            return True
    except Exception as e:
        print(f"✗ SMTP handshake failed: {e}")
        return False

def test_alternative_providers():
    """Test other email providers"""
    print("\n=== Testing Alternative Email Providers ===")
    providers = [
        ('smtp.outlook.com', 587, 'Outlook/Hotmail'),
        ('smtp.yahoo.com', 587, 'Yahoo'),
        ('smtp.mail.me.com', 587, 'iCloud'),
    ]
    
    for host, port, name in providers:
        try:
            sock = socket.create_connection((host, port), timeout=5)
            sock.close()
            print(f"✓ {name} ({host}:{port}) - Accessible")
        except Exception as e:
            print(f"✗ {name} ({host}:{port}) - Blocked")

def main():
    print(f"SMTP Connectivity Diagnostic Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Run all tests
    internet_ok = test_basic_connectivity()
    smtp_ports_ok = test_smtp_ports()
    
    if smtp_ports_ok:
        smtp_handshake_ok = test_smtp_handshake()
    else:
        smtp_handshake_ok = False
    
    test_alternative_providers()
    
    print("\n" + "=" * 50)
    print("SUMMARY:")
    print(f"Internet Connectivity: {'✓ OK' if internet_ok else '✗ FAILED'}")
    print(f"SMTP Ports Access: {'✓ OK' if smtp_ports_ok else '✗ BLOCKED'}")
    print(f"SMTP Handshake: {'✓ OK' if smtp_handshake_ok else '✗ FAILED'}")
    
    if not smtp_ports_ok:
        print("\nRECOMMENDATIONS:")
        print("• SMTP ports appear to be blocked by your network")
        print("• Try from a different network (mobile hotspot, home network)")
        print("• Contact your network administrator about SMTP access")
        print("• Consider using Gmail API instead of SMTP")
        print("• Use a VPN to bypass network restrictions")

if __name__ == "__main__":
    main()