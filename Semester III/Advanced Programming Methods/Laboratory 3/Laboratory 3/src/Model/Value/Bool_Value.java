package Model.Value;
import Model.Type.Type;
import Model.Type.Bool_Type;
public class Bool_Value implements Value{
    private final boolean value;
    public Bool_Value(boolean value){
        this.value=value;
    }
    public boolean Get_Value()
    {
        return this.value;
    }
    @Override
    public Type Get_Type()
    {
        return new Bool_Type();
    }
    @Override
    public String toString()
    {
        return ""+this.value;
    }
}
