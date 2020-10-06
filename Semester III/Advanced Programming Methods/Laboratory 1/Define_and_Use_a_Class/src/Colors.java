//  Laboratory 1:
//  Please write, compile and run simple programs in Java: declare and use a class,
//  derive a subclass, override a method, use static fields and methods, use an exception;

// define the class Other_Colors
class Other_Colors{
    // instance variables of the class
    String other;

    // Constructor of the class
    public Other_Colors(String other)
    {
        this.other=other;
    }

    /*
    Function to print a message
     */
    void get_other()
    {
        System.out.println(other);
    }

    /*
    Function to print all other colors
     */
    void to_String()
    {

    }
}

// define the subclass of the Other_Colors
class Subclass extends Other_Colors{

    // invoking base-class(Other_Colors) constructor
    public Subclass(String other) {
        super(other);
    }

    /*
    Function to print a message
    Return:-
     */
    static void get_red()
    {
        System.out.println("Red color!");
    }

    /*
    Function to print a message
    Return:-
     */
    static void get_blue()
    {
        System.out.println("Blue color!");
    }

    /*
    Function to print all the other colors
     */
    @Override
    void to_String()
    {
        get_other();
        get_blue();
        get_red();
    }
}
//  Define the class Colors
public class Colors {
    // instance variables of the class
    String black;
    String white;
    static String start= "Program started!";

    // Constructor of the class
    public Colors(String black,String white)
    {
        this.black=black;
        this.white=white;
    }
    public void get_white()
        /*
       Function which prints the string variable white
       Return: -
       */
    {
        System.out.println(white);
    }
    public void get_black()
        /*
        Function which prints the string variable black
        */
    {
        System.out.println(black);
    }

    public static void main(String[] args) {

        try
        {
            //code that may raise exception
            System.out.println(start);
        }
        catch(Exception exception)
        {
            System.out.println(exception);
        }
        Colors object= new Colors("Black color!","White color!");
        object.get_black();
        object.get_white();
        Subclass others= new Subclass("Other colors: ");
        others.to_String();
    }
}
