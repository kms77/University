package View;
import Model.*;
import Repository.Repository;
import Controller.Service;
import java.util.Scanner;
public class User_Interface
{
    /*
    Main function which contains the menu and the commands
     */
    public static void main(String[] args)
    {
        int capacity = 10;
        Repository repository = new Repository(capacity);
        Service service = new Service(repository);
        Scanner scanner = new Scanner(System.in);
        String Menu = """
                 ---------------------------------MENU------------------------------------
                |                                                                         |
                |     1)Add a new element into the box;                                   |
                |     2)Delete an element from the box;                                   |
                |     3)Update an element from the box;                                   |
                |     4)Display all elements;                                             |
                |     5)Display all elements with an weight greater than 200 grams;       |
                |     0)Exit;                                                             |
                |                                                                         |
                 -------------------------------------------------------------------------
                Choose from 0 to 5:""";
        while (true)
            try
            {
                System.out.println(Menu);
                int command = scanner.nextInt();
                if (command == 1)
                {
                    System.out.print("Id number: ");
                    int id_number = scanner.nextInt();
                    System.out.print("Type of element: ");
                    Scanner scanner_string = new Scanner(System.in);
                    String type = scanner_string.nextLine();
                    type = (type.split(" "))[0];
                    if (type == null)
                    {
                        throw new Exception("Invalid value!\n");
                    }
                    System.out.print("Density: ");
                    int density = scanner.nextInt();
                    System.out.print("Volume: ");
                    int volume = scanner.nextInt();
                    if(type.equalsIgnoreCase("apple"))
                    {
                        service.add_box_element(new Apple(id_number,"apple",density,volume));
                    }
                    else if (type.equalsIgnoreCase("book"))
                    {
                        service.add_box_element(new Book(id_number,"book",density,volume));
                    }
                    else if(type.equalsIgnoreCase("cake"))
                    {
                        service.add_box_element(new Cake(id_number,"cake",density,volume));
                    }
                    else
                    {
                            throw new Exception("Invalid type for an element!\n");
                    }
                }
                else if (command==2)
                {
                    System.out.println("Id number: ");
                    int id_number=scanner.nextInt();
                    service.delete_box_element(id_number);
                }
                else if(command==3)
                {
                    System.out.print("Id number: ");
                    int id_number = scanner.nextInt();
                    System.out.print("Type of element: ");
                    Scanner scanner_string = new Scanner(System.in);
                    String new_type = scanner_string.nextLine();
                    new_type = (new_type.split(" "))[0];
                    if (new_type == null)
                    {
                        throw new Exception("Invalid value!\n");
                    }
                    System.out.print("Density: ");
                    int new_density = scanner.nextInt();
                    System.out.print("Volume: ");
                    int new_volume = scanner.nextInt();
                    if(new_type.equalsIgnoreCase("apple"))
                    {
                        service.update_box_element(new Apple(id_number,"apple",new_density,new_volume));
                    }
                    else if (new_type.equalsIgnoreCase("book"))
                    {
                        service.update_box_element(new Book(id_number,"book",new_density,new_volume));
                    }
                    else if(new_type.equalsIgnoreCase("cake"))
                    {
                        service.update_box_element(new Cake(id_number,"cake",new_density,new_volume));
                    }
                    else
                    {
                        throw new Exception("Invalid type for an element!\n");
                    }
                }
                else if (command==4)
                {
                    Box[] array_of_elements= service.get_all_elements();
                    boolean check=false;
                    System.out.println("List of elements: \n");
                    for (Box array_of_element : array_of_elements) {
                        if (array_of_element != null) {
                            System.out.print(array_of_element.to_String());
                            check = true;
                        }
                    }
                    if(!check)
                    {
                        System.out.println("No element to display!\n");
                    }
                }
                else if(command==5)
                {
                    final int fixed_weight=200;
                    Box[] array_of_elements= service.filter_elements(fixed_weight);
                    boolean check=false;
                    System.out.println("List of elements: \n");
                    for (Box array_of_element : array_of_elements) {
                        if (array_of_element != null) {
                            System.out.print(array_of_element.to_String());
                            check = true;
                        }
                    }
                    if(!check)
                    {
                        System.out.println("No element to display!\n");
                    }
                }
                else if(command==0)
                {
                    System.out.println("Program closed!");
                    break;
                }
                else
                    throw new Exception("Invalid command!\n");
            }
        catch (Exception exception)
        {
            System.out.println(exception.getMessage());
        }
    }
}