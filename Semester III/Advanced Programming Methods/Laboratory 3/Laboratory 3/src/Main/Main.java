package Main;
import Controller.Service;
import Repository.Interface_Repository;
import Repository.Repository;
import View.User_Interface;
public class Main {

    public static void main(String[] args) {

        Interface_Repository repository = new Repository();
        Service service = new Service((repository));

        service.Set_Display_Tag(true);

        User_Interface user_interface = new User_Interface(service);
        user_interface.run();
    }
}
