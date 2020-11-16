package View;
import Controller.Service;
import Model.Program_State;
import Model.ADT.Dictionary.My_Dictionary;
import Model.ADT.Stack.My_Stack;
import Model.ADT.List.My_List;
import Model.Expression.Arithmetic_Expression;
import Model.Expression.Value_Expression;
import Model.Expression.Variable_Expression;
import Model.Statement.*;
import Model.Type.Integer_Type;
import Model.Type.Bool_Type;
import Model.Value.Integer_Value;
import Model.Value.Bool_Value;
import Model.Value.Value;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class User_Interface {
    private final Service service;
    private boolean running;
    private final My_Stack<Statement_Interface> execution_stack;
    private final My_Dictionary<String, Value> symbol_table;
    private final My_List<Value> output;
    private final My_List<Statement_Interface> program;
    private Program_State initial_state;
    public User_Interface(Service service){
        running=true;
        execution_stack=new My_Stack<>();
        symbol_table=new My_Dictionary<>();
        output=new My_List<>();
        program=new My_List<>();
        initial_state=null;
        this.service=service;
    }
    static void print_value(Value value){
        if(value.Get_Type().equals(new Integer_Type())){
            System.out.println(((Integer_Value)value).Get_Value());
        }
        else if (value.Get_Type().equals(new Bool_Type())){
            System.out.println(((Bool_Value)value).Get_Value());
        }
    }
    static void print_all_output(Program_State initial_state){
        initial_state.Get_Output().stream().forEach(User_Interface::print_value);
        try{
            System.out.println("Press enter to continue ...");
            System.in.read();
        }
        catch(IOException exception){
            exception.printStackTrace();
        }
    }
    void handle_selection(int selection) throws Exception{
        selection=Math.abs(selection)-1;
        if(selection==-1){
            running=false;
            System.out.println("Program closed!");
            return;
        }
        if(selection<program.size()){
            Statement_Interface statement= program.get(selection);
            if(statement==null){
                System.out.println("Invalid selection!\n");
            }
            else{
                initial_state= new Program_State(execution_stack,symbol_table,output,statement);
                this.service.Add(initial_state);
                try{
                    this.service.All_Step();
                }
                catch (Exception exception){
                    exception.printStackTrace();
                }
                print_all_output(initial_state);
            }
        }
        else
        {
            System.out.println("Program index not in the list of programs!\n");
        }
    }
    void Preload_Programs(My_List<Statement_Interface> program){
        // int v;
        // v=2;
        // Print(v)
        Statement_Interface first_example = new Composite(new Variable_Declaration("v",new Integer_Type()),
                new Composite(new Assignment("v",new Value_Expression(new Integer_Value(2))),
                        new Print(new
                                Variable_Expression("v"))));

        // int a;
        // int b;
        // a=2+3*5;
        // b=a+1;
        // Print(b);
        Statement_Interface second_example = new Composite( new Variable_Declaration("a",new Integer_Type()),
                new Composite(new Variable_Declaration("b",new Integer_Type()),
                        new Composite(new Assignment("a", new Arithmetic_Expression('+',new Value_Expression(new Integer_Value(2)),new
                                Arithmetic_Expression('*',new Value_Expression(new Integer_Value(3)), new Value_Expression(new Integer_Value(5))))),
                                new Composite(new Assignment("b",new Arithmetic_Expression('+',new Variable_Expression("a"), new
                                        Value_Expression(new Integer_Value(1)))), new Composite(new Print(new Variable_Expression("b")), new Print(new Variable_Expression("a")))))));

        // bool x;
        // int y;
        // x=true;
        // (If x )
        // Then y=2;
        // Else y=3;
        // Print(y);
        Statement_Interface third_example = new Composite(new Variable_Declaration("x",new Bool_Type()),
                new Composite(new Variable_Declaration("y", new Integer_Type()),
                        new Composite(new Assignment("x", new Value_Expression(new Bool_Value(true))),
                                new Composite(new If(new Variable_Expression("x"),new Assignment("y",new Value_Expression(new
                                        Integer_Value(2))), new Assignment("y", new Value_Expression(new Integer_Value(3)))), new Print(new
                                        Variable_Expression("y"))))));
        program.add(first_example);
        program.add(second_example);
        program.add(third_example);
    }
    void reset(){
        this.output.clear();
        this.symbol_table.clear();
    }
    public void run(){
        Preload_Programs(program);
        BufferedReader buffer= new BufferedReader(new InputStreamReader(System.in));
        while(running) {
            System.out.println("               ---------  MAIN  ---------                 ");
            System.out.println("1.Program one:  int v; v=2; Print(v)");
            System.out.println("2.Program two:  int a; int b; a=2+3*5; b=a+1; Print(b); Print(a);");
            System.out.println("3.Program three:  bool x; int y; x=true; (If x Then y=2 ELSE y=3); Print(y);");
            System.out.println("0.Close the program;");

            try {
                System.out.println("Choose a program: ");
                int selection = Integer.parseInt(buffer.readLine());
                handle_selection(selection);
                }
            catch (NumberFormatException exception)
            {
                System.out.println("Please input a number!\n");
            }
            catch (Exception exception) {
                exception.printStackTrace();
            }
            reset();
        }
    }
}
