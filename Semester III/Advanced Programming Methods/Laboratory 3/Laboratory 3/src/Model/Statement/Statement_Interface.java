package Model.Statement;
import Exception.Expression_Exception;
import Model.Program_State;
public interface Statement_Interface {
    Program_State execution(Program_State state) throws Expression_Exception;
}
