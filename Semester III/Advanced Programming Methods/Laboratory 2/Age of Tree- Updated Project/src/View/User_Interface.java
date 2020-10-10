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
                1)Add a new tree;
                2)Delete a tree with a given age;
                3)Get all trees with an age grater than 3 years;
                4)Display all trees;
                0)Exit;
                --------------------
                Choose:""";
        while (true)
            try {
                System.out.println(Menu);
                int command = scanner.nextInt();
                if (command == 1)
                {
                    String Second_Menu = """
                            Type of tree
                            --------------------
                            1)Apple tree
                            2) Pear tree
                            3) Cherry tree
                            --------------------
                            Choose:""";
                    System.out.println(Second_Menu);
                    int get_command = scanner.nextInt();
                    System.out.println("Age of the tree:");
                    int age_of_the_tree = scanner.nextInt();
                    if (get_command == 1) {
                        service.add_tree(new Apple_Tree(age_of_the_tree));
                    }
                    else if (get_command == 2)
                    {
                       service.add_tree(new Pear_Tree(age_of_the_tree));
                    }
                    else if (get_command==3)
                    {
                        service.add_tree(new Cherry_Tree(age_of_the_tree));
                    }
                    else
                    {
                        System.out.println("Invalid command!\n");
                    }
                }
                else if(command==2)
                {
                    String Second_Menu = """
                            Type of tree
                            --------------------
                            1)Apple tree
                            2) Pear tree
                            3) Cherry tree
                            --------------------
                            Choose:""";
                    System.out.println(Second_Menu);
                    int get_command = scanner.nextInt();
                    System.out.println("Age of the tree:");
                    int age_of_the_tree = scanner.nextInt();
                    if (get_command == 1) {
                        service.delete_tree(new Apple_Tree(age_of_the_tree));
                    }
                    else if (get_command == 2)
                    {
                        service.delete_tree(new Pear_Tree(age_of_the_tree));
                    }
                    else if (get_command==3)
                    {
                        service.delete_tree(new Cherry_Tree(age_of_the_tree));
                    }
                    else
                    {
                        System.out.println("Invalid command!\n");
                    }
                }
                else if(command==3)
                {
                    int age_of_tree=3;
                    boolean check=false;
                    Tree[] array_of_elements= service.search_tree(age_of_tree);
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
                else if(command==4)
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
                else if(command==0)
                {
                    System.out.println("Program closed!");
                    break;
                }
                else
                    throw new Exception(("Invalid command!\n"));
            }
        catch (Exception exception)
        {
            System.out.println(exception.getMessage());
        }
    }
}
