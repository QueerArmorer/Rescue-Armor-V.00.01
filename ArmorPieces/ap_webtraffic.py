import psutil
import time
import subprocess
import webbrowser

# Can you just not
input("Please stop any background web traffic. Press enter when ready to begin the test. ")

# Longboi check
print("\nThe test will run for 1 minute to check the current web traffic and then for 15 minutes with no web traffic.")

# Windows update BS
if psutil.pid_exists(psutil.win_service_get("wuauserv").pid):
    print("\nWindows Update is currently running. Press enter to exit or type 'emergency' and press enter to stop Windows Update.")
    if input().lower() == "emergency":
        subprocess.run(["net", "stop", "wuauserv"])

# Non-Windows update BS
game_updaters = ["Steam", "Uplay", "Origin", "Blizzard", "Microsoft Store", "Epic Games Launcher"]
for updater in game_updaters:
    if psutil.pid_exists(psutil.win_service_get(updater).pid):
        print(f"\n{updater} is currently running. Press enter to exit or type 'emergency' and press enter to stop {updater}.")
        if input().lower() == "emergency":
            subprocess.run(["taskkill", "/f", "/im", f"{updater}.exe"])

# Close web browsers
web_browsers = ["Firefox", "Chrome", "Opera", "Internet Explorer", "Microsoft Edge"]
for browser in web_browsers:
    for process in psutil.process_iter(['name']):
        if process.info['name'].lower() == f"{browser}.exe":
            process.kill()
            print(f"\n{browser} has been closed.")

# No seriously did they close shit?
general_traffic = 0
for i in range(60):
    general_traffic += psutil.net_io_counters().bytes_sent
    general_traffic += psutil.net_io_counters().bytes_recv
    time.sleep(1)

if general_traffic > 1000000:
    print("\nThere is currently too much web traffic to perform the test. Please close open sources. If you have already closed all known sources of traffic, consider this a failure, your system may be compromised.")
else:
    # "Get off my lawn" energy
    start_time = time.time()
    inactive_traffic = 0
    while time.time() - start_time < 900:
        inactive_traffic += psutil.net_io_counters().bytes_sent
        inactive_traffic += psutil.net_io_counters().bytes_recv
        time.sleep(1)
        if psutil.net_io_counters().bytes_sent > inactive_traffic or psutil.net_io_counters().bytes_recv > inactive_traffic:
            print("\nAnomalous web traffic has been detected by Rescue Armor. Your system may be compromised. Further investigation needed.")
            break
        elif
            print("\nTest past. No anomalous activity was detected by Rescue Armor.")

print("\nThe test is complete.")

