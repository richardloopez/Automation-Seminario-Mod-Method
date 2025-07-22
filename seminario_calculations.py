#!/usr/bin/env python3

# Author: Richard Lopez Corbalan
# GitHub: github.com/richardloopez
# Citation: If you use this code, please cite Lopez-Corbalan, R

import os
import csv
from collections import defaultdict
import statistics
import math

def collect_data(root_dir, depth_grade, file_type):
    data = defaultdict(dict)
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        depth = dirpath[len(root_dir):].count(os.sep)
        if depth == depth_grade:
            molecule_name = os.path.basename(os.path.dirname(os.path.dirname(dirpath)))
            
            for file in filenames:
                if file.endswith(file_type):
                    with open(os.path.join(dirpath, file), 'r') as f:
                        for line in f:
                            parts = line.split()
                            if file_type == "Bonds" and len(parts) == 5:
                                atoms, k, eq, num1, num2 = parts
                                key = f"{num1} {num2}"
                                data[key][molecule_name] = (float(k), float(eq))
                            elif file_type == "Angle" and len(parts) == 6:
                                atoms, k, eq, num1, num2, num3 = parts
                                key = f"{num1} {num2} {num3}"
                                data[key][molecule_name] = (float(k), float(eq))
    
    return data

def calculate_stats(values):
    if values and len(values) > 1:
        mean = statistics.mean(values)
        std_dev = statistics.stdev(values)
        abs_error = std_dev / math.sqrt(len(values))
        rel_error = (abs_error / mean) * 100 if mean != 0 else 0
        return mean, abs_error, rel_error
    return 0, 0, 0

def write_consolidated_file(data, filename, molecules, file_type):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write formulas
        writer.writerow(["Formulas used:"])
        writer.writerow(["Mean: sum(x) / n"])
        writer.writerow(["Absolute Error of the Mean: s / √n"])
        writer.writerow(["Relative Error of the Mean: (Absolute Error / Mean) * 100%"])
        writer.writerow(["Where s is sample standard deviation, n is number of observations"])
        writer.writerow([])  # Empty row for separation

        # Write header
        header = ['Number'] + [f"{molecule}_k()" for molecule in molecules] + [f"{molecule}_eq()" for molecule in molecules]
        header += ['Mean_k()', 'Mean_eq()', 'AbsError_k()', 'AbsError_eq()', 'RelError_k(%)', 'RelError_eq(%)']
        writer.writerow(header)
        
        # Write data
        for key, molecule_data in data.items():
            row = [key]
            k_values = []
            eq_values = []
            for molecule in molecules:
                if molecule in molecule_data:
                    k, eq = molecule_data[molecule]
                    k_values.append(k)
                    eq_values.append(eq)
                    row.extend([k, eq])
                else:
                    row.extend(['', ''])
            
            # Calculate and add statistics
            mean_k, abs_error_k, rel_error_k = calculate_stats(k_values)
            mean_eq, abs_error_eq, rel_error_eq = calculate_stats(eq_values)
            row.extend([mean_k, mean_eq, abs_error_k, abs_error_eq, rel_error_k, rel_error_eq])
            
            writer.writerow(row)

def main():
    root_dir = input("Enter the root directory path: ")
    depth_grade = int(input("Enter the depth grade: "))
    
    for file_type in ["Bonds", "Angle"]:
        data = collect_data(root_dir, depth_grade, file_type)
        
        # Get a sorted list of all molecule names
        molecules = sorted(set(molecule for data_item in data.values() for molecule in data_item.keys()))
        
        output_filename = f"consolidated_{file_type.lower()}.csv"
        write_consolidated_file(data, output_filename, molecules, file_type)
        
        print(f"Consolidated file has been created: {output_filename}")

if __name__ == "__main__":
    main()

