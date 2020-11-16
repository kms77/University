package Model;
import Model.ADT.Dictionary.My_Dictionary;
import Model.ADT.Stack.My_Stack;
import Model.ADT.List.My_List;
import Model.Statement.Statement_Interface;
import Model.Value.Value;

public class Program_State {
    My_Dictionary<String, Value> symbol_table;
    My_Stack<Statement_Interface> execution_stack;
    My_List<Value> output;
    public Program_State(My_Stack<Statement_Interface> execution_stack, My_Dictionary<String,Value> symbol_table, My_List<Value> output, Statement_Interface program)
    {
        this.execution_stack=execution_stack;
        this.symbol_table=symbol_table;
        this.output=output;
        execution_stack.push(program);
    }
    public My_Dictionary<String, Value> Get_Symbol_Table(){
        return this.symbol_table;
    }
    public My_Stack<Statement_Interface> Get_Stack(){
        return this.execution_stack;
    }
    public My_List<Value> Get_Output()
    {
        return this.output;
    }
    public void Clear_Program()
    {
        this.execution_stack.clear();
        this.symbol_table.clear();
        this.output.clear();
    }
    public String toString()
    {
        return  "Execution Stack= {" + execution_stack +
                "}\nSymbol Table= { " +symbol_table+
                "}\nOutput= { "+output+ "}";

    }
}
