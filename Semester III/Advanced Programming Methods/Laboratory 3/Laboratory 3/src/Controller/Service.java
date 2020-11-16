package Controller;
import Exception.ADT_Exception;
import Model.ADT.Stack.My_Stack;
import Model.Program_State;
import Model.Statement.Statement_Interface;
import Repository.Interface_Repository;

public class Service {
    private final Interface_Repository repository;
    private boolean display_tag;
    public Service(Interface_Repository repository){
        this.repository=repository;
        this.display_tag=false;
    }
    public void Add(Program_State state)
    {
        this.repository.Add(state);
    }
    public void Set_Display_Tag(boolean display_tag){
        this.display_tag=display_tag;
    }
    public Program_State one_step(Program_State state) throws Exception{
        My_Stack<Statement_Interface>stack=state.Get_Stack();
        if(stack.isEmpty()){
            throw new ADT_Exception("Execution state is empty!\n");
        }
        Statement_Interface current_statement=stack.pop();
        return current_statement.execution(state);
    }
    public void All_Step() throws Exception{
        Program_State program=repository.Get_Current_Program();
        if(this.display_tag){
            System.out.println(program);
        }
        while(!program.Get_Stack().isEmpty()){
            program=one_step(program);
            if(this.display_tag){
                System.out.println(program);
            }
        }
    }
}

