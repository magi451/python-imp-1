import subprocess
import sys

def install(package):
   
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Package '{package}' installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing '{package}': {e}")

def invite_friends():
    
    friends = ["magi", "balaji", "pranav"]
    server_ip = "Balaji2006.aternos.me:48643"

    for friend in friends:
        print(f"Hey {friend}, let's play Minecraft our server {server_ip}")

def launch_minecraft():
   
    minecraft_path = input("Enter the path to your minecraft executable: ")

    try:
        subprocess.Popen(minecraft_path)
        print("Minecraft excecuted successfully!")
    except FileNotFoundError as e:
        print(f"Error: Minecraft executable not found. Details: {e}")

if __name__ == "__main__":
    invite_friends()
    install("requests")
    launch_minecraft()
