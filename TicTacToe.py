from Ui import Gui, Terminal
from sys import argv

def usage():   
    print(f"""
Usage: {argv[0]} [g | t]
g : play with the GUI
t : play with the Terminal""")
    quit()


# changed comment here
if __name__ == "__main__":
    t = Terminal()
    t.run()


