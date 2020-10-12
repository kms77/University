#  Write a recursive program(Python or C + + programming language) for next requirements:

# 7. a. Test the equality of two lists
'''
Function which tests the equality of two lists
Input:   First_List: first list of elements
         Second_List: second list of elements
Output:  True: lists are equal
         False: lists are not equal
'''


def Equality_of_two_Lists(First_List, Second_List):
    if First_List == [] and Second_List == []:
        return True
    elif First_List == [] or Second_List == []:
        return False
    elif First_List[-1] != Second_List[-1]:
        return False
    else:
        First_List.pop()
        Second_List.pop()
        return Equality_of_two_Lists(First_List, Second_List)


# b. Determine the intersection of two sets represented as lists

'''
Function which determine the intersection of two sets represented as lists
Input:   First_Set: first set of elements
         Second_Set: second set of elements
         second_set_element: current index of element from the second set
         end_of_the_second_set: length of the second set
Output:  a list which represents the intersection of the two sets (First_Set and Second_Set) represented as lists
'''


def Intersection_of_two_Sets(First_Set, Second_Set, second_set_element, end_of_second_set):
    if First_Set == []:
        return []
    else:
        if First_Set[0] == Second_Set[second_set_element]:
            value = First_Set.pop(0)
            return [value] + Intersection_of_two_Sets(First_Set, Second_Set, 0, end_of_second_set)
        else:
            if end_of_second_set - 1 == second_set_element:
                First_Set.pop(0)
                return Intersection_of_two_Sets(First_Set, Second_Set, 0, end_of_second_set)
            else:
                second_set_element += 1
                return Intersection_of_two_Sets(First_Set, Second_Set, second_set_element, end_of_second_set)


if __name__ == "__main__":
    print("Test equlity of the two lists, list one [1,2,5,6] and list two [1,2,5,6]. Result :" + str(
        Equality_of_two_Lists([1, 2, 5, 6], [1, 2, 5, 6])))
    print("Intersection of the two sets, first set {1,2,7,8} and second set {1,3,5,8,9}: " + str(
        Intersection_of_two_Sets([1, 2, 7, 8], [1, 3, 5, 8, 9], 0, 5)))
