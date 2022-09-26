import gui
import controller
import model


str = gui.get_value_from_user()

controller.save_data(str)

gui.print_data(str)

res = model.calculator(str)
s = ''.join(res)
controller.save_data(s)

gui.print_data(res)

