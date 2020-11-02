package Repository;
import Model.*;
import Exception.Custom_Exception;
public class Repository implements Repository_Interface{
    Box [] elements;
    int size;
    /*
    Create a repository of current size zero and maximum capacity max_capacity
    Input: int max_capacity- the maximum capacity of our repository
    Output: -
     */
    public Repository(int max_capacity)
    {
        elements= new Box[max_capacity];
        size=0;
    }

    /*
    Function which returns the list of elements
    Input:-
    Output: Box- the list of elements
     */
    @Override
    public Box[] Get_All_Elements() {
        return elements;
    }

    /*
    Function which adds an element into the list
    A custom exception is thrown if the element is not valid
    Input: Box new_element - the new element that will be added into the list
    Output: -
     */
    @Override
    public void Add_Element(Box new_element) throws Custom_Exception
    {
        boolean id_found=false;
        for(int i=0;i< size;i++)
            if(elements[i].Get_Id()==new_element.Get_Id())
            {
                id_found=true;
                break;
            }
        if(id_found)
        {
            throw new Custom_Exception("Existing id!\n");
        }
        else if(size== elements.length)
        {
            throw new Custom_Exception("Can not add more elements!\n");
        }
        else if(new_element.Get_Density()<=0)
        {
            throw new Custom_Exception("Impossible density value!\n");
        }
        else if(new_element.Get_Volume()<=0)
        {
            throw new Custom_Exception("Impossible volume value!\n");
        }
        else
        {
            elements[size++]=new_element;
        }
    }

    /*
    Function which delete an element from the list
    A custom exception is thrown if the element is not valid
    Input: int id_number - the id of the element that will be deleted
    Output: -
     */
    @Override
    public void Delete_Element(int id_number) throws Custom_Exception
    {
        boolean element_found=false;
        for(int i=0;i<this.size;i++)
        {
            if(elements[i].Get_Id()==id_number)
            {
                elements[i]=elements[size-1];
                elements[size-1]=null;
                size--;
                element_found=true;
                break;

            }
        }
        if(!element_found)
        {
            throw new Custom_Exception("Not existing id!\n");
        }
    }

    /*
    Function which update an element from the list
    A custom exception is thrown if the element is not valid
    Input: Box element - the element that will update the list
    Output: -
     */
    @Override
    public void Update_Element(Box element) throws  Custom_Exception{
        if(element.Get_Density()<=0)
        {
            throw new Custom_Exception("Impossible density value!\n");
        }
        else if(element.Get_Volume()<=0)
        {
            throw new Custom_Exception("Impossible volume value!\n");
        }
        else {
            boolean id_found = false;
            for (int i = 0; i < this.size; i++)
                if (elements[i].Get_Id() == element.Get_Id()) {
                    elements[i] = element;
                    id_found = true;
                    break;
                }
            if (!id_found) {
                throw new Custom_Exception("Not existing id!\n");
            }
        }
    }


    /*
    Function which returns the length of the list of elements
    Input:-
    Output: int- length of the list if the elements
     */
    @Override
    public int Get_Length()
    {
        return this.size;
    }
}
