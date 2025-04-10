from app.models import User

# Переменная хранит текущего пользователя
current_user = User(username="Line_1_Engineer", role="engineer")

def get_current_user():
    return current_user

def switch_user(username: str):
    global current_user
    current_user = User(username=username, role="engineer")
