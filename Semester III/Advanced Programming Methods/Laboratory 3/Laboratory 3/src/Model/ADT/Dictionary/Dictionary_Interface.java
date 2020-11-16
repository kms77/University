package Model.ADT.Dictionary;
import Exception.ADT_Exception;
import java.util.Collection;
import java.util.Set;
public interface Dictionary_Interface<K,V> {
    void put(K key,V value);
    V get(K key);
    V remove(K key) throws ADT_Exception;
    Set<K> keyset();
    Collection<V> values() throws ADT_Exception;
   void clear();
}
