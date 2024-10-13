from settings import *


class Auth(StatesGroup):
    LoginInput = State()
    PasswordInput = State()
    LoginInput__auth = State()
    PasswordInput__auth = State()
    LoginAuthorizing = State()