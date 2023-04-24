import subprocess

# Malwarebytes goes first
print("Running Malwarebytes Anti-Rootkit...")
malwarebytes_cmd = ["C:\\Program Files\\Malwarebytes\\Anti-Rootkit\\mbar.exe", "--quick-scan", "--no-disk-scan"]
malwarebytes_process = subprocess.Popen(malwarebytes_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait, bitch
stdout, stderr = malwarebytes_process.communicate()
if stderr:
    print("Error running Malwarebytes Anti-Rootkit:", stderr.decode())
else:
    print("Malwarebytes Anti-Rootkit scan complete.")

# We good?
print("Checking for running processes...")
tasklist_cmd = ["tasklist"]
tasklist_process = subprocess.Popen(tasklist_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for tasklist
stdout, stderr = tasklist_process.communicate()
if stderr:
    print("Error checking for running processes:", stderr.decode())
else:
    if b"no task" in stdout.lower():
        print("No running processes found.")
    else:
        print("Found running processes.")

# Run GMER
print("Running GMER...")
gmer_cmd = ["C:\\gmer\\gmer.exe"]
gmer_process = subprocess.Popen(gmer_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for GMER to finish
stdout, stderr = gmer_process.communicate()
if stderr:
    print("Error running GMER:", stderr.decode())
else:
    print("GMER scan complete.")

# Wipe mouth and smile
print("After checking for Root Kits with multiple tools, we found the following:")
print("Malwarebytes Anti-Rootkit: ", stdout.decode())
print("GMER: ", stderr.decode())

# Full info
if b"rootkit" in stdout.lower():
    print("Rootkit found by GMER!")
    if b"delete" in stderr.lower():
        print("GMER has already deleted the rootkit. Rescue Armor is not considered compromised but be at alert.")
    else:
        print("GMER has not yet deleted the rootkit. Consider this system compromised.")
else:
    print("No rootkits found by GMER. Rescue Armor is not compromised.")
if b"rootkit" in stdout.lower():
    print("Rootkit found by Malwarebytes Anti-Rootkit!")
    if b"delete" in stdout.lower():
        print("Malwarebytes Anti-Rootkit has already deleted the rootkit. Rescue Armor is not compromised but be on alert.")
    else:
        print("Malwarebytes Anti-Rootkit has not yet deleted the rootkit. Consider this system compromised.")
else:
    print("No rootkits found by Malwarebytes Anti-Rootkit. Rescue Armor is not compromised but be on alert.")

