package Model.Statement;
import Exception.Expression_Exception;
import Model.ADT.Stack.My_Stack;
import Model.ADT.Dictionary.My_Dictionary;
import Model.Expression.Expression;
import Model.Type.Bool_Type;
import Model.Value.Value;
import Model.Value.Bool_Value;
import Model.Program_State;
public class If implements Statement_Interface{
    Expression expression;
    Statement_Interface Then_Statement;
    Statement_Interface Else_Statement;
    public If(Expression expression, Statement_Interface Then_Statement, Statement_Interface Else_Statement){
        this.expression=expression;
        this.Then_Statement=Then_Statement;
        this.Else_Statement=Else_Statement;
    }
    @Override
    public Program_State execution(Program_State state) throws Expression_Exception{
        My_Dictionary<String,Value> symbol_table=state.Get_Symbol_Table();
        My_Stack<Statement_Interface> stack=state.Get_Stack();
        Value condition=expression.evaluation(symbol_table);
        if(!condition.Get_Type().equals(new Bool_Type()))
        {
            throw new Expression_Exception("Condition expression is not a boolean!");
        }
        else{
            if(((Bool_Value)condition).Get_Value()){
                stack.push(Then_Statement);
            }
            else
            {
                stack.push(Else_Statement);
            }
        }
    return state;
    }
    @Override
    public String toString(){
        return "if "+expression+" then"+Then_Statement+ " else"+Else_Statement;
    }
}
