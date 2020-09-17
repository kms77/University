#include <cstdlib>
#include "Set.h"
#include "SetIterator.h"

//The Best Case= Worst Case= Average case= theta(1);
//Overall complexity: theta(1)
Set::Set() {

    //TODO - Implementation
    array = nullptr;
    length = 0;
    maxSize = 0;
}
//The Best Case= theta(1) ,Worst Case= theta(n), Average case= theta(n);
//Overall complexity: O(n);
bool Set::add(TElem elem) {

    //TODO - Implementation
    if (maxSize < 1) 
    {
        maxSize = 2;
        array = new TElem[maxSize];
        array[length++] = elem;
        return true;
    }

    if (length + 1 > maxSize) {
        maxSize =maxSize *2;
        auto* t_Array = new TElem[maxSize];
        int i = 0;
        for ( i = 0; i < length; i++) {
            if (elem == array[i]) {
                delete[] t_Array;
                maxSize= maxSize/2;
                return false;
            }
            t_Array[i] = array[i];
        }
        t_Array[length++] = elem;
        delete[] array;
        array = t_Array;
        return true;
    }

    if (search(elem)) {
        return false;
    }
    array[length++] = elem;
    return true;
}

//The Best Case= theta(1) ,Worst Case= theta(n), Average case= theta(n);
//Overall complexity:O(n)
bool Set::remove(TElem elem) {

    //TODO - Implementation
    if (!search(elem)) {
        return false;
    }
    int positioToDelete = 0;
    for (int i = 0; i < length; i++)
    {
        if (array[i] == elem)
            positioToDelete = i;
    }
    for (int i = positioToDelete; i < length - 1; i++)
        array[i] = array[i + 1];
    length--;
    return true;
}
//The Best Case= theta(1) ,Worst Case= theta(n), Average case= theta(n);
//Overall complexity:O(n)
bool Set::search(TElem elem) const {

    //TODO - Implementation
    for (int i = 0; i < length; i++) {
        if (array[i] == elem) {
            return true;
        }
    }
    return false;
}
//The Best Case= Worst Case= Average case= theta(1);
//Overall complexity:theta(1)
int Set::size() const {
    //TODO - Implementation
    return length;
}
//The Best Case= Worst Case= Average case= theta(1);
//Overall complexity: theta(1)
bool Set::isEmpty() const {
    //TODO - Implementation
    return length < 1;
}
//The Best Case= Worst Case= Average case= theta(1);
//Overall complexity: theta(1)
Set::~Set() {
    //TODO - Implementation
    free(array);
}


SetIterator Set::iterator()  {
    return SetIterator(*this);
}
