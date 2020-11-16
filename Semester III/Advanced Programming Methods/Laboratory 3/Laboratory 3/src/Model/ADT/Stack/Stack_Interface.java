package Model.ADT.Stack;
import Exception.ADT_Exception;
import java.util.stream.Stream;
public interface Stack_Interface<T> {
    T pop() throws ADT_Exception;
    void push(T value);
    T peek() throws ADT_Exception;
    void clear();
    boolean isEmpty();
    Stream<T> stream();
}
