import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Ventana de prueba")
ventana.geometry("400x400")

# Creamos un grafo de 400x400
canvas = tk.Canvas(ventana, width=400, height=400) # Creamos un canvas de 400x400
canvas.pack() # Empaquetamos el canvas

# Dibujamos una línea
canvas.create_line(10, 10, 200, 50, fill="red") # Dibujamos una línea (x1, y1, x2, y2)

# Dibujamos un rectángulo
canvas.create_rectangle(50, 50, 150, 100, fill="blue") # Dibujamos un rectángulo (x1, y1, x2, y2)

# Dibujamos un óvalo
canvas.create_oval(100, 100, 200, 150, fill="green") # Dibujamos un óvalo (x1, y1, x2, y2)

if __name__ == '__main__':
    ventana.mainloop()

