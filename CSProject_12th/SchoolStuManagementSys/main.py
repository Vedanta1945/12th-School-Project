from modsys import *

#looping the whole program
while True:
    display_menu()
    choice = input("\n" + smb.ARROW + fontcolor.cyan("Enter Your Choice : "))
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        about_us()
    elif choice == '7':
        print("\n" + smb.DONE + fontcolor.green("Thanks For Using Our Student Information System"))
        print(smb.WARN + fontcolor.red("Quitting...."))
        try:
            os.remove('raw_data.csv')
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
        time.sleep(2)
        quit()
    else:
           print("\n" + smb.WARN + fontcolor.red("Please, Enter A Valid Input !"))
           break
