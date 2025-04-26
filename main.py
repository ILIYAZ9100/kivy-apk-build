{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🚀 Kivy App to APK with Buildozer (Colab Ready, Error-Free)"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# 🛠️ 1. Install system dependencies",
    "!sudo apt update -y\n",
    "!sudo apt install -y python3-pip build-essential git python3-dev ffmpeg \\\n",
    "libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \\\n",
    "libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \\\n",
    "zlib1g-dev libgstreamer1.0-dev openjdk-17-jdk unzip"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# 🛠️ 2. Install Buildozer and Cython",
    "!pip install --upgrade pip\n",
    "!pip install cython==0.29.36\n",
    "!pip install buildozer"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# 📂 3. Upload your main.py file",
    "from google.colab import files\n",
    "uploaded = files.upload()"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# 🏗️ 4. Initialize Buildozer",
    "!buildozer init"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# ✍️ 5. Edit buildozer.spec automatically to fix Android settings\n",
    "with open('buildozer.spec', 'r') as file:\n",
    "    spec = file.read()\n",
    "\n",
    "spec = spec.replace('requirements = python3,kivy', 'requirements = python3,kivy')\n",
    "spec = spec.replace('# android.api = 27', 'android.api = 31')\n",
    "spec = spec.replace('# android.minapi = 21', 'android.minapi = 21')\n",
    "spec = spec.replace('# android.ndk_api = 21', 'android.ndk_api = 21')\n",
    "spec = spec.replace('# android.archs = armeabi-v7a', 'android.archs = arm64-v8a,armeabi-v7a')\n",
    "\n",
    "with open('buildozer.spec', 'w') as file:\n",
    "    file.write(spec)\n",
    "    print('✅ buildozer.spec updated')"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# 📦 6. Build the APK (this may take ~15-30 minutes)",
    "!buildozer -v android debug"
   ]
  },
  {
   "cell_type": "code",
   "metadata": {},
   "source": [
    "# 📥 7. Download the APK file manually\n",
    "import glob\n",
    "apk_files = glob.glob('bin/*.apk')\n",
    "if apk_files:\n",
    "    from google.colab import files\n",
    "    files.download(apk_files[0])\n",
    "else:\n",
    "    print('❌ No APK found. Build may have failed.')"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
