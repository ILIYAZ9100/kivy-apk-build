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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 🛠️ 1. Install system dependencies\n",
    "!sudo apt update -y\n",
    "!sudo apt install -y python3-pip build-essential git python3-dev ffmpeg \\\n",
    "libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \\\n",
    "libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \\\n",
    "zlib1g-dev libgstreamer1.0-dev openjdk-17-jdk unzip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 🛠️ 2. Install Buildozer and Cython\n",
    "!pip install --upgrade pip\n",
    "!pip install cython==0.29.36\n",
    "!pip install buildozer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 📂 3. Upload your Kivy files\n",
    "from google.colab import files\n",
    "print(\"Please upload your main.py and any other required files:\")\n",
    "uploaded = files.upload()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 🏗️ 4. Initialize Buildozer (only if spec doesn't exist)\n",
    "import os\n",
    "if not os.path.exists('buildozer.spec'):\n",
    "    !buildozer init\n",
    "    print(\"✅ buildozer.spec created\")\n",
    "else:\n",
    "    print(\"ℹ️ buildozer.spec already exists - skipping init\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ✍️ 5. Configure buildozer.spec with optimal Android settings\n",
    "import re\n",
    "\n",
    "def update_spec():\n",
    "    with open('buildozer.spec', 'r') as file:\n",
    "        spec = file.read()\n",
    "\n",
    "    # Update requirements\n",
    "    if 'requirements =' not in spec:\n",
    "        spec = re.sub(r'(^requirements\\s*=.*$)', 'requirements = python3,kivy', spec, flags=re.M)\n",
    "    \n",
    "    # Update Android settings\n",
    "    updates = {\n",
    "        '# android.api =': 'android.api = 31',\n",
    "        '# android.minapi =': 'android.minapi = 21',\n",
    "        '# android.ndk_api =': 'android.ndk_api = 21',\n",
    "        '# android.archs =': 'android.archs = arm64-v8a,armeabi-v7a',\n",
    "        '# android.accept_sdk_license =': 'android.accept_sdk_license = True'\n",
    "    }\n",
    "\n",
    "    for old, new in updates.items():\n",
    "        spec = spec.replace(old, new)\n",
    "\n",
    "    with open('buildozer.spec', 'w') as file:\n",
    "        file.write(spec)\n",
    "    \n",
    "    print('✅ buildozer.spec updated with:')\n",
    "    for line in updates.values():\n",
    "        print(f\" - {line}\")\n",
    "\n",
    "update_spec()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 📦 6. Build the APK (this may take ~15-30 minutes)\n",
    "print(\"🚀 Starting APK build process...\")\n",
    "!buildozer -v android debug 2>&1 | tee build.log\n",
    "print(\"\\nBuild completed! Check build.log for details.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 🔍 7. Check build results\n",
    "import glob\n",
    "print(\"Build results:\")\n",
    "print(\"=\"*50)\n",
    "!ls -la bin/\n",
    "print(\"=\"*50)\n",
    "\n",
    "# 📥 8. Download the APK if successful\n",
    "apk_files = glob.glob('bin/*.apk')\n",
    "if apk_files:\n",
    "    print(f\"\\n🎉 APK built successfully: {apk_files[0]}\")\n",
    "    from google.colab import files\n",
    "    files.download(apk_files[0])\n",
    "else:\n",
    "    print('\\n❌ APK build failed. Common issues:')\n",
    "    print(\"1. Missing dependencies in requirements\")\n",
    "    print(\"2. Incorrect Android SDK setup\")\n",
    "    print(\"3. Python code errors\")\n",
    "    print(\"Check build.log above for details.\")"
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
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
