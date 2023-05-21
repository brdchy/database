from MainWindow import MainWindow
from Request import Request



request = Request()
response = request.new_user("my_login", "my_password")
print(response)
request.close()



start = MainWindow()