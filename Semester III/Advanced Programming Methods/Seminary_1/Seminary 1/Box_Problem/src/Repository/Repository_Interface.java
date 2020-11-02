package Repository;
import Model.Box;
import Exception.*;
import java.lang.Exception;

/*
Here is the interface of the repository
 */
public interface Repository_Interface {
    public Box[] Get_All_Elements();
    public void Add_Element(Box new_element) throws Custom_Exception;
    public void Delete_Element(int id_number) throws  Custom_Exception;
    public void Update_Element(Box element) throws Custom_Exception;
    public int Get_Length();
}
