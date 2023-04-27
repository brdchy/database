import tkinter as tk
class MainWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("MainWindow")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='pink')

        # создаем Canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        # устанавливаем фон Canvas
        self.canvas.config(bg='pink')

        self.draw_walls()
        self.create_buttons()
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
        button1 = tk.Button(self.root, text="Login", width=20, height=3, font=("Arial", 13), command=self.open_login_window)
        button2 = tk.Button(self.root, text="Registration", width=20, height=3, font=("Arial", 13), command=self.open_registration_window)
        button3 = tk.Button(self.root, text="Exit", width=8, height=2, command=self.close_window, font=("Arial", 10))

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2, self.height//2 - 100, window=button1)
        self.canvas.create_window(self.width//2, self.height//2, window=button2)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button3)

    def close_window(self):
        self.root.destroy()

    def open_login_window(self):
        # создаем экземпляр класса AddWindow
        LoginWindow()
    
    def open_registration_window(self):
        # создаем экземпляр класса AddWindow
        RegistrationWindow()


class RegistrationWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("MainWindow")
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
        button1 = tk.Button(self.root, text="Ok", width=15, height=3, font=("Arial", 9), command=self.close_RegistrationWindow)
        button2 = tk.Button(self.root, text="Cancel", width=15, height=3, font=("Arial", 9), command=self.close_RegistrationWindow)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2 - 300, self.height//2 + 300, window=button1)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button2)

    def close_RegistrationWindow(self):
        # Скрываем главное окно
        self.root.withdraw()

    def create_input_field(self):
        # блок с названиями 
        frame1 = tk.Frame(self.root, background="pink")
        
        tk.Label(frame1, text="Login:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Password:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, pady= 10)
        
        self.canvas.create_window(200, 300, window=frame1)
        
        # блок с полями ввода
        frame2 = tk.Frame(self.root, background="pink")

        self.login_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.login_entry.grid(row=0, column=1, pady= 10)
        
        self.password_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, pady= 10)
        
        self.canvas.create_window(500, 300, window=frame2)

class LoginWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("MainWindow")
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
        button1 = tk.Button(self.root, text="Ok", width=15, height=3, font=("Arial", 9), command=self.open_book_window)
        button2 = tk.Button(self.root, text="Cancel", width=15, height=3, font=("Arial", 9), command=self.close_LoginWindow)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2 - 300, self.height//2 + 300, window=button1)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button2)

    def close_LoginWindow(self):
        # Скрываем главное окно
        self.root.withdraw()

    def open_book_window(self):
        # Скрываем главное окно
        self.root.withdraw()
        # создаем экземпляр класса AddWindow
        BookWindow()
        # Показываем главное окно после закрытия окна AddWindow
        self.root.deiconify()

    def create_input_field(self):
        # блок с названиями 
        frame1 = tk.Frame(self.root, background="pink")
        
        tk.Label(frame1, text="Login:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Password:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, pady= 10)
        
        self.canvas.create_window(200, 300, window=frame1)
        
        # блок с полями ввода
        frame2 = tk.Frame(self.root, background="pink")

        self.login_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.login_entry.grid(row=0, column=1, pady= 10)
        
        self.password_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, pady= 10)
        
        self.canvas.create_window(500, 300, window=frame2)

class BookWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("MainWindow")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='pink')

        # создаем Canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        # устанавливаем фон Canvas
        self.canvas.config(bg='pink')

        self.draw_walls()
        self.create_buttons()
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
        button1 = tk.Button(self.root, text="Book", width=15, height=3, font=("Arial", 9), command=self.open_input_window)
        button2 = tk.Button(self.root, text="Cancel", width=15, height=3, font=("Arial", 9), command=self.close_BookWindow)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2, self.height//2, window=button1)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button2)

    def close_BookWindow(self):
        # Скрываем главное окно
        self.root.withdraw()

    def open_input_window(self):
        # Скрываем главное окно
        self.root.withdraw()
        # создаем экземпляр класса AddWindow
        InputWindow()
        # Показываем главное окно после закрытия окна AddWindow
        self.root.deiconify()

class InputWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("MainWindow")
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
        button1 = tk.Button(self.root, text="Ok", width=15, height=3, font=("Arial", 9))
        button2 = tk.Button(self.root, text="Cancel", width=15, height=3, font=("Arial", 9), command=self.close_InputWindow)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2 - 300, self.height//2 + 300, window=button1)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button2)

    def close_InputWindow(self):
        # Скрываем главное окно
        self.root.withdraw()

    def create_input_field(self):
        # блок с названиями 
        frame1 = tk.Frame(self.root, background="pink")
        
        tk.Label(frame1, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Phone number:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Time:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.E, pady=10)
        tk.Label(frame1, text="Notes:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.NE, pady= 10)
        self.canvas.create_window(200, 300, window=frame1)
        
        # блок с полями ввода
        frame2 = tk.Frame(self.root, background="pink")

        self.name_entry = tk.Text(frame2, width= 40, height=1, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, pady= 10)
        
        self.number_entry = tk.Text(frame2, width= 40, height=1, font=("Arial", 12))
        self.number_entry.grid(row=1, column=1, pady= 10)

        # выпадающий список
        self.selected_time = tk.StringVar(frame2)
        times = ["", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
        self.selected_time.set(times[0])
        time_menu = tk.OptionMenu(frame2, self.selected_time, *times)
        time_menu.config(width=40, font=("Arial", 11))
        time_menu.grid(row=2, column=1, pady=10)

        self.notes_entry = tk.Text(frame2, width= 40, height=3, font=("Arial", 12))
        self.notes_entry.grid(row=3, column=1, pady= 10)

        self.canvas.create_window(500, 315, window=frame2)

start = MainWindow()