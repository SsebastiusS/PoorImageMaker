from tkinter import filedialog, messagebox, Tk, Button, Entry, Label, StringVar, Text, Scrollbar, LabelFrame, END
from PIL import Image
import os
import glob
import sys 

def merge_images(image_paths, grid_size, output_path):
    print("Loading Images...")
    images = [Image.open(img_path) for img_path in image_paths]
    
   # Obliczanie rozmiaru siatki o podane wartości
    final_width = images[0].width * grid_size[1]  # Szerokość to liczba kolumn
    final_height = images[0].height * grid_size[0]  # Wysokość to liczba rzędów
    
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

# Funkcja do wybierania folderu przez użytkownika
def browse_folder():
    dir_path = filedialog.askdirectory()
    if dir_path:
        folder_entry.set(dir_path)

def start_merging():
    folder_path = folder_entry.get()
    grid_size_str = grid_entry.get()

    # Czy folder istnieje
    if not folder_path or not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid directory path. Please choose a valid directory.")
        return

    # Czy grid size jest dobrze sformatowany
    try:
        grid_size = grid_size_str.split('x')
        rows, columns = map(int, grid_size)
    except ValueError:
        messagebox.showerror("Error", "Invalid grid size format.\nPlease enter a valid grid size (e.g.'3x4').")
        return
    
    # Zeskanuj obrazki z folderu
    supported_formats = ('*.png', '*.jpg', '*.jpeg', '*.webp')
    image_files = []
    for ext in supported_formats:
        images_with_ext = sorted([f for f in glob.glob(f'{folder_path}/{ext}') if not f.endswith('MergedOutput.png')])
        image_files.extend(images_with_ext)
        image_files.sort(key=lambda x: os.path.splitext(os.path.basename(x))[0])

    # Zobacz czy grid jest dobrze skonfigurowany do ilości plików
    total_tiles = rows * columns
    if len(image_files) != total_tiles:
        messagebox.showerror("Error", f"Expected {total_tiles} Images but found {len(image_files)}. Confirm given grid size is correct.")
        return

    output_filename = f'{folder_path}/MergedOutput.png'
    merge_images(image_files, (rows, columns), output_filename)
    messagebox.showinfo("Success", "Images merged successfully!")

# printowanie stdout i stderr w terminalu
class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.config(state='normal')
        self.text_widget.insert('end', string)
        self.text_widget.see('end')  # Auto scroll to the bottom
        self.text_widget.config(state='disabled')
        self.text_widget.update_idletasks()

    def flush(self):
        pass

# Przekierowanie
def setup_stdout_redirect(text_widget):
    sys.stdout = StdoutRedirector(text_widget)
    sys.stderr = StdoutRedirector(text_widget)
   
# Placeholder clear na focusie
def clear_if_default(event):
    """Clear the entry widget if the current text matches the default."""
    if grid_entry.get() == "2x2":
        grid_entry.set('')
        
# tk
root = Tk()
root.title("PoorImageMerger")
root.resizable(False,False)

# Wybieranie folderu
folder_label = Label(root, text="Directory")
folder_entry = StringVar()
folder_entry_widget = Entry(root, textvariable=folder_entry)
folder_label.grid(row=0, column=0, sticky='e', padx=(10,   0), pady=(10,   0))
folder_entry_widget.grid(row=0, column=1, padx=(10,   0), pady=(10,   0))
browse_button = Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2, padx=(10,   10), pady=(10,   0))

# Konfiguracja siatki łączącej
grid_label = Label(root, text="Grid Size")
grid_label.grid(row=3, column=0, sticky='e', padx=(10,  0), pady=(10,  0))
grid_entry = StringVar()


# Placeholder
grid_entry.set("2x2")
grid_entry_widget = Entry(root, textvariable=grid_entry, fg='gray')
grid_entry_widget.bind("<FocusIn>", clear_if_default)
grid_entry_widget.grid(row=3, column=1, padx=(10,  0), pady=(10,  0))

# Guzik wykonania
merge_button = Button(root, text="Merge!", command=start_merging)
merge_button.grid(row=4, column=1, padx=(10,   10), pady=(10,    10))

# Guzik about
def show_about():
    messagebox.showinfo("About", "PoorImageMerger v1.0\n\nAuthor: Sebastius\n\nThis application is distributed under the MIT License, allowing you to freely use, modify, and distribute it without any obligations. Find more details in the 'LICENSE' file.")

about_button = Button(root, text="About", command=show_about)
about_button.grid(row=6, column=2, padx=(10,  10), pady=(10,  10))

# Terminal statusu
status_frame = LabelFrame(root, text="Status")
status_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# tekst
status_text = Text(status_frame, wrap='word', height=8, width=50, state='disabled', font=("Helvetica", 8))
status_scrollbar = Scrollbar(status_frame, orient='vertical', command=status_text.yview)
status_text['yscrollcommand'] = status_scrollbar.set
status_text.pack(side='left', fill='both', expand=True)
status_scrollbar.pack(side='right', fill='y')

#start
setup_stdout_redirect(status_text)
root.mainloop()
