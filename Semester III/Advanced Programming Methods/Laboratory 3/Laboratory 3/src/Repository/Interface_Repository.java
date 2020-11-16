package Repository;
import Model.Program_State;
import Exception.ADT_Exception;
public interface Interface_Repository {
    Program_State Get_Current_Program() throws ADT_Exception;
    void Add(Program_State state);
    void Remove(Program_State state);
}
