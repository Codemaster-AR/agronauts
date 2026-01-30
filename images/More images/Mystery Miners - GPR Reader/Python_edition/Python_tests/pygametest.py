import tkinter as tk
import pygame
import os

# --- 1. Pygame Setup (Initialization and Constants) ---
# Pygame needs a display environment, so we hide the default Tkinter window briefly
# to initialize Pygame without a default screen popping up.

# Set the window environment variable for embedding (crucial for Linux/X11)
os.environ['SDL_VIDEODRIVER'] = 'windib'  # Or 'x11' on some systems, 'windib' is common

pygame.init()

# Define Pygame display size
PYGAME_WIDTH = 400
PYGAME_HEIGHT = 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- 2. Main Tkinter Application Class ---
class PygameTkinterApp:
    def __init__(self, master):
        self.master = master
        master.title("Pygame Embedded in Tkinter")

        # Set up a Frame to hold the Pygame canvas
        self.pygame_frame = tk.Frame(master, width=PYGAME_WIDTH, height=PYGAME_HEIGHT)
        self.pygame_frame.pack(padx=10, pady=10)

        # Get the ID (handle) of the Tkinter frame window. This is the key step.
        self.window_id = self.pygame_frame.winfo_id()

        # Initialize Pygame Screen using the Tkinter Frame ID
        self.screen = pygame.display.set_mode((PYGAME_WIDTH, PYGAME_HEIGHT), 0, 32, window=self.window_id)
        pygame.display.set_caption("Pygame Canvas")
        
        # Game State Variables
        self.angle = 0
        self.clock = pygame.time.Clock()
        self.running = True

        # Add a Tkinter button below the Pygame display
        self.exit_button = tk.Button(master, text="Quit", command=self.quit_app)
        self.exit_button.pack(pady=5)
        
        # Start the Pygame update loop using Tkinter's after method
        self.update_pygame()

    def update_pygame(self):
        """Runs one iteration of the Pygame game loop."""
        
        # 1. Handle Events (Crucial for Pygame to respond to input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Note: Keyboard/mouse events will be handled by the Tkinter window first.
            # You may need to manually pass them to Pygame depending on the OS/setup.

        # 2. Update Game State
        self.angle += 1  # Spin the square
        if self.angle > 360:
            self.angle = 0
            
        # 3. Drawing/Rendering
        self.screen.fill(BLACK)

        # Draw a rotating red square
        square_surface = pygame.Surface((50, 50))
        square_surface.fill(RED)
        
        # Rotate the square
        rotated_surface = pygame.transform.rotate(square_surface, self.angle)
        
        # Calculate position to center it
        rect = rotated_surface.get_rect(center=(PYGAME_WIDTH // 2, PYGAME_HEIGHT // 2))
        
        self.screen.blit(rotated_surface, rect)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        self.clock.tick(60)

        # 4. Schedule the next update
        # Check if the app is still running before scheduling the next update
        if self.running:
            self.master.after(10, self.update_pygame) # Call itself every 10 milliseconds

    def quit_app(self):
        """Cleans up Pygame and destroys the Tkinter window."""
        self.running = False
        pygame.quit()
        self.master.destroy()
   
# --- 3. Run the Application ---
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    app = PygameTkinterApp(root)
    
    # Start the Tkinter main loop
    root.mainloop()
    # if the problem does not figure out try adding pygame.quit() here as well
    # pygame.quit()