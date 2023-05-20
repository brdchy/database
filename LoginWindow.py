import tkinter as tk

from BookWindow import BookWindow
from tkinter import Entry

class LoginWindow:
    def __init__(self, width=900, height=700):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("LoginWindow")
        self.root.geometry(f"{width}x{height}")
        self.root.configure(background='pink')
        self.login_valid = False
        self.password_valid = False

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
        button1 = tk.Button(self.root, text="Ok", width=15, height=3, font=("Arial", 9), command=self.open_book_window)
        button2 = tk.Button(self.root, text="Cancel", width=15, height=3, font=("Arial", 9), command=self.close_LoginWindow)

        # добавляем кнопки на Canvas
        self.canvas.create_window(self.width // 2 - 300, self.height // 2 + 300, window=button1)
        self.canvas.create_window(self.width // 2 + 300, self.height // 2 + 300, window=button2)

    def check_credentials(self):
        # чтение пользователей из файла
        with open("users.txt", "r") as file:
            users = file.readlines()

        # перебор пользователей, чтобы найти совпадение логина и пароля
        for user in users:
            login, password, role = user.strip().split(",")
            if login == self.username_input.text() and password == self.password_input.text():
                if role == "admin":
                    # открыть окно администратора
                    self.admin_window = BookWindow() # пока что это для проверки условия
                else:
                    # открыть окно пользователя
                    self.user_window = BookWindow()
                return True



    def close_LoginWindow(self):
        # Скрываем главное окно
        self.root.withdraw()

    # команда для кнопки OK
    def open_book_window(self):
        self.validate_login()
        self.validate_password()

        if not self.login_valid:
            self.show_error_window("Wrong login. Try again")
            return

        if not self.password_valid:
            self.show_error_window("Wrong password. Try again")
            return
        # Скрываем главное окно
        self.root.withdraw()
        # создаем экземпляр класса AddWindow
        BookWindow()
        # Показываем главное окно после закрытия окна AddWindow
        self.root.deiconify()

    # устанавливаем параметры для окна ошибок
    def show_error_window(self, message):
        error_window = tk.Toplevel(self.root)
        error_window.title("Error")
        error_window.geometry("300x150+350+500")

        error_message = tk.Message(error_window, text=message, width=250, font=("Arial", 12))
        error_message.pack(pady=10)

        button_frame = tk.Frame(error_window)
        button_frame.pack()

        ok_button = tk.Button(button_frame, text="OK", command=error_window.destroy)
        ok_button.pack(pady=5)

    # валидация логина
    def validate_login(self):
        login = self.login_entry.get()
        if len(login) < 6 or not login.isalnum():
            self.login_valid = False
        else:
            self.login_valid = True

    # валидация пароля
    def validate_password(self):
        password = self.password_entry.get()
        if len(password) < 8 or not password.isalnum():
            self.password_valid = False
        else:
            self.password_valid = True

    def create_input_field(self):
        # блок с названиями
        frame1 = tk.Frame(self.root, background="pink")

        tk.Label(frame1, text="Login:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.E, pady=10)
        tk.Label(frame1, text="Password:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, pady=10)

        self.canvas.create_window(200, 300, window=frame1)

        # блок с полями ввода
        frame2 = tk.Frame(self.root, background="pink")

        self.login_entry = Entry(frame2, width=50, font=("Arial", 12))
        self.login_entry.pack(pady=10)
        self.login_entry.bind("<FocusOut>", lambda event: self.validate_login())

        self.password_entry = Entry(frame2, width=50, font=("Arial", 12))
        self.password_entry.pack(pady=10)
        self.password_entry.bind("<FocusOut>", lambda event: self.validate_password())

        self.canvas.create_window(500, 300, window=frame2)

