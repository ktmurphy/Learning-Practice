#! python3
# mapit.py but saved under chapter12practice.py - opens google maps to address using command line arguments
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open("https://www.google.com/maps/place/" + address)
