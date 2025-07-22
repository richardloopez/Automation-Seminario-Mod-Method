#Automation Script for the Modified Seminario Method
This script automates the execution of the Modified Seminario Method across multiple directories and subdirectories. It is designed for high-throughput processing of molecular systems, preparing the necessary files and running the Seminario protocol to calculate force constants (bond and angle parameters) from Gaussian output files.

What Does This Script Do?
Recursively explores your folder structure up to a user-defined depth (depth_degree), searching for subfolders containing exactly one .chk file and one .log file.

Converts .chk files to .fchk format using formchk.

Copies, renames, and organizes all inputs required for the Modified Seminario Method, then runs the main protocol (modified_Seminario_method.py) for each system.

Supports Gaussian 09 and Gaussian 16 .chk files, with optional environment management to ensure Gaussian 09 compatibility.

Results are produced in standard GAFF/Amber units for force field development.

Requirements
Python 3.

Gaussian utilities available in your environment (formchk) and access to Gaussian module management (gaussian/09 and/or gaussian/16) if needed.

The external repository Python_Modified_Seminario_Method (containing modified_Seminario_method.py).

Run this script from your project root directory—the location containing all system folders to process.

Expected Folder Structure
Suppose your files are organized as follows:

project_root/
│
├── Automation_Seminario_Mod_Method.py
├── Python_Modified_Seminario_Method/
│    └── modified_Seminario_method.py
├── system1/
│    └── [subdirectories]/
├── system2/
│    └── [subdirectories]/
└── ...
The script searches for the required .chk and .log in folders located at the depth_degree you specify.

Examples:

depth_degree = 0: looks in system1/, system2/, etc.

depth_degree = 2: searches two subfolder levels deep.

Input File Requirements
Each processing folder must contain:

Exactly one .chk file (checkpoint from Gaussian 09 or 16).

Exactly one .log file (Gaussian output).

The folder may contain other files, but only one of each of the above is considered—folders with more will be skipped to avoid ambiguity.

How to Use
From your project root, run:

python Automation_Seminario_Mod_Method.py
You will be prompted to answer:

Depth Degree (depth_degree): Which subfolder level contains the .chk and .log files?

Gaussian Environment Management: If your checkpoints are from Gaussian 16 and you need to ensure compatibility with the Seminario method, answer yes to switch the environment to Gaussian 09 automatically.

Path to Python_Modified_Seminario_Method: Provide the path to the folder housing modified_Seminario_method.py.

What Happens Internally
The script runs formchk to convert .chk to .fchk within each relevant subfolder.

A mod_seminario/ligand directory is created for every system, and input files are copied and renamed as lig.fchk, lig.log.

The Modified Seminario Method script (modified_Seminario_method.py) is executed, and results are stored back into each system’s folder structure.

All names are handled generically—no dependency on folder or file naming conventions.

Output
Results will appear under each processed system’s mod_seminario/ directory.

The result units are, as explained by github.com/aa840 in the "ModSeminario_Py":  
  **Stretching** / **Bond** Parameters **(kcal/mol/Å²)**  
  **Bending** / **Angle** Parameters **(kcal/mol/rad²)**  
  Note that the units match Amber GAFF ForceField  

Additional Notes
Folder Names: Script is not dependent on directory names, only the folder depth for file discovery.

Multiple Files: If a folder at the chosen depth contains more than one .chk or .log, it is skipped for your safety.

Environment: If running in an HPC or cluster environment, ensure required modules (Gaussian) are accessible.

The result units are, as explained by github.com/aa840 in the "ModSeminario_Py":  
  **Stretching** / **Bond** Parameters **(kcal/mol/Å²)**  
  **Bending** / **Angle** Parameters **(kcal/mol/rad²)**  
  Note that the units match Amber GAFF ForceField  
  
Messages or emails (**richardlopezcorbalan@gmail.com**) will be answered in order to solve any kind of question.  

  
