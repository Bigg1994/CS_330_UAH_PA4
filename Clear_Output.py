#########################################################
# clear output files
# Author: Garett Sutton
# Program Name: Clear_Output.py
# Python Version: 3.12
#########################################################

# List of text files to clear
files_to_clear = ["Scenario_1_Output_GS.txt", "Scenario_2_Output_GS.txt"]

# Loop through each file and clear its contents
for file in files_to_clear:
    with open(file, 'w') as f:
        # Opening file in write mode ('w') clears its contents
        pass

print("Contents of the files have been cleared.")