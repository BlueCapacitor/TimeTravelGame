"""
Created on Oct 10, 2020

@author: gosha
"""

from ui.display import Display


def set_up_and_run():
    display.current_page = display.Page.LEVEL_SELECT


if __name__ == '__main__':
    display = Display()
    display.title("Time Travel Game")

    display.after(0, set_up_and_run)
    display.mainloop()
