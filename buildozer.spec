[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.permissions = INTERNET
android.minapi = 21
android.ndk = 25b
android.sdk = 31
