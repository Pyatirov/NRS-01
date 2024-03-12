import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def generate_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Определение вершин и граней октаэдра
    vertices = np.array([
        [-1, 0, 0],
        [1, 0, 0],
        [0, -1, 0],
        [0, 1, 0],
        [0, 0, -1],
        [0, 0, 1]
    ])

    faces = [[vertices[i] for i in face] for face in [
        [0, 2, 4],
        [0, 3, 4],
        [1, 2, 4],
        [1, 3, 4],
        [0, 2, 5],
        [0, 3, 5],
        [1, 2, 5],
        [1, 3, 5]
    ]]

    ax.add_collection3d(Poly3DCollection(faces, facecolors='darkgrey', linewidths=0.3, edgecolors='k', alpha=0.6))

    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Создание главного окна tkinter
window = tk.Tk()
window.geometry("800x600")
window.title("Отображение октаэдра с помощью Matplotlib")

# Создание кнопки для отображения октаэдра
btn_generate = tk.Button(window, text="Отобразить октаэдр", command=generate_cube)
btn_generate.pack()

# Запуск главного цикла
window.mainloop()
