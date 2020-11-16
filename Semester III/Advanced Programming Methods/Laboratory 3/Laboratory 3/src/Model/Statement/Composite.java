package Model.Statement;
import Exception.Expression_Exception;
import Model.ADT.Stack.My_Stack;
import Model.Program_State;
public class Composite implements Statement_Interface{
    Statement_Interface first_element;
    Statement_Interface second_element;
    public Composite(Statement_Interface first_element,Statement_Interface second_element)
    {
        this.second_element=second_element;
        this.first_element=first_element;
    }
    @Override
    public Program_State execution(Program_State state) throws Expression_Exception{
        My_Stack<Statement_Interface> stack=state.Get_Stack();
        stack.push(second_element);
        stack.push(first_element);
        return state;
    }
    @Override
    public String toString()
    {
        return "{" + " "+first_element+
                " ,"+ second_element+"}";
    }
}
