package Model.Statement;
import Model.Program_State;
import Model.ADT.Dictionary.My_Dictionary;
import Model.Type.Bool_Type;
import Model.Type.Integer_Type;
import Model.Type.Type;
import Model.Value.Value;
import Model.Value.Bool_Value;
import Model.Value.Integer_Value;
public class Variable_Declaration implements Statement_Interface{
    private static final int DEFAULT_INT_VALUE=0;
    private static final boolean DEFAULT_BOOL_VALUE=false;
    private  final String name;
    private final Type type;
    public Variable_Declaration(String name, Type type){
        this.name=name;
        this.type=type;
    }
    @Override
    public Program_State execution(Program_State state)
    {
        My_Dictionary<String,Value> symbol_table=state.Get_Symbol_Table();
        if(symbol_table.get(name)==null)
        {
            if(type.equals(new Integer_Type()))
            {
                symbol_table.put(name, new Integer_Value(DEFAULT_INT_VALUE));
            }
            else
                if(type.equals(new Bool_Type()))
                {
                    symbol_table.put(name, new Bool_Value(DEFAULT_BOOL_VALUE));
                }
        }
        return state;
    }
    @Override
    public String toString()
    {
        return type+" "+name;
    }
}
