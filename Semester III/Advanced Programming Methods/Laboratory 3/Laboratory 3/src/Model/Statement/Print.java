package Model.Statement;
import Exception.Expression_Exception;
import Model.ADT.List.My_List;
import Model.Program_State;
import Model.Expression.Expression;
import Model.Value.Value;
public class Print implements Statement_Interface{
    Expression expression;
    public Print(Expression expression){
        this.expression=expression;
    }
    @Override
    public Program_State execution(Program_State state)throws Expression_Exception {
        My_List<Value> my_list= state.Get_Output();
        my_list.add(expression.evaluation(state.Get_Symbol_Table()));
        return state;
    }
    @Override
    public String toString()
    {
        return "Print {" + expression.toString()+"}";
    }
}
