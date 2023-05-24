import tkinter as tk
from tkinter import messagebox
from Request import Request
from tkinter import Entry




class AdminWindow:
    def __init__(self, request, width=900, height=700):
        self.width = width
        self.height = height
        self.request = request
        self.root = tk.Tk()
        self.root.title("Admin Window")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='pink')

        # создаем Canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        # устанавливаем фон Canvas
        self.canvas.config(bg='pink')

        self.draw_walls()
        self.create_buttons()
        self.create_input_field()
        self.root.mainloop()
        
    
    def draw_walls(self):
        # размер отступа от края окна
        padding = 20
        # координаты угловых точек
        x1, y1 = padding, padding
        x2, y2 = self.width - padding, self.height - padding
        # верхняя горизонтальная линия
        self.canvas.create_text((x1+x2)//2, y1-10, text="═"*(x2-x1), font=("Courier New", 12), fill="white")
        # нижняя горизонтальная линия
        self.canvas.create_text((x1+x2)//2, y2+10, text="═"*(x2-x1), font=("Courier New", 12), fill="white")
        # левая вертикальная линия
        self.canvas.create_text(x1-10, (y1+y2)//2, text="\n".join(["║"]*(y2-y1)), font=("Courier New", 12), fill="white")
        # правая вертикальная линия
        self.canvas.create_text(x2+10, (y1+y2)//2, text="\n".join(["║"]*(y2-y1)), font=("Courier New", 12), fill="white")
        
    def create_buttons(self):
        # создаем кнопки
        button1 = tk.Button(self.root, text="Change", width=15, height=3, font=("Arial", 9), command=self.request.UnloadUsers)
        button2 = tk.Button(self.root, text="Cancel", width=15, height=3, font=("Arial", 9), command=self.close_AdminWindow)
        button3 = tk.Button(self.root, text="delete", width=15, height=3, font=("Arial", 9))#, #command=self.)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2 + 300, self.height//2, window=button1)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button2)
        self.canvas.create_window(self.width//2 + 300, self.height//2 - 70, window=button3)

    def create_input_field(self):
        
        # блок с названиями
        frame1 = tk.Frame(self.root, background="pink")

        tk.Label(frame1, text="Use:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.E, pady=10)
        self.canvas.create_window(100, 100, window=frame1)
        
        #создаётся выпадающий список
        user_list = self.request.UnloadUsers()
        frame2 = tk.Frame(self.root, background="pink")
        self.selected_user = tk.StringVar(frame2)
        users = [""]
        users.extend(user_list)
        self.selected_user.set(users[0])
        users_menu = tk.OptionMenu(frame2, self.selected_user, *users)
        users_menu.config(width=40, font=("Arial", 11))
        users_menu.grid(row=1, column=1, pady=10)
        self.canvas.create_window(500, 315, window=frame2)
        
    def close_AdminWindow(self):
        # Скрываем главное окно
        self.root.withdraw()
