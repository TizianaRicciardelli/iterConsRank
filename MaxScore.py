import os
import csv
import sys

def extract_data(folder_path): # extract data from files in different folders 
    data = {}
    folder_id = os.path.basename(folder_path)
    for i in range(30,0, -1): # range of steps from 1 to 30
        file_path = os.path.join(folder_path, f"Zscore-0.85-{i}.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                first_line = file.readline().strip().split('\t')[1]
                data[i] = first_line
    return folder_id, data

def main(folder_file):
    output_csv = "MaxScore_all-30s_rev.csv" # output name and path
   
    all_data = [] # initialize list
  
    with open(folder_file, 'r') as file: # folders paths from a file
        folder_list = [line.strip() for line in file.readlines()]

    for folder_path in folder_list: # looping into the folders
        if os.path.isdir(folder_path):
            folder_id, folder_data = extract_data(folder_path) #apply function previously defined 
            folder_row = [folder_id] 
            for i in range(1, 31):
                if i in folder_data:
                    folder_row.append(folder_data[i])
                else:
                    folder_row.append(None)
            all_data.append(folder_row)

    with open(output_csv, 'w', newline='') as csvfile: # write the output file 
        writer = csv.writer(csvfile)
        writer.writerow(['Folder ID'] + [f"ID_{i}" for i in range(30, 0, -1)]) #first row with column headers
        writer.writerows(all_data)

    print("yay")

if __name__ == "__main__":
    folder_file = sys.argv[1]
    main(folder_file)
