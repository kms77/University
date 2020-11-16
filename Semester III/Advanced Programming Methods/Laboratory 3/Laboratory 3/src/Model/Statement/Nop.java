package Model.Statement;
import Model.Program_State;
public class Nop implements Statement_Interface{
    @Override
    public Program_State execution(Program_State state){
        return state;
    }
    @Override
    public String toString(){
        return "nop";
    }
}
