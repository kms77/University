package Test;
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
import Model.Value.Integer_Value;
import Model.Value.Bool_Value;
import Exception.*;
import Repository.Repository;
import org.junit.Test;
public class Unit_Test {
    @Test(expected = Expression_Exception.class)
    public void Test_Arithmetic_Division_By_Zero() throws Exception {
        Repository repository = new Repository();
        Service service = new Service(repository);
        // int a = 8/0
        Statement_Interface example = new Composite(new Variable_Declaration("a", new Integer_Type()),
                new Composite(new Assignment("a", new Arithmetic_Expression('/'
                        , new Value_Expression(new Integer_Value(8)), new Value_Expression(new Integer_Value(0)))), new Print(new Variable_Expression("a"))));
        Program_State program_state = new Program_State(new My_Stack<>(), new My_Dictionary<>(), new My_List<>(), example);
        service.Add(program_state);
        service.All_Step();
    }
    @Test(expected = Expression_Exception.class)
    public void Test_Arithmetic_Expresion_Different_Types() throws Exception{
        Repository repository = new Repository();
        Service service = new Service(repository);
        // print(true + 3)
        Statement_Interface example = new Print(new Arithmetic_Expression('+', new Value_Expression(new Bool_Value(true)), new Value_Expression(new Integer_Value(5))));
        Program_State program_state = new Program_State(new My_Stack<>(), new My_Dictionary<>(), new My_List<>(), example);
        service.Add(program_state);
        service.All_Step();
    }
}
