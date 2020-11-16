package Model.Expression;
import Exception.Expression_Exception;
import Model.ADT.Dictionary.Dictionary_Interface;
import Model.Type.Bool_Type;
import Model.Value.Value;
import Model.Value.Bool_Value;
import java.util.stream.Stream;

public class Logic_Expression implements Expression{
    public static final int INVALID_OPERATOR=2;
    private final Expression first_expression;
    private final Expression second_expression;
    private final int operator;
    public Logic_Expression(String operator,Expression first_expression,Expression second_expression)
    {
        switch(operator){
            case "&&" -> this.operator=0;
            case "||" -> this.operator=1;
            default -> this.operator=INVALID_OPERATOR;
        }
        this.first_expression=first_expression;
        this.second_expression=second_expression;
    }
    enum Operator_Type{
        And,
        Or,
    }
    @Override
    public Value evaluation(Dictionary_Interface<String,Value> table) throws Expression_Exception{
        Value first_value,second_value;
        if(this.operator==INVALID_OPERATOR)
        {
            throw new Expression_Exception("Invalid logic operator");
        }
        first_value=first_expression.evaluation(table);
        if(first_value.Get_Type().equals(new Bool_Type()))
        {
            second_value=second_expression.evaluation(table);
            if(second_value.Get_Type().equals(new Bool_Type()))
            {
                Bool_Value first_bool=(Bool_Value) first_value;
                Bool_Value second_bool=(Bool_Value) second_value;
                boolean First_Bool,Second_Bool;
                First_Bool=first_bool.Get_Value();
                Second_Bool=second_bool.Get_Value();
                Operator_Type operator_type=Operator_Type.values()[operator];
                switch (operator_type){
                    case And -> {
                        return new Bool_Value(First_Bool && Second_Bool);
                    }
                    case Or -> {
                        return new Bool_Value(First_Bool || Second_Bool);
                    }
                }
            }
            else
                throw  new Expression_Exception("Second operand is not a boolean!\n");
        }
        else
             throw new Expression_Exception("First operand is not a boolean!\n");
        return null;
    }
    @Override
    public String toString(){
        String display_operator;
        switch (operator){
            case 0 -> display_operator= "&&";
            case 1 -> display_operator= "||";
            default -> display_operator= " invalid ";
        }
        return "" + first_expression+ " " + display_operator + " " + second_expression;
    }
}
