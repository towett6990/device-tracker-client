[app]
# Your app title (shows on phone)
title = Device Tracker Client

# APK package name (unique reverse-domain style)
package.name = deviceclient
package.domain = org.yourname

# Main entry point (your Python file)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
main.py = mobile_client.py

# App version
version = 0.1

# Application requirements (from requirements.txt)
requirements = python3,kivy,requests

# Android permissions (for GPS + Internet)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# Orientation
orientation = portrait

# Icon (optional, can add later)
# icon.filename = %(source.dir)s/icon.png

# Presplash (optional)
# presplash.filename = %(source.dir)s/presplash.png

# Android API version (31 = Android 12)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.archs = armeabi-v7a,arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

