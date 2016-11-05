'''
Created on Oct 27, 2016

@author: Vlad
'''
#from copy import deepcopy

def startup_initialization(apartment_list):
    '''
    The following function :
    > initializes the dictionary list with apartments for easier startup
    >>>input : Empty Apartment List
    >>>output : Apartment List Initialized With 10 Entries
    '''
    apartment_list.append({"apartment_number":1,"service_type":'gas',"amount":100})
    apartment_list.append({"apartment_number":2,"service_type":'water',"amount":200})
    apartment_list.append({"apartment_number":3,"service_type":'gas',"amount":400})
    apartment_list.append({"apartment_number":4,"service_type":'gas',"amount":500})
    apartment_list.append({"apartment_number":5,"service_type":'heat',"amount":600})
    apartment_list.append({"apartment_number":5,"service_type":'water',"amount":250})
    apartment_list.append({"apartment_number":2,"service_type":'heat',"amount":250})
    apartment_list.append({"apartment_number":6,"service_type":'gas',"amount":390})
    apartment_list.append({"apartment_number":7,"service_type":'water',"amount":50})
    apartment_list.append({"apartment_number":8,"service_type":'gas',"amount":70})
    pass

#=======================================================================================================================

def check_number(unknown):
    '''
    The following function :
    > Checks if the given string is a number or not
    >>>input : A Given String
    >>>output : False or True; depending if the string can be converted to an integer or not
    '''
    try:
        int(unknown)
        return True     #If the value can be converted into an integer then return True
    except ValueError:
        return False    #If there is an error than the string can not be converted, return False
    pass


def _check_service_type(unknown):
    '''
    The following function :
    > Checks if the given service type is a valid one
    >>>input : A Given String
    >>>output : 
    '''
    service_types = ["gas","heat","electricity","water"]        #Available service types 
    for service in service_types:
        if unknown == service:      #If the given service type matches one from the list then return True
            return True
    return False

#=======================================================================================================================

def _add_apartment_comparison(apartment_list, apartment_number, service_type, amount):
    '''
    The following function :
    > Finds if the new entry is already in the list
    > If it is return True
    >>>input : Apartment List; Apartment Number; Service Type;
    >>>output : True or False; Depending if the entry already exists or not
    '''
    for apart in apartment_list:
        if int(apartment_number) == apart["apartment_number"] and service_type == apart["service_type"]:
            apart["amount"] = apart["amount"] + int(amount)
            return True
    return False


def add_apartment(apartment_list, apartment_number, service_type, amount):
    '''                                                                                       
    The following function :
    > Checks if the apartment entry is already existing
    > If it is just add the expense to the existing one
    > Otherwise add a new entry to the list
    >>>input : Apartment List; Apartment Number; Service Type; Expense;
    >>>output : Response Message; -1 to -3 for errors; 1 if everything is fine  
    '''
    if check_number(apartment_number) == False: return "-1"       #If the apartment number is a string return error message
    elif _check_service_type(service_type) == False: return "-2"         #If the amount is a string return error message
    elif check_number(amount) == False: return "-3"     #If the service type is not recognized return error message
    else:
        apartment = _add_apartment_comparison(apartment_list, apartment_number, service_type, amount)
        if apartment == False :
            apartment = {"apartment_number":int(apartment_number),"service_type":service_type,"amount":int(amount)}       #A dictionary is created with the previous fields
            apartment_list.append(apartment)        #The new entry(dictionary) is added to the list of dictionaries
    #undo(apartment_list, undo_list)
    return "1"

#=======================================================================================================================

def display_certain(apartment_list, apartment, list_new):
    '''
    The following function :
    > Copies all the entries for an apartment & puts them in a new list
    >>>input : Apartment List; Apartment Number; New Empty List;
    >>>output : New List; Or an Numeric Value  
    '''
    ok = 0
    if check_number(apartment) == False:
        return -2
    for apt in apartment_list:
        if apt["apartment_number"] == int(apartment):
            ok = 1
            list_new.append(apt)
    if ok == 1:
        return 1
    return -1


def _display_equal(apartment_list, amount, list_new):
    '''
    The following function :
    > Copies all the entries that have the expenses equal to a given amount & puts them in a new list
    >>>input : Apartment List; Apartment Number; New Empty List;
    >>>output : New List; Or an Numeric Value;
    '''
    ok = 0
    if check_number(amount) == False:
        return -2
    for apt in apartment_list:
        if apt["amount"] == int(amount):
            ok = 1
            list_new.append(apt)
    if ok == 1:
        return 1
    return -1


def _display_bigger(apartment_list, amount, list_new):
    '''
    The following function :
    > Copies all the entries that have the expenses bigger then given amount & puts them in a new list
    >>>input : Apartment List; Apartment Number; New Empty List;
    >>>output : New List; Or an Numeric Value;
    '''
    ok = 0
    if check_number(amount) == False:
        return -2
    for apt in apartment_list:
        if apt["amount"] > int(amount):
            ok = 1
            list_new.append(apt)
    if ok == 1:
        return 1
    return -1


def _display_smaller(apartment_list, amount, list_new):
    '''
    The following function :
    > Copies all the entries that have the expenses smaller then a given amount & puts them in a new list
    >>>input : Apartment List; Apartment Number; New Empty List;
    >>>output : New List; Or an Numeric Value;
    '''
    ok = 0
    if check_number(amount) == False:
        return -2
    for apt in apartment_list:
        if apt["amount"] < int(amount):
            ok = 1
            list_new.append(apt)
    if ok == 1:
        return 1
    return -1


def display_big_small(apartment_list, sign, amount, list_new):
    '''
    The following function : 
    > Interprets the given sign and calls the accordingly function
    >>>input : Apartment List; Sign; Amount; New Empty List;
    >>>output : An Numeric Value;
    '''
    if sign == "<":
        x = _display_smaller(apartment_list, amount, list_new)
    elif sign == ">":
        x = _display_bigger(apartment_list, amount, list_new)
    elif sign == "=":
        x = _display_equal(apartment_list, amount, list_new)
    else: x = -3
    return x


def display_apartment_options(apartment_list, *arguments):
    '''
    The following command :
    > Interprets the list command
    >>>input : Apartment List; and/or Other Arguments
    >>>output : Numeric Value; representative for the command
    '''
    if len(apartment_list) == 0:
        return "-1"
    if len(arguments) == 0:     #If there are no other arguments, then the function will list all apartments
        return "1"
    elif len(arguments) == 1:       #If there is just one other argument then the function will list all entries for a certain apartment
        return "2"
    return "3"

#=======================================================================================================================

def _remove_apartments_between(apartment_list,lower_bound,upper_bound):
    '''
    The following function runs through the list of apartments and reselects
    just the ones that are outside the given interval
    '''
    apartment_list[:] = [apt for apt in apartment_list if apt["apartment_number"] > int(upper_bound) or apt["apartment_number"] < int(lower_bound)]


def _remove_service_type(apartment_list,apartment_service_type):
    '''
    The following function runs through the list of services and reselects
    just the ones that are not equal to the one inserted by the user
    '''
    apartment_list[:] = [serv for serv in apartment_list if serv["service_type"] != apartment_service_type]


def _remove_apartment(apartment_list,apartment_number):
    '''
    The following function runs through the list of apartments and reselects
    just the ones that are not equal to the one inserted by the user
    '''
    apartment_list[:] = [apt for apt in apartment_list if apt["apartment_number"] != int(apartment_number)]


def remove_options(apartment_list,*arguments):
    '''
    The following function :
    > Finds out which remove function needs to be called 
    >>>input : Apartment List; Arguments;
    >>>output : Numeric Value; corresponding to an message
    '''
    original_len = len(apartment_list)
    if len(arguments) != 1:         #If there are multiple elements in "arguments" then the remove function is "remove x to y"
        if arguments[1] == 'to' and check_number(arguments[0]) == True and check_number(arguments[2]) == True:
            _remove_apartments_between(apartment_list,arguments[0],arguments[2])
            if original_len == len(apartment_list):
                return -3
            return 1
        return -1
    elif check_number(arguments[0]) == True:        #If the string can be converted to integer then remove apartment
        _remove_apartment(apartment_list, int(arguments[0]))
        if original_len == len(apartment_list):
                return -3
        return 1
    else:
        if check_number(arguments[0]) == False and _check_service_type(arguments[0]) == True:
            _remove_service_type(apartment_list, arguments[0])     #If the string can not be converted to integer then remove service type
            if original_len == len(apartment_list):
                return -3
            return 1
        else: 
            return -2
    return -1

#=======================================================================================================================

def replace_amount(apartment_list, apartment_number, service_type, noth, new_amount):
    '''
    The following function replaces the expense of a certain                                     <<<Replace apartment expense>>>
    apartment for a service with a new, user introduced one
    '''
    if check_number(apartment_number) == False:
        return -2
    if _check_service_type(service_type) == False:
        return -2
    if check_number(new_amount) == False:
        return -2
    for apartment in apartment_list:        #Run through all dictionaries in the list
        if apartment["apartment_number"] == int(apartment_number) and apartment["service_type"] == service_type:   #If the apt. number and service type coincide:
            apartment["amount"]=int(new_amount)     #Replace old expense with a the new one
            return 1
    return -1        #If the apartment was not found The function returns False

#=======================================================================================================================

def sum_service_type(apartment_list, service_type):
    '''
    The following function :
    > Sums the total expenses for the given service type
    >>>input : Apartment List; Service Type;
    >>>output : A Numerical Value; Representing the sum or an error message
    '''
    if _check_service_type(service_type) == False:
        return -2
    sum_expense = 0
    ok = 0
    for apt in apartment_list:
        if apt["service_type"] == service_type:      #If the two service types coincide, add the expense to the 'sum'
            sum_expense += apt["amount"]
            ok = 1
    if ok == 1:     #If the given service type exist return 'sum'
        return sum_expense
    return -1

#=======================================================================================================================

def max_apartment_expense(apartment_list, apartment_number, max_apartment):
    '''
    The following function :
    > Copies all the entries with the given apartment number
    > Sorts the new list descending by the expenses
    >>>input : Apartment List; Apartment Number; Empty Max Apartment List;
    >>>output : A Numerical Value; Representing a message
    '''
    ok = 0
    if check_number(apartment_number) == False:
        return -1
    else:
        for apt in apartment_list:      #For every apartment if the apartment number matches with the given one
            if int(apartment_number) == apt["apartment_number"]:
                apartment = apt.copy()      #Copy the dictionary in a new one
                max_apartment.append(apartment)     #Add the copied dictionary to the new dictionary list
                ok = 1
        if ok == 1:
            max_apartment[:] = sorted(max_apartment, key = lambda k: k['amount'], reverse = True)       #Command to sort a list of dictionaries
            return 1
    return -2

#=======================================================================================================================

def _sort_list(apartment_or_serv, amount, sorted_l):
    '''
    The following function :
    > Sorts the list with every new entry 
    >>>input : Service Or Apartment; Expense; Sorted List
    >>>output : NONE
    '''
    for pos in sorted_l:        #We check if the given value already exists in the list, if it does we sum the old expense with the new one
        if pos["apart_serv"] == apartment_or_serv:
            pos["amount"] += amount
            return True
    sorted_l.append({"apart_serv": apartment_or_serv,"amount": amount})     #Otherwise we add a new value to the list


def _sort_apartment(apartment_list, sorted_l):
    '''
    The following function :
    > Calls the function that adds new values into the new list
    > Orders the new list
    >>>input : Apartment List; New List
    >>>output : NONE
    '''
    for apt in apartment_list:      #In this function we need just the number of the apartment and it's expense, so we use them from every entry
        apartment = apt["apartment_number"]
        amount = apt["amount"]
        _sort_list(apartment, amount, sorted_l)
    sorted_l[:] = sorted(sorted_l, key = lambda k: k['amount'])            #Command to sort a list of dictionaries
    

def _sort_service_type(apartment_list, sorted_l):
    '''
    The following function :
    > Calls the function that adds new values into the new list
    > Orders the new list
    >>>input : Apartment List; New List
    >>>output : NONE
    '''
    for apt in apartment_list:      #In this function we need just the service types and their expense, so we use them from every entry
        apartment = apt["service_type"]
        amount = apt["amount"]
        _sort_list(apartment, amount, sorted_l)
    sorted_l[:] = sorted(sorted_l, key = lambda k: k['amount'])            #Command to sort a list of dictionaries


def sort_options(apartment_list, task, sorted_l):
    '''
    The following function :
    > Interprets the second part of the command
    > Calls each function accordingly
    >>>input : Apartment List; Task; Empty List
    >>>output : A Numerical Value; Representing a certain message
    '''
    if len(apartment_list) == 0:
        return -1
    if task == "apartment":
        _sort_apartment(apartment_list, sorted_l)
        return 1
    elif task == "type":
        _sort_service_type(apartment_list, sorted_l)
        return 2
    else : return -2

#=======================================================================================================================

def _filter_check(apartment_list, task):
    '''
    The following function :
    > It checks if there are any entries available in the existing list
    >>>input : Apartment List; Tasks(Service or Expense);
    >>>output : A Numerical Value;
    '''
    if _check_service_type(task):
        for serv in apartment_list:
            if serv["service_type"] == task:
                return 1
    elif check_number(task):
        for apt in apartment_list:
            if apt["amount"] < int(task):
                return 2
    return -1


def _filter(apartment_list, task, x):
    '''
    The following function :
    > Keep all the entries that match the command
    >>>input : Apartment List; Tasks(Service or Expense), A Numerical Value (Representing the Tasks);
    >>>output : NONE
    '''
    if x == 1:
        apartment_list[:] = [apt for apt in apartment_list if apt["service_type"] == task]
    else :
        apartment_list[:] = [apt for apt in apartment_list if apt["amount"] < int(task)]
    pass


def filter_options(apartment_list, task):
    '''
    The following function :
    > Keep all the entries that match the command
    >>>input : Apartment List; Tasks(Service or Expense);
    >>>output : A Numerical Value
    '''
    x = _filter_check(apartment_list, task)
    if len(apartment_list) == 0:
        return -1
    elif x == -1:
        return -2
    else:
        _filter(apartment_list, task, x)
    return 1

#=======================================================================================================================

def undo_undo(undo_list, undo_list_number):
    x = len(undo_list_number)
    y = len(undo_list)
    z = undo_list_number[x - 1]
    q = z
    undo_list[:] = undo_list[:y-q]
    undo_list_number[:] = undo_list_number[:x-1]


def undo(undo_list, undo_list_number, apartment_list):
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
        return 1
    else : 
        return -1
    pass

