package Model.ADT.Stack;
import Exception.ADT_Exception;
import java.util.stream.Stream;
import java.util.Stack;
public class My_Stack<T> implements Stack_Interface<T> {
    private final Stack<T> stack;
    public My_Stack(){
        stack=new Stack<>();
    }
    @Override
    public T pop()throws ADT_Exception{
        T object =stack.pop();
        if(object ==null){
            throw new ADT_Exception(" Stack is empty!");
        }
        return object;
    }
    @Override
    public void push(T value){
        stack.push(value);
    }
    @Override
    public T peek() throws ADT_Exception{
        T object= stack.peek();
        if(object==null)
        {
            throw new ADT_Exception("Stack is empty!");
        }
        return object;
    }
    @Override
    public boolean isEmpty(){
        return stack.empty();
    }
    @Override
    public void clear(){
        stack.clear();
    }
    @Override
    public Stream<T> stream(){
        return this.stack.stream();
    }
    @Override
    public String toString(){
        return stack.toString();
    }
}
