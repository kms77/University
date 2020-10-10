package View;
import Model.*;
import Repository.Repository;
import Controller.Service;
import java.util.Scanner;
public class User_Interface
{
    public static void main(String[] args)
    {
        Repository repository = new Repository();
        Service service = new Service(repository);
        Scanner scanner = new Scanner(System.in);
        String Menu = """
                --------MENU--------
                1)Display all trees;
                2)Get all trees with an age grater than 3 years;
                0)Exit;
                --------------------
                Choose:""";
        Apple_Tree first_apple_tree= new Apple_Tree(2);
        Apple_Tree second_apple_tree= new Apple_Tree(5);
        Pear_Tree first_pear_tree= new Pear_Tree(3);
        Pear_Tree second_pear_tree= new Pear_Tree(5);
        Cherry_Tree first_cherry_tree= new Cherry_Tree(7);
        Cherry_Tree second_cherry_tree= new Cherry_Tree(9);
        try
        {
            service.add_tree(first_apple_tree);
            service.add_tree(second_apple_tree);
            service.add_tree(first_pear_tree);
            service.add_tree(second_pear_tree);
            service.add_tree(first_cherry_tree);
            service.add_tree(second_cherry_tree);
        }
        catch (Exception exception)
        {
            System.out.println(exception.getMessage());
        }
        while (true)
        {
                System.out.println(Menu);
                int command = scanner.nextInt();
                if (command == 1)
                {
                    Tree[] array_of_elements= service.get_all_trees();
                    boolean check=false;
                    for (int i=0;i< array_of_elements.length;i++) {
                        if(array_of_elements[i]!=null)
                        {
                            System.out.print(array_of_elements[i]);
                            check=true;
                        }
                    }
                    if(!check)
                    {
                        System.out.println("No tree to display!\n");
                    }
                }
                else if(command==2)
                {
                    int age_of_tree=3;
                    boolean check=false;
                    Tree[] array_of_elements= service.filter_tree(age_of_tree);
                    for (int i=0;i< array_of_elements.length;i++) {
                        if(array_of_elements[i]!=null)
                        {
                            System.out.print(array_of_elements[i]);
                            check=true;
                        }
                    }
                    if(!check)
                    {
                        System.out.println("No tree to display!\n");
                    }
                }
                else if(command==0)
                {
                    System.out.println("Program closed!");
                    break;
                }
                else
                    System.out.println("Invalid command!\n");
            }
    }
}
