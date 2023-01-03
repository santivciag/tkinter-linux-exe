import tkinter as tk
from app.utils.pyinstaller_paths import resource_path


app = tk.Tk()

canvas = tk.Canvas(app, bg="black", width=650, height=400)
canvas.pack()

bg_image = tk.PhotoImage(file = resource_path("img/car.png"))
canvas.create_image(0, 0, anchor = tk.NW, image = bg_image)

button = tk.Button(app, text="Click me!", command=lambda :print("Clicked!"))
button.config(bg="blue", fg="white", font=("Arial 18 bold italic"))
button.pack()

app.mainloop()