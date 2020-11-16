package Model.Expression;
import Exception.Expression_Exception;
import Model.ADT.Dictionary.Dictionary_Interface;
import Model.Value.Value;
public class Variable_Expression implements Expression{
    String id;
    public Variable_Expression(String id)
    {
        this.id=id;
    }
    @Override
    public Value evaluation(Dictionary_Interface<String,Value>table) throws Expression_Exception{
        Value value=table.get(id);
        if(value==null)
        {
            throw new Expression_Exception("Variable not declared!");
        }
        return value;
    }
    @Override
    public String toString()
    {
        return id;
    }
}
