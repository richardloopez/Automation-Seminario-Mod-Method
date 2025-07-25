# Automation_Seminario_mod.py

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
  
Messages or emails (**richardlopezcorbalan@gmail.com**) will be answered in order to solve any kind of question.  









# seminario_calculations.py

This Python script automates the aggregation and statistical analysis of parameters produced by the Modified Seminario Method across multiple molecular systems. It is designed to streamline the comparison and averaging of force constants from different calculations, and to provide statistical measures directly usable for force field development or later analysis.

What Does This Script Do?
Recursively scans a directory tree at a user-specified depth to find parameter files named either Bonds or Angle, as generated by the Modified Seminario Method for each molecular system.

Extracts bond and angle parameters (force constants and equilibrium values) for each unique parameter type, across all molecular systems found.

Computes statistics: mean, absolute error of the mean, and relative error of the mean, for each parameter across all molecules.

Outputs two consolidated CSV files (consolidated_bonds.csv and consolidated_angle.csv), listing all bond/angle types, individual values per molecule, and full statistics for each.

Requirements
Python 3 (no additional dependencies outside the standard library).

Multiple folders (or subfolders) containing Bonds and/or Angle files with parameter values—these should have been generated, typically, by the Modified Seminario Method workflow.

Expected Folder Structure
Suppose you have results from several calculations organized within a directory tree, such as:


project_root/

├── molecule1/

│   └── mod_seminario/

│       ├── Bonds

│       └── Angle

├── molecule2/

│   └── mod_seminario/

│       ├── Bonds

│       └── Angle

├── molecule3/

│   └── mod_seminario/

│       └── ...

...

This script uses the depth_grade parameter to decide where (how deep in your folder tree) to look for Bonds and Angle files.

Input File Requirements
Each target folder at the specified depth should contain a Bonds and/or Angle file.

Bonds file: Each line should have the format:
atoms k eq num1 num2
where k is the bond force constant, eq is the equilibrium distance, and num1, num2 are atom indices/labels.

Angle file: Each line should have the format:
atoms k eq num1 num2 num3
where k is the angle force constant, eq is the equilibrium angle, and num1, num2, num3 are atom indices/labels.

Example lines:

From Bonds: C-H 340.0 1.09 1 2

From Angle: H-C-H 33.0 109.5 1 2 3

The actual atoms label is not required by the code and is ignored after splitting.

Usage
Run the script (from any location):

python consolidate_seminario_parameters.py
At startup, the script will prompt you for:

root directory path: The folder where your calculations start (e.g., project_root/ above).

depth grade: An integer indicating folder depth from the root where to look for Bonds and Angle files. E.g., if your files are two levels below the root, enter 2.

The script will then process all found files and create:

consolidated_bonds.csv

consolidated_angle.csv

These CSV files will contain, for each parameter type:

The index/label (atom numbers)

The force constants and equilibrium values for each system

The average (mean) and statistical errors, using sample standard deviation.

CSV header columns:

Number: unique key for the bond/angle (atom indices)

[molecule]_k(): force constant for that molecule

[molecule]_eq(): equilibrium value for that molecule

Statistics for mean, absolute error (s/√n), and relative error for both force constants and equilibrium values

Output Example

Number,molecule1_k(),molecule1_eq(),molecule2_k(),molecule2_eq(),...,Mean_k(),Mean_eq(),AbsError_k(),AbsError_eq(),RelError_k(%),RelError_eq(%)
1 2,340.0,1.09,345.0,1.08,...,342.5,1.085,2.5,0.005,0.73,0.46
Notes
Folder and molecule names are derived automatically from their path and require no naming convention.

If a system is missing a bond/angle present in another, its value will be left blank in the CSV.

Formulas used are explicitly written at the top of each CSV for transparency and reproducibility.

The script is robust to missing or extra files—only valid lines and unique parameter definitions are included.
  
