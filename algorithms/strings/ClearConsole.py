import os

CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# call to CC() to clear console on (Almost) EVERY operating system
