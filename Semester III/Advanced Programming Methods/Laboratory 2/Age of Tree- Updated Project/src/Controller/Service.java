package Controller;
import Repository.*;
import Model.*;
import Exception.*;
public class Service {
     private final Interface_Repository repository;
     public Service(Interface_Repository Repository)
     {
         repository=Repository;
     }
     public void add_tree(Tree new_tree) throws New_Exception{
         repository.add_element(new_tree);
     }
     public Tree[] search_tree(int age_of_tree)
     {
         int dimension=0;
         Tree[] elements =new Tree[repository.get_size()];
         for(int i=0;i<repository.get_size();i++)
         {
             if(repository.get_elements()[i].get_age_of_tree()>age_of_tree) {
                 elements[dimension++] = repository.get_elements()[i];
             }
         }
         return elements;
     }
     public Tree[] get_all_trees()
     {
         return repository.get_elements();
     }
     public void delete_tree(Tree tree) throws New_Exception {
         repository.delete_element(tree);
     }
}
