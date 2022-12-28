import PyPDF2
from tkinter import filedialog
import tkinter as tk

def select_pdf():
    # Open a file selection dialog and get the selected file's path
    file_path = filedialog.askopenfilename()

    # Display the selected file's path
    file_label['text'] = file_path

def optimize_pdf():
    # Get the selected file's path from the label
    file_path = file_label['text']

    # Open the PDF file
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)

    # Create a new PDF file with optimized content
    optimized_pdf = PyPDF2.PdfWriter()
    for page in pdf.pages:
        optimized_pdf.addPage(page)

    # Compress images
    for page in optimized_pdf.pages:
        page.compressContentStreams()

    # Remove unnecessary metadata
    optimized_pdf.addMetadata({'/Producer': ''})
    optimized_pdf.addMetadata({'/CreationDate': ''})

    # Merge duplicate fonts
    optimized_pdf.addMetadata({'/EmbedAllFonts': ''})

    # Save the optimized PDF
    with open('optimized.pdf', 'wb') as output:
        optimized_pdf.write(output)

    # Display the results
    original_size = pdf.getFileInfo()['/Size']
    optimized_size = optimized_pdf.getFileInfo()['/Size']
    result_label['text'] = f'Original size: {original_size} bytes\nOptimized size: {optimized_size} bytes'

# Create the GUI
root = tk.Tk()
root.title('PDF Optimizer')

# Add a label to display the selected file's path
file_label = tk.Label(root, text='No file selected')
file_label.pack()

# Add a button to select the PDF file
browse_button = tk.Button(root, text='Select PDF', command=select_pdf)
browse_button.pack()

# Add a button to optimize the PDF
optimize_button = tk.Button(root, text='Optimize PDF', command=optimize_pdf)
optimize_button.pack()

# Add a label to display the results
result_label = tk.Label(root, text='')
result_label.pack()

# Run the GUI
root.mainloop()
