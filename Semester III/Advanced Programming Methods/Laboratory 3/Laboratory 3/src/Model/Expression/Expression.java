package Model.Expression;
import Exception.Expression_Exception;
import Model.ADT.Dictionary.Dictionary_Interface;
import Model.Value.Value;
public interface Expression {
    Value evaluation(Dictionary_Interface<String, Value> table) throws Expression_Exception;
}
