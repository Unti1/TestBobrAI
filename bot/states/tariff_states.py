from settings import *

class Tariff(StatesGroup):
    OutOfLimit = State()
    ProcessPayment = State()
    