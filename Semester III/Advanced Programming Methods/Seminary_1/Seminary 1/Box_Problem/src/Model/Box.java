package Model;

/*
  Here is the interface of our domain module
 */
public interface Box {
      int Get_Id();
      String Get_Type();
      double Get_Weight();
      double Get_Density();
      double Get_Volume();
      void Set_Density(double new_density);
      void Set_Volume(double new_volume);
      String to_String();
}
