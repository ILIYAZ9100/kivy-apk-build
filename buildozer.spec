[app]

# Application configuration
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0
requirements = python3,kivy,android
orientation = portrait
fullscreen = 1

# Graphics configuration
android.window_soft_input_mode = adjustResize
presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

[buildozer]

# Build configuration
log_level = 2
warn_on_root = 0
target_dir = bin

[android]

# Android specific
arch = arm64-v8a,armeabi-v7a
ndk_path = 
android.ndk = 25b
android.sdk = 31
android.minapi = 21
android.maxapi = 31
android.allow_backup = True
android.accept_sdk_license = True

# Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Debug config
android.debug = True
android.meta_data = 
android.intent_filters = 

[loggers]
root = INFO

[formatters]
keys = simple

[handlers]
keys = console

[handler_console]
class = StreamHandler
level = DEBUG
formatter = simple
args = (sys.stdout,)

[formatter_simple]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
