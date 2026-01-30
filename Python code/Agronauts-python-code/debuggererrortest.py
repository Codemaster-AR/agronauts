# # import turtle
# # import time
# # import _tkinter

# # # --- Setup ---
# # screen = turtle.Screen()
# # screen.setup(width=800, height=800)
# # screen.bgcolor("black")wwww
# # screen.title("Recursive C-Curve Fractal")
# # screen.colormode(255)  # Use RGB for colors

# # t = turtle.Turtle()
# # t.speed(0)  # Maximize drawing speed (0 is fastest)
# # t.penup()
# # t.goto(-100, 0)
# # t.pendown()
# # t.color("cyan")  # Use a named color or RGB tuple

# # # --- Recursive Function ---
# # def c_curve(t, order, length, switch=1):
# #     """
# #     Draws a C-Curve fractal recursively.

# #     t: The turtle object.
# #     order: The recursion depth (higher is more detailed).
# #     length: The length of the base segment.
# #     switch: Determines the direction of the turn (+1 or -1).
# #     """
# #     if order == 0:
# #         t.forward(length)
# #     else:
# #         t.right(45 * switch)
# #         c_curve(t, order - 1, length / 1.41421356, -switch)
# #         t.left(90 * switch)
# #         c_curve(t, order - 1, length / 1.41421356, -switch)
# #         t.right(45 * switch)

# # # --- Drawing and Execution ---
# # FRACTAL_ORDER = 12
# # BASE_LENGTH = 300

# # t.pensize(1)

# # c_curve(t, FRACTAL_ORDER, BASE_LENGTH, 1)

# # # Keep the window open
# # turtle.done()
# # import python_http_client
# # import python_http_client.exceptions
# # import json

# import os
# import matplotlib.pyplot as plt
# import numpy as np

# def process_gpr_image(file_path):
#     """
#     Reads and processes the image data from the given path.
#     The image is converted to a 2D intensity array (grayscale) suitable 
#     for GPR analysis.
#     """
#     if not os.path.exists(file_path):
#         print(f"❌ Error: File not found at path: {file_path}")
#         return None
        
#     try:
#         # 1. Read the image into a NumPy array
#         img_data = plt.imread(file_path)
        
#         print(f"✅ Image loaded successfully from: {os.path.basename(file_path)}")
#         print(f"Shape of the original data: {img_data.shape}")
        
#         # 2. Pre-processing: Convert to Grayscale (Intensity)
        
#         # Drop the alpha channel if present (4 channels -> 3 channels)
#         if img_data.ndim == 3 and img_data.shape[2] == 4:
#             img_data = img_data[:, :, :3]
            
#         # Convert to Grayscale if it's a color image (3 channels -> 1 channel)
#         if img_data.ndim == 3:
#             # Standard luminance formula for grayscale conversion
#             # Resulting array is 2D (Depth vs. Distance)
#             gray_data = np.dot(img_data[...,:3], [0.2989, 0.5870, 0.1140])
#             print("Converted image to Grayscale (2D array) for processing.")
#             return gray_data
        
#         # If it was already 1 channel (grayscale), return it directly
#         return img_data

#     except Exception as e:
#         print(f"❌ An error occurred while reading the file: {e}")
#         return None

# # --- Main Script Loop ---

# def gpr_reader_cli():
#     """Main command-line interface for the GPR reader."""
#     gpr_array = None
    
#     print("Welcome to the GPR Image Reader.")
#     print("Type 'upload <file_path>' to load an image, or 'exit' to quit.")
#     print("\n💡 **Examples:**")
#     print("   Windows: upload C:\\Data\\profile.png")
#     print("   Linux/macOS: upload /home/user/data/profile.png")
    
#     while True:
#         user_input = input("\n> ").strip()
        
#         # 1. Handle the 'exit' command
#         if user_input.lower() == 'exit':
#             print("Exiting GPR Reader. Goodbye!")
#             break
            
#         # 2. Handle the 'upload <file_path>' command
#         if user_input.lower().startswith('upload '):
#             # Split the input into the command and the path
#             parts = user_input.split(maxsplit=1)
            
#             if len(parts) < 2:
#                 print("⚠️ Please provide the full path after 'upload'.")
#                 continue
            
#             # Remove any extra quotes the user might have included
#             file_path = parts[1].strip().replace('"', '').replace("'", '')
            
#             # Call the processing function
#             gpr_array = process_gpr_image(file_path)
            
#             if gpr_array is not None:
#                 print("\n**Image successfully loaded and processed.**")
                
#                 # Show the result for confirmation
#                 plt.figure()
#                 plt.imshow(gpr_array, cmap='gray', aspect='auto')
#                 plt.title("Loaded GPR Profile (Intensity)")
#                 plt.xlabel("Distance Axis (Pixels)")
#                 plt.ylabel("Depth/Time Axis (Pixels)")
#                 plt.colorbar(label='Amplitude/Intensity')
#                 plt.show()
                
#         else:
#             print("Unknown command. Type 'upload <file_path>' or 'exit'.")

# # Run the script
# if __name__ == "__main__":
#     gpr_reader_cli()
import os
from google import genai
from google.genai import types

# 🚨 SECURITY WARNING: Hardcoding your API key is a security risk. 
# Only use this for temporary, local testing.
# REPLACE "YOUR_HARDCODED_API_KEY_HERE" with your actual Gemini API key.
YOUR_API_KEY = "AIzaSyC7Y4W06hbx8sUeWzxK168fKoVaJjjjXNw"

# --- 1. Client Initialization with Hardcoded Key ---
try:
    # Pass the API key directly to the client constructor
    client = genai.Client(api_key=YOUR_API_KEY)
except Exception as e:
    print("--- API KEY ERROR ---")
    print("Failed to initialize the Gemini client. Ensure your hardcoded key is correct.")
    print(f"Original Error: {e}")
    exit()

# --- 2. Get User Input for File Path ---
# Prompt the user for the image file path
image_path = input("Please enter the full path to your image file (e.g., /users/anay/radargram.png): ")

# --- 3. Read the Image File and Determine MIME Type ---
try:
    # Read the image from a local file in binary mode
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
    
    # Simple logic to determine MIME type based on file extension
    file_extension = os.path.splitext(image_path)[1].lower()
    if file_extension in ('.jpg', '.jpeg'):
        mime_type = 'image/jpeg'
    elif file_extension == '.png':
        mime_type = 'image/png'
    else:
        # Default to JPEG if not PNG or JPEG, or if the extension is unusual
        print(f"Warning: Unknown file type '{file_extension}'. Using image/jpeg as default MIME type.")
        mime_type = 'image/jpeg'
        
except FileNotFoundError:
    print(f"\nError: The file was not found at '{image_path}'. Please check the path and try again.")
    exit()
except Exception as e:
    print(f"\nAn unexpected error occurred while reading the file: {e}")
    exit()

# --- 4. Define the Detailed Prompt ---
gpr_prompt = (
    "Analyze this image in detail. If it is a Ground-Penetrating Radar (GPR) radargram, "
    "identify any clear hyperbolic reflections, their relative depth/location, and "
    "suggest the potential subsurface objects or features (e.g., rebar, pipe, void). "
    "If it is not a GPR image, simply describe its contents."
)

# --- 5. Generate Content ---
print("\n--- Sending Request to Gemini API... ---")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type=mime_type, 
        ),
        gpr_prompt
    ]
)

# --- 6. Print Result ---
print("\n====================================")
print("       ✨ GEMINI ANALYSIS RESULT ✨       ")
print("====================================")
print(response.text)
print("====================================")