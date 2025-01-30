#!/usr/bin/env python3

import os
import shutil
import subprocess

# Author: Richard Lopez Corbalan
# GitHub: github.com/richardloopez
# Citation: If you use this code, please cite Lopez-Corbalan, R.
# Seminario_mod Method: github.com/aa840/ModSeminario_Py

def seminarizador(folder, manage_gaussian):
    print(f"Executing seminarizador in: {folder}")
    os.chdir(folder)
    
    # Check for .chk and .log files
    chk_files = [f for f in os.listdir() if f.endswith(".chk")]
    log_files = [f for f in os.listdir() if f.endswith(".log")]
    
    if not chk_files or not log_files:
        print(f"    {folder} does not contain: {'chk file' if not chk_files else ''} {'log file' if not log_files else ''}".strip())
        return
    
    chk_file = chk_files[0]
    
    # Manage Gaussian modules and environment if required
    if manage_gaussian:
        subprocess.run("module unload gaussian/16", shell=True, executable="/bin/bash", stderr=subprocess.DEVNULL)
        subprocess.run("module load gaussian/09", shell=True, executable="/bin/bash", stderr=subprocess.DEVNULL)

        # Force environment variables for Gaussian 09
        os.environ["GAUSS_EXEDIR"] = "/usr/local/gaussian/09.D/g09"
        os.environ["PATH"] = f"{os.environ['GAUSS_EXEDIR']}:{os.environ['PATH']}"
    
    # Check and execute formchk
    formchk_path = shutil.which("formchk")
    print(f"Using formchk from: {formchk_path}")
    subprocess.run(["formchk", chk_file])
    
    # Create mod_seminario folder and move to it
    os.makedirs("mod_seminario/ligand", exist_ok=True)
    shutil.copytree(SEMINARIO_PATH, "mod_seminario/Python_Modified_Seminario_Method", dirs_exist_ok=True)
    
    # Move to ligand folder
    os.chdir("mod_seminario/ligand")
    
    # Copy and rename files
    for ext, new_name in zip([".fchk", ".log"], ["lig.fchk", "lig.log"]):
        for file in os.listdir("../../"):
            if file.endswith(ext):
                shutil.copy(f"../../{file}", new_name)
                break
    
    # Run Seminario script
    os.chdir("../Python_Modified_Seminario_Method")
    subprocess.run(["python", "modified_Seminario_method.py", "../ligand/", "../ligand/", "1"])
    
    # Return to base directory
    os.chdir("../../..")

# User information
print("Warning: This script processes subdirectories to apply the Seminario method.")
print("You can have as many folders and subfolder as you want.") 
print("\nHave in mind: in the subfolder you want to perform the Seminario method you need to have:"
        "\n         -Only one .chk file"
        "\n         -Only one .log file"
        "\n         *Presence of other files is not a problem"
        "\n         *This code has to be launched in the folder [0] (along with the other folders, not subfolders)")

# Get user input
depth_degree = int(input("What is the depth degree of the subfolders? [1 - infinite) [folder containing this code = 0] [0 is allowed] : "))
manage_gaussian = input("Seminario only works with Gaussian 09. Do you want this script to unload Gaussian 16 and load Gaussian 09 automatically? (yes/no): ").strip().lower() == "yes"
SEMINARIO_PATH = input("Paste the Path to Python_Modified_Seminario_Method: ").strip()

print("Exploring directories...")
visited_dirs = set()

def explore_directory(base_folder, current_depth, max_depth):
    if current_depth > max_depth:
        return
    
    for folder in sorted(os.listdir(base_folder)):
        folder_path = os.path.join(base_folder, folder)
        
        if os.path.isdir(folder_path) and folder_path not in visited_dirs:
            visited_dirs.add(folder_path)
            print(f"Exploring: {folder_path}")
            seminarizador(folder_path, manage_gaussian)
            explore_directory(folder_path, current_depth + 1, max_depth)

# Start exploring from the current directory
explore_directory(os.getcwd(), 0, depth_degree)

