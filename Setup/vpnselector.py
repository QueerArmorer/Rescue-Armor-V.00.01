import os

print("Rescue Armor is flexible and allows you to pick certain options.")
print("A VPN is a private network that secures your internet connection and keeps your data safe.")
print("ProtonVPN is a free VPN service that offers strong encryption and privacy features, as well as integration with their secure email service. NordVPN is a paid VPN service that offers advanced P2P capabilities and a larger network of servers in more countries.")
print("Please choose your VPN provider:")
print("1. ProtonVPN (Free)")
print("2. NordVPN (Paid)")

# Get user input
choice = input("Enter your choice (1 or 2): ")

# Verify user input
if choice == "1":
    print("You have chosen ProtonVPN.")
    # Run the ProtonVPN installation script
    os.system("python protonvpn.py install")
elif choice == "2":
    print("You have chosen NordVPN.")
    # Run the NordVPN installation script
    os.system("python nordvpn.py install")
else:
    print("Invalid input. Please try again.")

