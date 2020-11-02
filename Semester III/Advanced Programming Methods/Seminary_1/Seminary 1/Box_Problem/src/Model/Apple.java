package Model;

/*
Class which defines an apple object
 */
public class Apple implements Box {
    int id_number;
    String type;
    double density,volume;
    public Apple(int id_number,String type,double density, double volume)
    {
        this.id_number=id_number;
        this.type=type;
        this.density=density;
        this.volume=volume;
    }
   /*
    Function which returns the id number of the object
    Input:-
    Output: int- the id of the object
    */
    @Override
    public int Get_Id() { return this.id_number; }

    /*
    Function which returns the type of the object
    Input: -
    Output: String- the type of the object
     */
    @Override
    public String Get_Type() { return this.type; }

    /*
    Function which computes the weight of the object
    Input: -
    Output:double- the weight of the object
     */
    @Override
    public double Get_Weight()
    {
        return this.density*this.volume;
    }

    /*
    Function which returns the density of the object
    Input: -
    Output: double- the density of the object
     */
    @Override
    public double Get_Density()
    {
        return this.density;
    }

    /*
    Function which returns the volume of the object
    Input: -
    Output: double- the volume of the object
     */
    @Override
    public double Get_Volume() { return this.volume; }

    /*
    Function which sets a value for the density of the object
    Input: double- new_density the new density value of the object
    Output: -
     */
    @Override
    public void Set_Density(double new_density)
    {
        this.density=new_density;
    }

    /*
    Function which sets a value for the volume of the object
    Input: double- new_volume the new volume value of the object
    Output: -
     */
    @Override
    public void Set_Volume(double new_volume) { this.volume=new_volume;}

    /*
    Function which returns a string in order to print an apple object( it is to string method )
    Input: -
    Output: string- which will be used for printing an apple object
     */
    @Override
    public String to_String()
    {
        return "-------------"+ "\nId number: "+ this.id_number+"\nType: "+this.type+
                "\nDensity: "+this.density+" g/cm3"+"\nVolume: "+this.volume+
                " cm3"+"\nWeight: "+this.Get_Weight()+" g"+"\n-------------\n";
    }
}

