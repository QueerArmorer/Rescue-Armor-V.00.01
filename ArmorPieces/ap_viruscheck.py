import subprocess
import os
import time

# Windows Defender
subprocess.run(['MpCmdRun.exe', '-Scan', '-ScanType', '3'])

# Waiting games
while True:
    p = subprocess.Popen(['tasklist', '/FI', 'IMAGENAME eq MsMpEng.exe'], stdout=subprocess.PIPE)
    if b'MsMpEng.exe' not in p.communicate()[0]:
        break
    time.sleep(5)

# Check if Avast and Bitdefender are installed
avast_installed = os.path.exists('C:\\Program Files\\AVAST Software\\Avast')
bitdefender_installed = os.path.exists('C:\\Program Files\\Bitdefender Antivirus Free')

# Run the Jewels
if avast_installed:
    subprocess.run(['C:\\Program Files\\AVAST Software\\Avast\\AvastUI.exe'])
elif bitdefender_installed:
    subprocess.run(['C:\\Program Files\\Bitdefender Antivirus Free\\bdagent.exe'])
else:
    print("Error: Neither Avast nor Bitdefender was installed. At least one is usually installed with this suite. Rescue Armor is likely compromise compromised.")

