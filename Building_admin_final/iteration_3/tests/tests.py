'''
Created on Oct 27, 2016

@author: Vlad
'''

from iteration_3.backbone.functions import undo, undo_undo,add_apartment, display_apartment_options, display_big_small, remove_options, replace_amount, sum_service_type, max_apartment_expense, sort_options, filter_options, check_number
#from distutils.command.check import check


def _test_init_list(apartment_list_t):
    '''
    The following function initializes a list
    for the test function
    '''
    apartment_list_t.append({"apartment_number":1,"service_type":'gas',"amount":100})
    apartment_list_t.append({"apartment_number":2,"service_type":'water',"amount":120})
    apartment_list_t.append({"apartment_number":3,"service_type":'heat',"amount":75})
    apartment_list_t.append({"apartment_number":4,"service_type":'heat',"amount":500})
    apartment_list_t.append({"apartment_number":5,"service_type":'gas',"amount":432})
    apartment_list_t.append({"apartment_number":6,"service_type":'heat',"amount":330})


def _test_add():
    '''
    The following function :
    > Tests the add functions
    '''
    apart_l = []
    _test_init_list(apart_l)
    assert add_apartment(apart_l, "dog", "gas", 123) == "-1"
    assert add_apartment(apart_l, 123, "cat", 123) == "-2"
    assert add_apartment(apart_l, 123, "gas", "wine") == "-3"
    assert add_apartment(apart_l, 12, "gas", 123) == "1"
    assert len(apart_l) == 7
    

def _test_remove():
    '''
    The following function :
    > Tests the remove functions
    '''
    apart_l = []
    _test_init_list(apart_l)
    assert remove_options(apart_l, "mouse", "to", 123) == -1
    assert remove_options(apart_l, 2, "with", 123) == -1
    assert remove_options(apart_l, 1, "to", "key") == -1
    assert remove_options(apart_l, "mouse", "to", 123) == -1
    assert remove_options(apart_l, "dog") == -2
    assert remove_options(apart_l, 123, "to", 123) == -3
    assert remove_options(apart_l, 1) == 1
    assert len(apart_l) == 5


def _test_replace():
    '''
    The following function :
    > Tests the replace functions
    '''
    apart_l = []
    _test_init_list(apart_l)
    assert replace_amount(apart_l, "qwe", "water", "with", 12) == -2
    assert replace_amount(apart_l, 12, "car", "with", 12) == -2
    assert replace_amount(apart_l, "123", "water", "with", "hit") == -2
    assert replace_amount(apart_l, 1, "gas", "with", 123) == 1


def _test_sum():
    '''
    The following function :
    > Tests the sum functions
    '''
    apart_l = []
    _test_init_list(apart_l)
    assert sum_service_type(apart_l, "cow") == -2
    assert sum_service_type(apart_l, "electricity") == -1
    assert sum_service_type(apart_l, "gas") == 532


def _test_max():
    '''
    The following function :
    > Tests the max functions
    '''
    apart_l = []
    list_new = []
    _test_init_list(apart_l)
    assert max_apartment_expense(apart_l, "horse", list_new) == -1
    assert max_apartment_expense(apart_l, "123", list_new) == -2
    assert max_apartment_expense(apart_l, "1", list_new) == 1
    assert len(list_new) == 1


def _test_sort():
    '''
    The following function :
    > Tests the sort functions
    '''
    apart_l = []
    list_new = []
    _test_init_list(apart_l)
    assert sort_options(list_new,"apartment",list_new) == -1
    assert sort_options(apart_l,"plane",list_new) == -2
    assert sort_options(apart_l,"apartment",list_new) == 1
    assert sort_options(apart_l,"type",list_new) == 2


def _test_filter():
    '''
    The following function :
    > Tests the filter functions
    '''
    apart_l = []
    list_new = []
    _test_init_list(apart_l)
    assert filter_options(list_new, "electricity") == -1
    assert filter_options(apart_l, "electricity") == -2
    assert filter_options(apart_l, "gas") == 1
    

def _test_check():
    '''
    The following function :
    > Tests the check number function
    '''
    assert check_number("123") == True
    assert check_number("asdfg") == False
    assert check_number(123) == True


def _test_display():
    '''
    The following function :
    > Tests the display functions
    '''
    apart_l = []
    list_new = []
    assert display_apartment_options(apart_l) == "-1"
    _test_init_list(apart_l)
    assert display_apartment_options(apart_l) == "1"
    assert display_apartment_options(apart_l, 12) == "2"
    assert display_apartment_options(apart_l, 12, 123) == "3"
    assert display_big_small(apart_l, "<", 500, list_new) == 1
    assert display_big_small(apart_l, "asd", 500, list_new) == -3
    assert display_big_small(apart_l, "=", "qwerty", list_new) == -2
    assert display_big_small(apart_l, "=", 1, list_new) == -1


def _test_undo():
    '''
    The following function :
    > Tests the undo functions
    '''
    list_new = [1]
    empty = []
    apart_l = []
    _test_init_list(apart_l)
    undo_undo(apart_l, list_new)
    assert len(apart_l) == 5
    assert undo(list_new, empty, apart_l) == -1


def test():
    '''
    This function calls all the test functions
    '''
    _test_add()
    _test_remove()
    _test_replace()
    _test_sum()
    _test_max()
    _test_sort()
    _test_check()
    _test_display()
    _test_undo()
    pass
    