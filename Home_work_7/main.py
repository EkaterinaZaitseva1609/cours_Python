import gui
import controller

while True:
    list_str = gui.get_command_from_user()
    print(list_str)
    controller.process_command(list_str)

