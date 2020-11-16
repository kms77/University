package Repository;
import Model.ADT.List.My_List;
import Model.Program_State;
import Exception.ADT_Exception;
public class Repository  implements Interface_Repository{
    My_List<Program_State> state_list;
    public Repository()
    {
        state_list=new My_List<>();
    }
    @Override
    public void Add(Program_State state){
        state_list.add(state);
    }
    @Override
    public void Remove(Program_State state){
        state_list.remove(state);
    }
    @Override
    public Program_State Get_Current_Program() throws ADT_Exception {
        Program_State current_state= this.state_list.get(0);
        this.state_list.remove(current_state);
        return current_state;
    }
}
