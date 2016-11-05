'''
Created on Oct 27, 2016

@author: Vlad
'''
from copy import deepcopy

'''
    Imports
'''

from iteration_3.backbone.functions import startup_initialization, add_apartment, display_apartment_options, display_certain, display_big_small, remove_options, replace_amount, sum_service_type, max_apartment_expense, sort_options, filter_options, check_number, undo_undo, undo


'''
    UI functions
'''

def _help_command_ui(undo_list, undo_list_number, x):
    '''
    The following function :
    > Lists on the screen all the implemented commands
    >>>input : NONE
    >>>output : NONE
    '''
    print("    X - apartment number, Y - apartment number, SERV - service type, A - expenses, SIGN - '<' '=' '>'")
    print("")
    print("    add <X> <SERV> <A>                - add a new apartment with its service type and expense")
    print("    remove <X>                        - remove a certain apartment from the list")
    print("    remove <X> to <Y>                 - remove apartments from x to y")
    print("    remove <SERV>                     - remove all entries that have the given service type")
    print("    replace <X> <SERV> with <A>       - replace the expense of a certain entry with a new one")
    print("    list <SIGN> <A>                   - display all entries with the expense <, = or > than a certain amount")
    print("    list <X>                          - display all entries for a certain apartment")
    print("    list                              - display all entries")
    print("    sum <SERV>                        - display total sum of a certain service type")
    print("    max <X>                           - display the maximum amount per each expense type for a certain time")
    print("    sort apartment                    - display the list of apartments sorted ascending by total amount of expenses")
    print("    sort type                         - display the list of services sorted ascending by total amount of expenses")
    print("    filter <A>                        - keep only the apartments with the expense lower then A")
    print("    filter <SERV>                     - keep only the apartments with the given service type")
    print("    undo                              - restore the previous lists")
    print("    exit                              - exit the program")
    print("")
    pass

#=======================================================================================================================

def _add_apartment_error_message(response_code):
    '''
    The following function :
    > Interprets the given variable and display an error message or calls the undo save function
    >>>input : Response Variable From Add Function
    '''
    try:
        message = {"-1": ">>>Invalid apartment number! :(", "-2": ">>>Invalid service type! :(",
                   "-3": ">>>Invalid expense! :("}
        print(message[response_code])
    except KeyError:
        pass
    pass


def _add_apartment_ui(undo_list, undo_list_number, apartment_list, apartment_number, service_type, expense):
    '''
    The following function :
    > Calls the add apartment function
    > Calls the message interpretation function for add using the returned variable
    >>>input : Apartment List; Apartment Number; Service Type; Expense;
    >>>output : NONE
    '''
    _undo_save(apartment_list,undo_list, undo_list_number)
    response_code = add_apartment(apartment_list, apartment_number, service_type, expense)
    _add_apartment_error_message(response_code)
    if response_code != "1":
        undo_undo(undo_list, undo_list_number)
    pass

#=======================================================================================================================

def _display_ui(apartment):
    '''
    The following function :
    > Prints an entry from the dictionary
    >>>input : Dictionary Entry
    >>>output : NONE 
    '''
    print(">>>apartment number = {0}, service type = {1}, amount = {2}".format(apartment["apartment_number"], apartment["service_type"], apartment["amount"]))


def _display_apartments_list_ui(apartment_list):
    '''
    The following function :
    > Calls the display function for every apartment in the list
    >>>input : Apartment List;
    >>>output : NONE
    '''
    for apartment in apartment_list:
        _display_ui(apartment)
    pass


def _display_apartment_ui(apartment_list, apartment):
    '''
    The following function :
    > Displays every entry for a certain apartment
    >>>input : Apartment List; Given Apartment
    >>>output : NONE
    '''
    list_new = []
    x = display_certain(apartment_list, apartment, list_new)
    if x == 1:
        _display_apartments_list_ui(list_new)
    elif x == -2 : print(">>>Invalid apartment number! :(")
    else : print(">>>There is no entry that matches the apartment number")


def _display_bigger_or_smaller_ui(apartment_list, sign, amount):
    '''
    The following function :
    > Checks if there are any entries in the list
    > If there are call the apartment display function
    >>>input : Apartment List, Other Arguments
    >>>output : NONE
    '''
    list_new = []
    x = display_big_small(apartment_list, sign, amount, list_new)
    if x == 1:
        _display_apartments_list_ui(list_new)
    elif x == -2 : print(">>>Invalid apartment number! :(")
    elif x == -3 : print(">>>Invalid sign ",sign)
    else : print(">>>There is no entry that matches the apartment number")


def _display_options_ui(undo_list, undo_list_number, apartment_list, *arguments):
    '''
    The following function :
    > Checks if there are any entries in the list
    > If there are call the apartment display function
    >>>input : Apartment List, Other Arguments
    >>>output : NONE
    '''
    value = display_apartment_options(apartment_list, *arguments)
    if value == "-1":
        print(">>>There are no registered entries in the list! :(")
    else :
        commands = {"1": _display_apartments_list_ui, "2": _display_apartment_ui, "3": _display_bigger_or_smaller_ui}
        commands[value](apartment_list, *arguments)
    pass

#=======================================================================================================================

def _remove_apartment_ui(undo_list, undo_list_number, apartment_list, *arguments):
    '''
    The following function :
    > Interprets the result of the remove_options function
    >>>input : Apartment List; Arguments;
    >>>output : NONE
    '''
    _undo_save(apartment_list,undo_list, undo_list_number)
    x = remove_options(apartment_list, *arguments)
    if x == -1 :
        print(">>>The given command is incorrect! :(")
        undo_undo(undo_list, undo_list_number)
    elif x == -2:
        print(">>>The given service type does not exist")
        undo_undo(undo_list, undo_list_number)
    elif x == -3:
        print(">>>There are no entries that match the previous command")
        undo_undo(undo_list, undo_list_number)
    pass

#=======================================================================================================================

def _replace_ui(undo_list, undo_list_number, apartment_list, *arguments):
    '''
    The following function :
    > Calls the replace_amount function and displays a message if the entered apartment is not found
    >>>input : Apartment List; Arguments
    >>>output : NONE
    '''
    _undo_save(apartment_list,undo_list, undo_list_number)
    if len(arguments) != 4 or arguments[2] != "with":       #If there are not enough elements or the 3 element is not with, then the command is incorrect
        print(">>>Incorrect command, please reenter.")
        undo_undo(undo_list, undo_list_number)
    else:
        x = replace_amount(apartment_list, *arguments)
        if  x == -1:     #If the given apartment is not found the following message is displayed
            undo_undo(undo_list, undo_list_number)
            print(">>>The required entry does not exist.")
        elif x == -2:
            print(">>>Incorrect syntax for one of the variables!")
    pass

#=======================================================================================================================

def _sum_ui(undo_list, undo_list_number, apartment_list, service_type):
    x = sum_service_type(apartment_list, service_type)
    if x == -1:
        print(">>>The given service type was not found in the list.")
    elif x == -2:
        print(">>>Invalid service type!")
    else :
        print(">>>The total expenses for {0} are {1}".format(service_type, x))
    pass

#=======================================================================================================================

def _max_ui(undo_list, undo_list_number, apartment_list, apartment_number):
    '''
    The following function calls the main max function and
    displays a message depending on what the main max function returns
    '''
    max_apartment = []
    x = max_apartment_expense(apartment_list, apartment_number, max_apartment)
    if x == -1:
        print(">>>Incorrect syntax")
    elif x == -2:
        print(">>>The given apartment was not found")
    else : _display_apartments_list_ui(max_apartment)

#=======================================================================================================================

def _sort_display_ui(sorted_l, type_var):
    '''
    The following function :
    > Displays each entry
    >>>input : Sorted List; Task Type;(Apartment or Service)
    '''
    if type_var == 1:     #If the command is for apartments, then display 'apartment number' otherwise 'service type'
        x = "apartment number"
    else: x = "service type"
    if len(sorted_l) == 0:        #The instruction checks if there is any element in the list between 
        print(">>>No apartment registered")        #If not a message is displayed  
    for entry in sorted_l:      #For each apartment "apt" from the apartment_list, all stored information are printed
        print(">>>{0} = {1} :  expense = {2}".format(x, entry["apart_serv"], entry["amount"]))
    pass


def _sort_ui(undo_list, undo_list_number, apartment_list, task):
    '''
    The following function :
    > Interprets the second part of the command 
    > Calls the right function 
    > It also displays a message in case of an error
    >>>input : Apartment List; Task
    >>>output : NONE
    '''
    sorted_l = []
    x = sort_options(apartment_list, task, sorted_l)
    if x == -1:
        print(">>>There are no elements in the existing list! :(")
    elif x == -2:
        print(">>>Invalid command! :(")
    else : _sort_display_ui(sorted_l, x)

#=======================================================================================================================

def _filter_ui(undo_list, undo_list_number, apartment_list, task):
    '''
    The following function :
    > Calls the filter function
    > Interprets the numerical value returned by the filter function
    >>>input : Apartment List; Task(Service or Expense)
    >>>output : NONE
    '''
    #_undo_ui(apartment_list,undo_list, undo_list_number)
    #_undo_dis(apartment_list,undo_list)
    _undo_save(apartment_list,undo_list, undo_list_number)
    x = filter_options(apartment_list, task)
    if x == -1:
        print(">>>The existing list is empty! :(")
        undo_undo(undo_list, undo_list_number)
    elif x == -2:
        print(">>>There have not been found any entries for the given command!")
        undo_undo(undo_list, undo_list_number)
    pass

#=======================================================================================================================
'''
def _undo_undo(undo_list, undo_list_number):
    x = len(undo_list_number)
    y = len(undo_list)
    z = undo_list_number[x - 1]
    q = z
    undo_list[:] = undo_list[:y-q]
    undo_list_number[:] = undo_list_number[:x-1]
'''


def _undo_save(apartment_list, undo_list, undo_list_number):
    undo_list_number.append(len(apartment_list))
    undo_list.extend(deepcopy(apartment_list))


def _undo_ui(undo_list, undo_list_number, apartment_list):
    '''
    '''
    x = undo(undo_list, undo_list_number, apartment_list)
    if x == -1:
        print(">>>No previous list exists!")
    pass

'''
def _undo_ui(undo_list, undo_list_number, apartment_list):
    if len(undo_list_number) != 0:
        x = len(undo_list_number)
        y = len(undo_list)
        z = undo_list_number[x - 1]
        q = z
        apartment_list.clear()
        while z != 0:
            apartment_list.append(undo_list[y-z])
            z = z - 1
        undo_list[:] = undo_list[:y-q]
        undo_list_number[:] = undo_list_number[:x-1]
    else : print("No previous list exists")
'''
#=======================================================================================================================

def _command_read():
    '''
    The following function :
    > Returns the interpreted the command
    >>>input : User Given Command
    >>>output : Interpreted Command
    '''
    command = input("<<< ")
    position = command.find(" ")    #Returns the position of the first space " " if it exists otherwise returns -1
    if position == -1:      #If True the command is formed from only one word (no spaces)
        return command,""       #Returns the word and nothing else in the place of the other arguments
    cmd = command[:position]        #"cmd" takes the first part of the string "Primary command", up to the position of the space " "
    arguments = command[position:]      #"arguments" takes the last part of the string, from the position of the space " " to the end of the string "Arguments list"
    arguments = arguments.split()       #The last part is divided and the words are put in a list
    return cmd, arguments       #return "Primary command" and "Arguments list"


def _command_based_input():
    '''
    The following function :
    > Calls the input command function
    > Interprets the command
    > Calls each function accordingly
    >>>input : NONE
    >>>output : NONE
    '''
    apartment_list = []
    undo_list = []
    undo_list_number = []
    startup_initialization(apartment_list)
    commands = {"add": _add_apartment_ui,"help":  _help_command_ui, "list": _display_options_ui, "remove":  _remove_apartment_ui, "replace":  _replace_ui, "sum": _sum_ui, "max": _max_ui, "sort": _sort_ui, "filter": _filter_ui, "undo": _undo_ui}
    #The previous command creates a dictionary of functions
    while True:
        cmd, arguments = _command_read()     #"cmd & arguments" receive the transformed command from the "read_command()" function
        if cmd == 'exit':       #If the command is "exit" the function stops
            break
        try:        #"try" repeats an instruction, if there is an Error, until the command is correct
            commands[cmd](undo_list, undo_list_number, apartment_list, *arguments)
        except KeyError as ke:      #If the command does not exist, print the following message and repeat
            print(">>>This command is not implemented : ", ke)
        except Exception:     #If there are too many arguments, print the following message and repeat
            print(">>>Incorrect command! ")
    pass

#=======================================================================================================================

def _add_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input for the add function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    apartment_number = input("<<<apartment number : ")
    service_type = input("<<<service type : ")
    expense = input("<<<expense : ")
    _add_apartment_ui(undo_list, undo_list_number, apartment_list, apartment_number, service_type.strip(), expense)


def _remove_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input  for the remove function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    print(">>>Press the number of the function you wish to use : ")
    print("    [1]Remove an apartment")
    print("    [2]Remove from apart x to apart y")
    print("    [3]Replace a service type")
    x = input(">>>Enter : ")
    if check_number(x) == True:
        if int(x) == 1:
            apartment_number = input("<<<apartment number : ")
            _remove_apartment_ui(undo_list, undo_list_number, apartment_list, apartment_number)
        elif int(x) == 2:
            apartment_number_1 = input("<<<first apartment number : ")
            apartment_number_2 = input("<<<second apartment number : ")
            _remove_apartment_ui(undo_list, undo_list_number, apartment_list, apartment_number_1, "to", apartment_number_2)
        elif int(x) == 3:
            service_type = input("<<<service type : ")
            _remove_apartment_ui(undo_list, undo_list_number, apartment_list, service_type)
        else:print(">>>Command not implemented")
    else: print(">>>Incorrect syntax")
    pass


def _replace_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input  for the replace function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    apartment_number = input("<<<apartment number : ")
    service_type = input("<<<service type : ")
    expense = input("<<<new expense : ")
    _replace_ui(undo_list, undo_list_number, apartment_list, apartment_number, service_type, "with", expense)


def _list_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input  for the list function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    print(">>>Press the number of the function you wish to use : ")
    print("    [1]List all")
    print("    [2]List <, = or > then")
    print("    [3]List all entries for an apartment")
    x = input(">>>Enter : ")
    if check_number(x) == True:
        if int(x) == 1:
            _display_options_ui(undo_list, undo_list_number, apartment_list)
        elif int(x) == 2:
            sign = input("<<<sign : ")
            amount = input("<<<amount : ")
            _display_options_ui(undo_list, undo_list_number, apartment_list, sign, amount)
        elif int(x) == 3:
            apartment_number = input("<<<apartment number : ")
            _display_options_ui(undo_list, undo_list_number, apartment_list, apartment_number)
        else:print(">>>Command not implemented")
    else: print(">>>Incorrect syntax")


def _sum_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input  for the sum function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    service_type = input("<<<service type : ")
    _sum_ui(undo_list, undo_list_number, apartment_list, service_type)


def _max_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input  for the max function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    apartment_number = input("<<<apartment number : ")
    _max_ui(undo_list, undo_list_number, apartment_list, apartment_number)


def _sort_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input  for the sort function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    print(">>>Press the number of the function you wish to use : ")
    print("    [1]Sort apartment ")
    print("    [2]Sort type ")
    x = input(">>>Enter : ")
    if check_number(x) == True:
        if int(x) == 1:
            _sort_ui(undo_list, undo_list_number, apartment_list, "apartment")
        elif int(x) == 2:
            _sort_ui(undo_list, undo_list_number, apartment_list, "type")
        else:print(">>>Command not implemented")
    else: print(">>>Incorrect syntax")


def _filter_meui(undo_list, undo_list_number, apartment_list):
    '''
    The following function :
    > Receives the user input  for the filter function
    >>>input : Undo List; Undo List Number; Apartment List;
    >>>output : NONE
    '''
    print(">>>Press the number of the function you wish to use : ")
    print("    [1]Filter service")
    print("    [2]Filter all for expense <  then amount")
    x = input(">>>Enter : ")
    if check_number(x) == True:
        if int(x) == 1:
            service_type = input("<<<service type : ")
            _filter_ui(undo_list, undo_list_number, apartment_list, service_type)
        elif int(x) == 2:
            amount = input("<<<amount : ")
            _filter_ui(undo_list, undo_list_number, apartment_list, amount)
        else:print(">>>Command not implemented")
    else: print(">>>Incorrect syntax")
    pass

#=======================================================================================================================

def _commands_ui():
    '''
    The following function :
    > Displays the menu based UI
    > Returns the chosen command
    >>>input : NONE
    >>>output : Numerical Value;
    '''
    print("")
    print("===================================================")
    print("Press the number of the function you wish to use : ")
    print("    [1]Add an entry")
    print("    [2]Remove an entry")
    print("    [3]Replace an entry")
    print("    [4]List options")
    print("    [5]Help")
    print("    [6]Total Sum of a service type")
    print("    [7]Maximum of an apartment")
    print("    [8]Sort options")
    print("    [9]Filter the list")
    print("    [10]Undo")
    print("    [0]Exit")
    print("")
    return input(">>>Enter : ")


def _meui_input():
    '''
    The following function :
    > Calls each function according to the user input
    >>>input : NONE
    >>>output : NONE
    '''
    apartment_list = []
    undo_list = []
    undo_list_number = []
    startup_initialization(apartment_list)
    while True:
        x = _commands_ui()
        if check_number(x) == True:
            if int(x) == 0:
                break
            elif int(x) == 1:
                _add_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 2:
                _remove_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 3:
                _replace_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 4:
                _list_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 5:
                _help_command_ui(undo_list, undo_list_number, 1)
            elif int(x) == 6:
                _sum_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 7:
                _max_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 8:
                _sort_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 9:
                _filter_meui(undo_list, undo_list_number, apartment_list)
            elif int(x) == 10:
                _undo_ui(undo_list, undo_list_number, apartment_list)
            else:
                print(">>>The given command is not implemented !")
        else : print(">>>Incorrect syntax")
    pass

#=======================================================================================================================

def app_start():
    '''
    The following function :
    > Calls the commands based input function or the menu based one
    >>>input : NONE
    >>>output : NONE
    '''
    x = input(">>>Press [1] for command based UI or [2] for menu based UI : ")
    if check_number(x) == True:
        if int(x) == 1:
            _command_based_input()
        elif int(x) ==2:
            _meui_input()
        else:print(">>>Command not implemented")
    else: print(">>>Incorrect syntax!")
    pass

