package Model.Value;
import Model.Type.Type;
import Model.Type.Integer_Type;
public class Integer_Value implements Value{
    private final int value;
    public Integer_Value(int value){
        this.value=value;
    }
    public int Get_Value()
    {
        return this.value;
    }
    @Override
    public Type Get_Type()
    {
        return new Integer_Type();
    }
    @Override
    public  String toString()
    {
        return  ""+this.value;
    }
}
