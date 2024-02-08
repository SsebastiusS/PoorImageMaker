## GUI manual

### Step 1: Launch the Application 
Start the .exe file to start the tool.


### Step 2: Select Directory with Images to merge

1. Launch the application.
2. On the main screen, you will find a textbox labeled "Directory Path" and a "Browse" button next to it.
3. You can manually type the directory path in the textbox or click the "Browse" button to select the directory using a file dialog.

   #### Manual Entry:
   - Type the full path of the directory containing your images in the "Directory Path" textbox.

   #### Using the Browse Button:
   - Click the "Browse" button.
   - Navigate to the directory containing your images using the file dialog.
   - Select the desired directory and click "OK" or "Select" to confirm.


### Step 3: Configure Grid Size
Grid size format: "RowsxColumns"

Specify the desired grid size based on the number of rows and columns you want in the merged image.

Example: You have 12 images and wish to create one image that merges them into a grid with 3 rows and 4 columns. In the Grid size field, input "3x4".

### Step 4: Initiate Image Merge
Just press "Merge!" button on the bottom and it will merge images according to the configuration you provided in the selected Directory and produce "MergedOutput.png" file.

## CLI manual

### Step  1: Open Command Prompt or Terminal
Open the Command Prompt on Windows or Terminal on macOS/Linux.

### Step  2: Navigate to the Directory Containing the Executable
Use the `cd` command to navigate to the directory where your `pim-cmd.exe` (Windows) or `pim-cmd` (Linux) executable is located.

Example:
```
bash cd /path/to/your/executable
```

### Step  3: Run the Executable with Required Arguments
Run the executable with the `-i` flag followed by the directory path containing the images to merge, and the `-g` flag followed by the grid size in "RowsxColumns" format.

Example:
```
pim-cmd.exe -i "C:\Users\YourName\Images" -g 3x4
```

Or on Linux:
```
pim-cmd -i "/home/username/Images" -g 3x4

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
On Linux, you may need to give the executable permission to run using the `chmod +x pim-cmd` command before you can execute it.
