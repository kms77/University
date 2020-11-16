package Model.Expression;
import Exception.Expression_Exception;
import Model.ADT.Dictionary.Dictionary_Interface;
import Model.Type.Integer_Type;
import Model.Value.Integer_Value;
import Model.Value.Value;
public class Arithmetic_Expression implements Expression{
    private static final int INVALID_OPERATOR=4;
    private final Expression first_expression;
    private final Expression second_expression;
    private final int operator;
    public Arithmetic_Expression(char operator,Expression first_expression, Expression second_expression)
    {
        switch (operator){
            case '+' -> this.operator=0;
            case '-' -> this.operator=1;
            case '*' -> this.operator=2;
            case '/' ->this.operator=3;
            default -> this.operator=INVALID_OPERATOR;
        }
        this.first_expression=first_expression;
        this.second_expression=second_expression;
    }
    private enum Operator_Type{
        Addition,
        Subtraction,
        Multiplication,
        Division,
    }
    @Override
    public Value evaluation(Dictionary_Interface<String,Value> table) throws Expression_Exception {
        Value first_value, second_value;
        if (this.operator == INVALID_OPERATOR) {
            throw new Expression_Exception("Invalid arithmetic operator");
        }
        first_value = first_expression.evaluation(table);
        if (first_value.Get_Type().equals(new Integer_Type())) {
            second_value = second_expression.evaluation(table);
            if (second_value.Get_Type().equals(new Integer_Type())) {
                int first_number, second_number;
                first_number = ((Integer_Value) first_value).Get_Value();
                second_number = ((Integer_Value) second_value).Get_Value();
                Operator_Type operator_type = Operator_Type.values()[operator];
                switch (operator_type) {
                    case Addition -> {
                        return new Integer_Value(first_number + second_number);
                    }
                    case Subtraction -> {
                        return new Integer_Value(first_number - second_number);
                    }
                    case Multiplication -> {
                        return new Integer_Value(first_number * second_number);
                    }
                    case Division -> {
                        if (second_number == 0)
                            throw new Expression_Exception("Division by zero error!");
                        else
                            return new Integer_Value(first_number / second_number);
                    }
                }
            } else
                throw new Expression_Exception("Second operand does not have an integer value!");
        } else
            throw new Expression_Exception("First operand does not have an integer value!");
        return null;
    }
    @Override
    public String toString(){
        char display_operator;
        switch (operator){
            case 0 ->display_operator='+';
            case 1 ->display_operator='-';
            case 2 ->display_operator='*';
            case 3 ->display_operator='/';
            default -> display_operator=' ';
        }
        return "" + first_expression+ display_operator+second_expression;
    }
}
