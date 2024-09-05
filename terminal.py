from os import *
from time import *

print("""
=========================
=                       =
=        SSH MOd.       =
=                       =
=========================
""")

sleep(0.5)

while True:
    terminal_S = input("local@root: ")
    system(f"{terminal_S}")
    sleep(0.1)
