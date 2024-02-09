from PIL import Image
import os
import glob
import sys
import argparse

# łączenie
def merge_images(image_paths, grid_size, output_path):
    print("Loading Images...")
    images = [Image.open(img_path) for img_path in image_paths]

    final_width = images[0].width * grid_size[1]  #kolumny
    final_height = images[0].height * grid_size[0]  #wiersze
    
    print("Generating new Image...")
    merged_image = Image.new('RGBA', (final_width, final_height))
    
    print("Merging Images...")
    for idx, img in enumerate(images):
        x_pos = (idx % grid_size[1]) * img.width
        y_pos = (idx // grid_size[1]) * img.height
        merged_image.paste(img, (x_pos, y_pos))
    
    print("Saving Merged Image...")
    merged_image.save(output_path, 'PNG')
    print("Success! Saved as {}".format(output_path))

# mielenie
def process_directory(input_dir, grid_size):
    print("Searching for Images in specified directory...")
    supported_formats = ('*.png', '*.jpg', '*.jpeg', '*.webp')
    image_files = []
    for ext in supported_formats:
        images_with_ext = sorted([f for f in glob.glob(f'{input_dir}/{ext}') if not f.endswith('MergedOutput.png')])
        image_files.extend(images_with_ext)
        image_files.sort(key=lambda x: os.path.splitext(os.path.basename(x))[0])

    if len(image_files) >  0:
        print("Found Images for merging.")
        total_tiles = grid_size[0] * grid_size[1]
        if len(image_files) != total_tiles:
            print(f"Error: Expected {total_tiles} Images but found {len(image_files)}. Confirm given grid size is correct.")
            return

        output_filename = f'{input_dir}/MergedOutput.png'
        merge_images(image_files, grid_size, output_filename)
    else:
        print("Error: No Images found in specified directory. Ensure the files being merged are one of the supported extensions.")

# mielenie bulkiem
def process_directory_bulk(input_dir, grid_size):
    print("Processing directories recursively...")
    for root, dirs, files in os.walk(input_dir):
        supported_formats = ('*.png', '*.jpg', '*.jpeg', '*.webp')
        image_files = []
        for ext in supported_formats:
            images_with_ext = sorted([f for f in glob.glob(f'{root}/{ext}') if not f.endswith('MergedOutput.png')])
            image_files.extend(images_with_ext)
            image_files.sort(key=lambda x: os.path.splitext(os.path.basename(x))[0])

        if image_files:
            print(f"Found Images for merging in directory: {root}")
            output_filename = f'{root}/MergedOutput.png'
            merge_images(image_files, grid_size, output_filename)
        else:
            print(f"No Images found in directory: {root}. Skipping.")

def main():
    parser = argparse.ArgumentParser(
        usage="%(prog)s -i INPUT_DIR -g [Rows]x[Columns] [-b]",
        description="Merge multiple images into one image using grid logic."
    )
    parser.add_argument('-i', '--input', required=True, help='Path to directory containing images to merge. Example: -i "/path/to/images"')
    parser.add_argument('-g', '--grid', required=True, help='Grid size in [Rows]x[Columns] format. Example: -g   3x4')
    parser.add_argument('-b', '--bulk', action='store_true', help='Enable bulk processing of subdirectories.')
    
    try:
        args = parser.parse_args()
    except SystemExit as e:
        return

    if args is None or not any(vars(args).values()):
        parser.print_help()
        print("\nError: No arguments provided. Please provide at least the input directory and grid size.")
        return

    input_dir = args.input
    grid_size = tuple(map(int, args.grid.split('x')))

    if args.bulk:
        print(f"\nWARNING: This will merge all the files in each subdirectory separately under '{input_dir}' with the grid size {args.grid}.")
        print("\nThe grid setting will create MergedOutput without checking if the grid size should be different among subdirectories.")
        print("\nThis may skip some images, improperly sort them, or create empty tiles in merged images if the subdirectories have inconsistent numbers of images.")
        confirmation = input("Are you sure you want to proceed? (Y/N): ")
        if confirmation.lower() == 'y':
            process_directory_bulk(input_dir, grid_size)
        else:
            print("Operation cancelled by user.")
    else:
        process_directory(input_dir, grid_size)
        
#main
if __name__ == "__main__":
    main()

