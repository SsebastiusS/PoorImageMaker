## CLI manual

### Step  1: Open Command Prompt or Terminal
Open the Command Prompt on Windows or Terminal on macOS/Linux.

### Step  2: Navigate to the Directory Containing the Executable
Use the `cd` command to navigate to the directory where your `pimcli.exe` executable is located.

Example:
```
cd /path/to/your/executable
```

### Step  3: Run the Executable with Required Arguments
Run the executable with the `-i` flag followed by the directory path containing the images to merge, and the `-g` flag followed by the grid size in "RowsxColumns" format.

Example:
```
pim-cmd.exe -i "C:\Users\YourName\Images" -g 3x4
```

#### Flags:
- `-i` or `--input`: Specifies the directory path containing the images to merge.
- `-g` or `--grid`: Specifies the grid size for the merged image.
- `-b` or `--bulk`: Enables bulk processing of subdirectories.
- `-h` or `--help`: Prints help.

### Step  4: Confirm Bulk Processing (Optional)
If you use the `-b` flag, the program will prompt you to confirm the bulk processing operation. Type 'y' to proceed, or 'n' to cancel.

### Step  5: Review the Output
After the process is complete, the merged image will be saved as 'MergedOutput.png' in the specified input directory. If the -b flag was used, each subdirectory will contain its respective 'MergedOutput.png'.

### Additional Notes:
Ensure that the grid size matches the number of images in the directory. Otherwise, the merged image may contain empty tiles or skip some images.
Use quotes around paths that contain spaces to avoid errors.
On Linux, outside of needing wine or other means of running *.exe files you may need to give the executable permission to run using the `chmod +x pimcli` command before you can execute it.
