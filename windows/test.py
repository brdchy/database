import tkinter as tk
from tkinter import messagebox
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

        # рисуем стены
        self.draw_walls()
        # создаем кнопки
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


    def open_new_window(self):
        # Скрываем главное окно
        self.root.withdraw()
        # создаем экземпляр класса AddWindow
        add_window = AddWindow()
        # Показываем главное окно после закрытия окна AddWindow
        self.root.deiconify()

    def close_window(self):
        self.root.destroy()

    def create_buttons(self):
        # создаем кнопки
        button1 = tk.Button(self.root, text="Add", width=8, height=2, command=self.open_new_window)
        button2 = tk.Button(self.root, text="Vary", width=8, height=2)
        button3 = tk.Button(self.root, text="Delete", width=8, height=2)
        button4 = tk.Button(self.root, text="Exit", width=8, height=2, command=self.close_window)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2 - 300, self.height//2 + 300, window=button1)
        self.canvas.create_window(self.width//2 - 100, self.height//2 + 300, window=button2)
        self.canvas.create_window(self.width//2 + 100, self.height//2 + 300, window=button3)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button4)


class AddWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("AddWindow")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='pink')

        # создаем Canvas
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill="both", expand=True)
        # устанавливаем фон Canvas
        self.canvas.config(bg='pink')

        # рисуем стены
        self.draw_walls()

        #создаем поля ввода
        self.create_input_field()

         # создаем кнопки
        self.create_buttons()

        self.validate_input()

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

    def close_AddWindow(self):
        # Скрываем главное окно
        self.root.withdraw()
        # создаем экземпляр класса AddWindow
        add_window = MainWindow()
        # Показываем главное окно после закрытия окна AddWindow
        self.root.deiconify()
    
    # def save_data(self):
    #     name = self.name_entry.get()
    #     age = self.age_entry.get()
    #     address = self.address_entry.get()
    #     number = self.number_entry.get()
    #     email = self.email_entry.get()


    def create_input_field(self):
        # блок с названиями 
        frame1 = tk.Frame(self.root, background="pink")
        
        tk.Label(frame1, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Age:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Address:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Phone number:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Email address:", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.E, pady= 10)
        tk.Label(frame1, text="Notes:", font=("Arial", 12)).grid(row=5, column=0, sticky=tk.NE, pady= 10)
        
        self.canvas.create_window(100, 200, window=frame1)
        
        # блок с полями ввода
        frame2 = tk.Frame(self.root, background="pink")

        self.name_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, pady= 10)
        
        self.age_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.age_entry.grid(row=1, column=1, pady= 10)
        
        self.address_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.address_entry.grid(row=2, column=1, pady= 10)
        
        self.number_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.number_entry.grid(row=3, column=1, pady= 10)
        
        self.email_entry = tk.Text(frame2, width= 50, height=1, font=("Arial", 12))
        self.email_entry.grid(row=4, column=1, pady= 10)
        
        self.notes_entry = tk.Text(frame2, width= 50, height=3, font=("Arial", 12))
        self.notes_entry.grid(row=5, column=1, pady= 10)
        
        self.canvas.create_window(400, 217, window=frame2)

    # def validate_input(self):
    #     name = self.name_entry.get("1.0", tk.END).strip()
    #     age = self.age_entry.get("1.0", tk.END).strip()
    #     address = self.address_entry.get("1.0", tk.END).strip()
    #     phone_number = self.number_entry.get("1.0", tk.END).strip()
    #     email = self.email_entry.get("1.0", tk.END).strip()
    #     notes = self.notes_entry.get("1.0", tk.END).strip()

    #     # Валидация поля name
    #     if not name:
    #         messagebox.showerror("Error", "Please enter a name")
    #         return False

    #     # Валидация поля age
    #     try:
    #         age = int(age)
    #         if age < 0 or age > 100:
    #             raise ValueError
    #     except ValueError:
    #         messagebox.showerror("Error", "Please enter a valid age")
    #         return False

    #     # Валидация поля address
    #     if not address:
    #         messagebox.showerror("Error", "Please enter an address")
    #         return False

    #     # Валидация поля phone_number
    #     if not phone_number:
    #         messagebox.showerror("Error", "Please enter a phone number")
    #         return False

    #     # Валидация поля email
    #     if not email:
    #         messagebox.showerror("Error", "Please enter an email")
    #         return False
    #     elif "@" not in email:
    #         messagebox.showerror("Error", "Please enter a valid email")
    #         return False

    #     return True



    def create_buttons(self):
        # создаем кнопки
        button1 = tk.Button(self.root, text="Ok", width=8, height=2)
        button2 = tk.Button(self.root, text="Cancel", width=8, height=2, command=self.close_AddWindow)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width//2 - 300, self.height//2 + 300, window=button1)
        self.canvas.create_window(self.width//2 + 300, self.height//2 + 300, window=button2)

start = MainWindow()