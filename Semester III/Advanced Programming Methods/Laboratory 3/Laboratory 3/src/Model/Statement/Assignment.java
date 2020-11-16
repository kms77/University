package Model.Statement;
import Exception.Expression_Exception;
import Model.ADT.Dictionary.My_Dictionary;
import Model.Program_State;
import Model.Expression.Expression;
import Model.Value.Value;
public class Assignment  implements Statement_Interface{
    String id;
    Expression expression;
    public Assignment(String id, Expression expression)
    {
        this.id=id;
        this.expression=expression;
    }
    @Override
    public Program_State execution(Program_State state) throws Expression_Exception{
        My_Dictionary<String,Value> symbol_table= state.Get_Symbol_Table();
        if (symbol_table.get(id)!=null){
            Value first_value=expression.evaluation(symbol_table);
            if(first_value.Get_Type().equals(symbol_table.get(id).Get_Type())) {
                symbol_table.put(id, first_value);
            }
            else
                throw new Expression_Exception("Expression type and variable type do not match!\n");
            }
            else
                throw new Expression_Exception("Variable id not declared!\n");
            return state;
    }
    @Override
    public String toString(){
        return id+ " = "+ expression;
    }
}
