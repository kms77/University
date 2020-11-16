package Model.ADT.List;
import Exception.ADT_Exception;
import java.util.stream.Stream;
public interface List_Interface<T> {
    T get(int index) throws ADT_Exception;
    int size();
    boolean add (T value);
    boolean remove(T value);
    void clear();
    Stream<T> stream();
}
