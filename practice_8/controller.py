import user
import funcs



user_choice = user.menu()
if user_choice == '1':
    funcs.add_info()
elif user_choice == '2':
    funcs.find_num()
elif user_choice == '3':
    funcs.del_num()
elif user_choice == '4':
    funcs.show_all()


