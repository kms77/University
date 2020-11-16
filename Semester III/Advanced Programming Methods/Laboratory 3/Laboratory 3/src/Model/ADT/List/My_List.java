package Model.ADT.List;
import Exception.ADT_Exception;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;
public class My_List<T> implements List_Interface<T>{
    private final List<T> list;
    public My_List(){
        list=new ArrayList<>();
    }
    @Override
    public T get(int index) throws ADT_Exception
    {
        if(index>this.list.size()){
            throw new ADT_Exception(" Index out of range!");
        }
        return list.get(index);
    }
    @Override
    public int size(){
        return list.size();
    }
    @Override
    public void clear()
    {
        list.clear();
    }
    @Override
    public boolean add(T value){
        return list.add(value);
    }
    @Override
    public boolean remove(T value){
        return list.remove(value);
    }
    @Override
    public Stream<T> stream(){
        return this.list.stream();
    }
    @Override
    public String toString(){
        return list.toString();
    }
}
