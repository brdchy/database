import tkinter as tk
from tkinter import Entry

from Request import Request



class InputWindow:
    def __init__(self, request, width=900, height=700):
        self.request = request
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("InputWindow")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='pink')
        self.name_valid = False
        self.number_valid = False

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
        self.canvas.create_text((x1 + x2) // 2, y1 - 10, text="═" * (x2 - x1), font=("Courier New", 12), fill="white")
        # нижняя горизонтальная линия
        self.canvas.create_text((x1 + x2) // 2, y2 + 10, text="═" * (x2 - x1), font=("Courier New", 12), fill="white")
        # левая вертикальная линия
        self.canvas.create_text(x1 - 10, (y1 + y2) // 2, text="\n".join(["║"] * (y2 - y1)), font=("Courier New", 12),
                                fill="white")
        # правая вертикальная линия
        self.canvas.create_text(x2 + 10, (y1 + y2) // 2, text="\n".join(["║"] * (y2 - y1)), font=("Courier New", 12),
                                fill="white")

    def create_buttons(self):
        # создаем кнопки
        button1 = tk.Button(self.root, text="Ok", width=15, height=3, font=("Arial", 9), command=self.save_InputWindow)
        button2 = tk.Button(self.root, text="Cancel", width=15, height=3, font=("Arial", 9), command=self.close_InputWindow)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width // 2 - 300, self.height // 2 + 300, window=button1)
        self.canvas.create_window(self.width // 2 + 300, self.height // 2 + 300, window=button2)

    # команда для кнопки OK
    def save_InputWindow(self):
        self.validate_name()
        self.validate_number()
        if not self.name_valid:
            self.show_error_window("Name must contain only letters. Please try again.")
            return

        if not self.number_valid:
            self.show_error_window("Number must be equal to 11 characters and contain only numbers. Please try again.")
            return

        if self.number_valid and self.name_valid:
            
            number = self.number_entry.get()
            name = self.name_entry.get()
            # тут наебучи нужно еще передовать стол
            time = self.selected_time.get()
            notes = self.notes_entry.get('1.0', 'end-1c')
            self.request.new_booking(name, number, time, notes)

       
        

    def close_InputWindow(self):
        # Скрываем главное окно
        self.root.withdraw()

    # устанавливаем параметры для окна ошибок
    def show_error_window(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x150")

        error_message = tk.Message(error_window, text=message, width=250, font=("Arial", 12))
        error_message.pack(pady=10)

        button_frame = tk.Frame(error_window)
        button_frame.pack()

        ok_button = tk.Button(button_frame, text="OK", command=error_window.destroy)
        ok_button.pack(pady=5)

    # валидация номера
    def validate_number(self):
        number = self.number_entry.get()
        if number.isdigit() and len(number) == 11:  # Проверяем, что номер состоит только из цифр и имеет длину 11 символов
            self.number_valid = True
        else:
            self.number_valid = False

    # валидация имени
    def validate_name(self):
        name = self.name_entry.get()
        if any(char.isdigit() or not char.isalpha() for char in name):
            self.name_valid = False
        else:
            self.name_valid = True

    def create_input_field(self):
        # блок с названиями
        frame1 = tk.Frame(self.root, background="pink")

        tk.Label(frame1, text="Name:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.E, pady=10)
        tk.Label(frame1, text="Phone number:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, pady=10)
        tk.Label(frame1, text="Table:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.E, pady=10)
        tk.Label(frame1, text="Time:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.E, pady=10)
        tk.Label(frame1, text="Notes:", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.NE, pady=10)
        self.canvas.create_window(200, 300, window=frame1)

        # блок с полями ввода
        frame2 = tk.Frame(self.root, background="pink")

        self.name_entry = Entry(frame2, width=40, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, pady=10)
        self.name_entry.bind("<FocusOut>", lambda event: self.validate_name())

        self.number_entry = Entry(frame2, width=40, font=("Arial", 12))
        self.number_entry.grid(row=1, column=1, pady=10)
        self.number_entry.bind("<FocusOut>", lambda event: self.validate_number())

        #выпадающий список свободных столов
        self.selected_table = tk.StringVar(frame2)
        tables = ["", "1", "2", "3", "4", "5"]
        self.selected_table.set(tables[0])
        tables_menu = tk.OptionMenu(frame2, self.selected_table, *tables)
        tables_menu.config(width=40, font=("Arial", 11))
        tables_menu.grid(row=2, column=1, pady=10)
        

        # выпадающий список времени столов
        self.selected_time = tk.StringVar(frame2)
        times = ["", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
        self.selected_time.set(times[0])
        time_menu = tk.OptionMenu(frame2, self.selected_time, *times)
        time_menu.config(width=40, font=("Arial", 11))
        time_menu.grid(row=3, column=1, pady=10)

        self.notes_entry = tk.Text(frame2, width=40, height=3, font=("Arial", 12))
        self.notes_entry.grid(row=4, column=1, pady=10)

        self.canvas.create_window(500, 315, window=frame2)

