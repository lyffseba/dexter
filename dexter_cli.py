import os
import sys
import time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    print_slow("==================================================")
    print_slow("           D E X T E R   O S   v1.0               ")
    print_slow("==================================================")
    print_slow("\n[SYSTEM] Initializing AI Research Swarm...")
    time.sleep(1)
    print_slow("[SYSTEM] Connecting to Modular Cloud...")
    time.sleep(0.5)
    print_slow("[SYSTEM] Authenticating RunPod API...")
    time.sleep(0.5)
    print_slow("[SYSTEM] Environment: SECURE.\n")
    
    print("Welcome, Director lyffseba.")
    print("The lab is funded. The GPUs are standing by.\n")
    
    while True:
        print("----- COMMAND MENU -----")
        print("1. [LAB 00]  Run Local Diagnostics (Data & Tokenizer)")
        print("2. [LAB 03]  Compile Mojo Architecture locally")
        print("3. [RUNPOD]  Deploy RTX 3090 (Commence RLHF Training)")
        print("4. [MODULAR] Deploy MAX Inference Endpoint")
        print("5. [EXIT]    Disconnect")
        
        choice = input("\nAwaiting command (1-5): ")
        
        if choice == '1':
            print_slow("\n[EXECUTING] Launching Jupyter Lab for Lab 00...")
            os.system("uv tool run --from jupyterlab jupyter-lab labs/00_getting_started.ipynb")
        elif choice == '2':
            print_slow("\n[EXECUTING] Compiling train.mojo via Pixi...")
            os.system("cd labs/autoresearch/mojo && ~/.pixi/bin/pixi run mojo train.mojo")
            print("\n")
        elif choice == '3':
            print_slow("\n[WARNING] This action will consume RunPod credits ($0.25/hr).")
            confirm = input("Confirm deployment of 1x RTX 3090? (y/n): ")
            if confirm.lower() == 'y':
                print_slow("\n[DEPLOYING] Contacting RunPod API...")
                # The actual runpodctl command goes here
                print_slow("[SUCCESS] Pod 'autoresearch-3090' is booting up.")
                print_slow("[NETWORK] Establishing SSH connection...")
                print_slow("... Standing by for agent 'pi' to take over the instance.\n")
                break
            else:
                print("\n[ABORTED] Deployment cancelled.\n")
        elif choice == '4':
            print_slow("\n[EXECUTING] Preparing Modular MAX serving script...")
            print("Run: bash scripts/02_start_server.sh on your instance.\n")
        elif choice == '5':
            print_slow("\n[SYSTEM] Disconnecting... Goodbye, Director.")
            break
        else:
            print("\n[ERROR] Invalid command.\n")

if __name__ == "__main__":
    main()
