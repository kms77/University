//  Laboratory 1:
//  Please write, compile and run simple program in Java: declare and use a class;
//  Define the class Colors
public class Colors {
    // instance variables of the class
    String black;
    String white;

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
           Colors object= new Colors("Black color!","White color!");
           object.get_black();
           object.get_white();
    }
}
