import tkinter as tk
import time

def start_joke():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    
    # The label that will move
    label = tk.Label(root, text="HELLO", fg="lime", bg="black", font=("Arial", 50, "bold"))
    label.place(x=0, y=100)

    start_time = time.time()
    speed = 5
    x_pos = 0
    direction = 1
    
    # Movement loop for 20 seconds
    while time.time() - start_time < 20:
        # Calculate new position
        x_pos += (speed * direction)
        
        # Bounce off the edges of the screen
        if x_pos > root.winfo_screenwidth() - 200 or x_pos < 0:
            direction *= -1
            speed += 2  # Speed up every time it hits a wall
            
        label.place(x=x_pos, y=root.winfo_screenheight() // 2)
        root.update()
        time.sleep(0.01)

    # Transition to the joke message
    label.config(text="IT'S A JOKE!", fg="red")
    label.place(x=root.winfo_screenwidth()//2 - 150, y=root.winfo_screenheight()//2)
    root.update()
    
    time.sleep(1.5) # Let them see the "Joke" text for a split second
    root.destroy() # Close immediately

if __name__ == "__main__":
    start_joke()