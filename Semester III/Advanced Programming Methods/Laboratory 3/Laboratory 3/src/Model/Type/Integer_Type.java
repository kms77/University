package Model.Type;

public class Integer_Type implements Type{
    @Override
    public boolean equals(Object object){
        return object instanceof Integer_Type;
    }

    @Override
    public String toString ()
    {
        return "int";
    }
}
