package Model.ADT.Dictionary;
import Exception.ADT_Exception;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;
public class My_Dictionary <K,V> implements Dictionary_Interface<K,V>{
     private final HashMap<K,V> hashMap;
     public My_Dictionary(){
         hashMap=new HashMap<>();
     }
     @Override
    public void put(K key, V value){
         hashMap.put(key,value);
     }
     @Override
    public V get(K key){
         return hashMap.get(key);
     }
     @Override
    public V remove(K key) throws ADT_Exception{
         V was_removed=hashMap.remove(key);
         if(was_removed==null)
         {
             throw new ADT_Exception(" Key "+ key+" not present in dictionary;");
         }
         return hashMap.remove(key);
     }
     @Override
    public void clear(){
         this.hashMap.clear();
     }
     @Override
    public Set<K> keyset(){
         return hashMap.keySet();
     }
     @Override
    public Collection<V> values() throws ADT_Exception{
         if(hashMap.size()==0)
         {
             throw new ADT_Exception(" Dictionary is empty!\n");
         }
         return hashMap.values();
     }
     @Override
    public String toString(){
         return this.hashMap.toString();
     }
}
