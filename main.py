from MainWindow import MainWindow
from Request import Request




request = Request()
#response = request.new_user("my_login", "my_password")
while True:
    a=str(input())
    response = request.message(a)




#start = MainWindow()