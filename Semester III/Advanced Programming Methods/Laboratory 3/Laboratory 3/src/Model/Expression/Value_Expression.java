package Model.Expression;
import Model.ADT.Dictionary.Dictionary_Interface;
import Model.Value.Value;
public class Value_Expression implements Expression{
    private final Value value;
    public Value_Expression(Value value){
        this.value=value;
    }
    @Override
    public Value evaluation(Dictionary_Interface<String,Value> table){
        return this.value;
    }
    @Override
    public String toString()
    {
        return this.value.toString();
    }
}
