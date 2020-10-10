package Repository;
import Model.Tree;
import Exception.*;
public class Repository implements Interface_Repository
{
    private  int capacity=10, size=0;
    private Tree[] elements= new Tree[capacity];
    public Repository(){}
    public Tree[] get_elements()
    {
        return elements;
    }
    public int get_size()
    {
        return size;
    }
    public void add_element(Tree new_element) throws New_Exception{
        if(size==capacity)
        {
            throw new New_Exception("Can not add more elements!\n");
        }
        else if(new_element.get_age_of_tree()<=0)
        {
            throw new New_Exception("Impossible age!\n");
        }
        else
        {
            elements[size] =new_element;
            size++;
        }
    }
    public void delete_element(Tree element) throws New_Exception
    {
        boolean element_found=false;
        for(int i=0;i<this.size;i++)
        {
            if(element.getClass()==elements[i].getClass() && element.get_age_of_tree()==elements[i].get_age_of_tree())
            {
                elements[i] = elements[size - 1];
                elements[size - 1] = null;
                size--;
                element_found = true;
                break;
            }
        }
        if(!element_found)
        {
            throw new New_Exception("The tree does not exist!\n");
        }
    }
}
