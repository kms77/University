#  Write a recursive program(Python or C + + programming language) for next requirements:

# 12. a. Test the inclusion of two lists

'''
Function which test the inclusion of two lists
Input:   First_List: first list of elements
         Second_List: second list of elements
         Aux-List: the auxiliary list. We compare it with the other two lists
         Copy_of_First_List: a copy of the first list. We need it because the first list will be destroy
         second_list_element: current index of element from the second list
         end_of_the_second_list: the length of the second list
Output:  True: one list is included in another list
         False: inclusion of the two lists does not exist
'''


def Test_Inclusion(First_List, Second_List, Aux_List, Copy_of_First_List, second_list_element, end_of_the_second_list):
    if First_List == [] or Second_List == []:
        if ((First_List == [] and Aux_List == []) or Second_List == 0):
            return False
        elif Copy_of_First_List == Aux_List or Second_List == Aux_List:
            return True
        else:
            return False
    else:
        if First_List[0] == Second_List[second_list_element]:
            value = First_List.pop(0)
            Aux_List = Aux_List + [value]
            if First_List == []:
                if Copy_of_First_List == Aux_List or Second_List == Aux_List:
                    return True
                else:
                    return False
            return Test_Inclusion(First_List, Second_List, Aux_List, Copy_of_First_List, 0, end_of_the_second_list)
        else:
            if end_of_the_second_list - 1 == second_list_element:
                First_List.pop(0)
                if First_List == []:
                    if Copy_of_First_List == Aux_List or Second_List == Aux_List:
                        return True
                    else:
                        return False
                return Test_Inclusion(First_List, Second_List, Aux_List, Copy_of_First_List, second_list_element,
                                      end_of_the_second_list)
            else:
                second_list_element += 1
                return Test_Inclusion(First_List, Second_List, Aux_List, Copy_of_First_List, second_list_element,
                                      end_of_the_second_list)


# b. Insert in a list, after value e, a new value e1.

'''
Function which insert in a list, after value e, a new value e1
Input:   List: first list of elements
         e: value after that the new element will be inserted 
         e1: the new value that will be inserted after value e
Output:  the list with the new e1 element inserted into
         or the same list from the start of the program if value e does not exist
'''


def Insert_in_a_List(List, e, e1):
    if List == []:
        return []
    value = List.pop()
    if value == e:
        return Insert_in_a_List(List, e, e1) + [e, e1]
    else:
        return Insert_in_a_List(List, e, e1) + [value]


if __name__ == "__main__":
    print("Result of the test inclusion of the two lists [2,7,9] and [1,2,3,7,9]: " + str(
        Test_Inclusion([2, 7, 9], [1, 2, 3, 7, 9], [], [2, 7, 9], 0, 5)))
    print("Insert in a the list [2, 3, 5, 6], after value 3, the value 4: " + str(Insert_in_a_List([2, 3, 5, 6], 3, 4)))
