# Importing those two to be able to clear the screen of the terminal.
from os import system, name

# Function that will clear the terminal.
def clear():
    # Clearing screen for Windows.
    if name == 'nt': 
        system('cls') 
  
    # Clearing screen for Mac and Linux.
    else: 
        system('clear') 