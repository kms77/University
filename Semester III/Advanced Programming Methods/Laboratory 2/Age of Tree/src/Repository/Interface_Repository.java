package Repository;
import Model.Tree;
import Exception.*;


public interface Interface_Repository
{
    public Tree[] get_elements();
    public void add_element(Tree new_element) throws New_Exception;
    public int get_size();
    public void delete_element(Tree element) throws New_Exception;
}
