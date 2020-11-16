package Model.Type;

public class Bool_Type implements Type {
    @Override
    public boolean equals(Object object)
    {
        return object instanceof Bool_Type;
    }
    @Override
    public String toString ()
    {
        return "bool";
    }
}
