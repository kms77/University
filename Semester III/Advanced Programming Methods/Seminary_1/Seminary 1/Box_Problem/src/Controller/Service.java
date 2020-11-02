package Controller;
import Model.*;
import Exception.*;
import Repository.*;
public class Service {
       private final Repository_Interface repository;
       public Service(Repository_Interface repository_interface){
           repository=repository_interface;
       }

       /*
       Function which calls the repository in order to add a new element in the list
       If it is not a valid element an exception is thrown
       Input: Box new_element- element that could be added into the list
       Output: -
        */
       public void add_box_element(Box new_element) throws Custom_Exception{
           repository.Add_Element(new_element);
       }

       /*
       Function which calls the repository in order to delete an existing element from the list
       If it is not an existing element an exception is thrown
       Input: int id_number- eid of the element that could be deleted from the list
       Output: -
       */
       public void delete_box_element(int id_number) throws Custom_Exception{
           repository.Delete_Element(id_number);
       }

       /*
       Function which calls the repository in order to update an existing element from the list
       If it is not an existing element an exception is thrown
       Input: Box element- element that could update the list
       Output: -
       */
       public void update_box_element(Box element) throws  Custom_Exception{
           repository.Update_Element(element);
       }

       /*
       Function which calls the repository in order to return hte list of elements
       Input: -
       Output: Box - the list of elements
       */
       public Box [] get_all_elements() {
           return repository.Get_All_Elements();
       }

       /*
       Function which returns the filtered list of elements.
       All elements with a weight greater than 200 grams are returned.
       Input: int- fixed_weight the exact value of 200 grams
       Output: Box filter_list the list which contains all elements with an weight greater than 200 grams
        */
       public Box[] filter_elements(int fixed_weight)
       {
       Box[] all_elements=repository.Get_All_Elements();
       int length_of_the_list=repository.Get_Length();
       Box[] filter_list=new Box[length_of_the_list];
       int size_of_the_list=0;
       for(int i=0;i<length_of_the_list;i++)
           if(all_elements[i].Get_Weight()>fixed_weight)
               filter_list[size_of_the_list]=all_elements[i];
       return filter_list;
       }
}
