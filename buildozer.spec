[app]
# General app metadata
title = Calculator App
package.name = calculatorapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Files and directories to exclude to reduce APK size
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv
source.exclude_patterns = LICENSE,README.md,*.md

# Python and Kivy dependencies
requirements = python3,kivy==2.1.0

# Android-specific settings
android.api = 31
android.minapi = 21
android.ndk = 23.1.7779620
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/23.1.7779620
android.build_tools_version = 31.0.0
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = False

# No permissions required for this calculator app
android.permissions =

# Lock to portrait for calculator UI
orientation = portrait

# Logging and debugging
android.logcat_filters = *:S python:D

# Optional: Specify icon and presplash (uncomment if you have these assets)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

[buildozer]
# Verbose logging for debugging
log_level = 2
warn_on_root = 1

# Use SDL2 bootstrap for Kivy
p4a.bootstrap = sdl2
