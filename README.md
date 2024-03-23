# Python Keylogger

A simple keylogger implemented in Python.

## Features

- **Crafting Data Files**: Necessary data structures and variables with appropriate extensions for efficient storage and organization of logged information before writing them into files.
- **Keyboard Logging**: Utilizing the pynput module to log keystrokes.
- **Email Functionality**: Incorporating email functionality via the email module.
- **System Information**: Gathering system details using socket and platform modules.
- **Clipboard Monitoring**: Accessing clipboard information with the win32clipboard module.
- **Microphone Recording**: Recording with the microphone using the sounddevice module and writing to .wav files with scipy.io.wavefile.
- **Screen Capture**: Taking screenshots with ImageGrab from the Pillow Module.
- **Timer Integration**: Implementing a timer to define the duration of keylogging sessions.
- **File Encryption**: Utilizing the cryptography.fernet module to encrypt files.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/python-keylogger.git

2. **CD to directory**
   ```bash
   cd /path/to/your/project
   
3. **Run the keylogger**
   ```bash
   python3 keylogger.py
