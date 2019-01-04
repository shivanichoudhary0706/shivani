package product;

import product.Product;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

public class ProductRepository {
    HashMap<Integer,Product> map=new HashMap<>();
    public boolean add1(Product prd){
        if(!map.containsKey(prd.getId())){
            map.put(prd.getId(), prd);
            return true;
        }
        return false;
    }
    public boolean removeId(int id){
        int i; 
        for(i=0;i<map.size();i++){
             if(map.get(i).getId()==id){
                 break;
             }
        } 
        if(i!=map.size()){
        System.out.println(map.get(i).getId());
                 map.remove(i);
                 return true;
        }  
        return false;
        
    }
    public Product get(int id){
        return map.get(new Integer(id));
    }
    public Collection<Product> getProducts(){
        return map.values();
    }
    public Set <Integer> getId(){
        
        return map.keySet();
    }
    /*public Set <Integer> setRate(double rate){
        
    }*/

    Object getId(int i) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
}
