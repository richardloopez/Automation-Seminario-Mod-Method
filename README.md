# Automation-Seminario-Mod-Method
Automates the execution of the Seminario Mod Method. It allows running the Seminario Mod Method across as many folders and subfolders as desired, with no limitations on folder structure.

Iterates in any folder it is launched untill the "**depth grade**" is reached. Depth grade is an input which tells this code where the archives (.log , .chk) are. This code is not completely free of some "folder architecture" because it will only search for the archives in the "last" subfolder of each iteration. Depth grade is a number ranging between [0 - infinite). For example: 
  First: In the same folder are Automation_Seminario_Mod_Method and i01/i01_A/i01_A_1
  
  depth grade = 0 archives should be in i01/
  depth grade = 1 archives should be in i01/i01_A
  depth grade = 2 archives should be in i01/i01_A/i01_A_1

  depth grade = 0 searching will be performed in all iXX/
  depth grade = 1 searching will be performed in i0XX/iXX_X
  depth grade = 2 searching will be performed in iXX/iXX_X/iXX_X_X

  Note that "X" represents an unknown way to name the path: This code is NOT name-dependent in any sense.

Both Seminario and Seminario_Mod use Guassian 09 formatted .chk (.fchk), but this code works with **BOTH** **Gaussian 09** and **Gaussian 16** .chk.
  If you use G09, you should disable G09 environment forcing (input to Question 2 = no)
  If you use G16, you should enable G09 environment forcing (input to Question 2 = yes)
  
Messages or emails (**richardlopezcorbalan@gmail.com**) will be answered in order to solve any kind of question.

  
