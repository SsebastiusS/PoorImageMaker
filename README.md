# PoorImageMerger README

## Introduction

Welcome to PoorImageMerger, a tool designed to merge multiple images into a single image. 

This program offers both a Graphical User Interface (GUI) version and a Command Line Interface (CLI) version to cater to different user preferences.

The CLI version allows bulk merging of multiple directories and subdirectories, offering batch processing of images.

## Grid Merge logic

   - The sorted images are placed next to each other in a grid based on the specified format (RowsxColumns)
   - For example, with files 1.png, 2.png, 3.png, and 4.png:
     - A grid setting of 2x2 would merge them as follows:
       ```
       1.png  2.png
       3.png  4.png
       ```
     - A grid setting of 4x1 would merge them in a single column:
       ```
       1.png  
       2.png 
       3.png 
       4.png
       ```
       And 1x4 would merge in a single row
       ```
       1.png, 2.png, 3.png, and 4.png
       ```

This logic allows you to control how your images are arranged in the merged result. Simply set the grid format according to your preference, and the images will be combined accordingly.

## Supported File Types

The application supports the following file types: PNG, JPG, JPEG, and WebP.

## Notes

The application automatically sorts images based on their filenames, so ensure proper numbering for accurate merging.
If you encounter any issues or have further questions, contact sebastius on discord.
ifferent file extensions in the same directory might lead to sorting issues on certain non-Windows OS.

## Manuals
[GUI Manual](GUImanual.md)
[CLI Manual](CLImanual.md)

## [Download](https://cdn.discordapp.com/attachments/1204872273685774356/1205127798713491476/PoorImageMerger.zip)
