#!/bin/bash
# ===============================
# Termux Wi-Fi Security Tool Setup
# Safe: Own network only
# ===============================

echo "[*] Updating Termux packages..."
pkg update -y && pkg upgrade -y

echo "[*] Installing essential tools..."
pkg install git python curl nano -y

echo "[*] Installing Wi-Fi security tools..."
pkg install aircrack-ng wifite tcpdump -y

echo "[*] Checking Wi-Fi interface..."
WIFI_INTERFACE=$(ip link | grep wlan0 | awk -F: '{print $2}' | tr -d ' ')
if [ -z "$WIFI_INTERFACE" ]; then
    echo "[❌] Wi-Fi interface wlan0 not found. Check your device."
else
    echo "[✅] Wi-Fi interface detected: $WIFI_INTERFACE"
fi

echo "[*] Ready to use commands (Own Network Only):"
echo "-------------------------------------------"
echo "1️⃣ Scan nearby Wi-Fi networks:"
echo "   sudo airodump-ng $WIFI_INTERFACE"
echo "2️⃣ Enable monitor mode (if supported):"
echo "   sudo airmon-ng start $WIFI_INTERFACE"
echo "3️⃣ Capture WPA handshake (own network):"
echo "   sudo airodump-ng -c [channel] --bssid [BSSID] -w capture $WIFI_INTERFACE"
echo "4️⃣ Test password strength with wordlist:"
echo "   sudo aircrack-ng -w wordlist.txt capture-01.cap"
echo "5️⃣ Deauth own devices (testing only):"
echo "   sudo aireplay-ng --deauth 5 -a [BSSID] $WIFI_INTERFACE"
echo "6️⃣ View connected Wi-Fi info (Android Termux):"
echo "   termux-wifi-connectioninfo"
echo "-------------------------------------------"

echo "[*] Remember: Own network only! Testing others = illegal!"
