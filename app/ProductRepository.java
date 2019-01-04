package app;
import app.Product;
import java.util.Comparator;

public class ProductRepository {
    private java.util.ArrayList<Product> products=new java.util.ArrayList<>();
    public java.util.ArrayList<Product> getproducts(){
        return products;
    }
    public void add(int id,String name,String category,double price,boolean available){
        products.add(new Product(id,name,category,price,available));
    }
   /* public boolean removeById(int id){
        int i;        
//print
        for(i=0;i<products.size();i++){
        System.out.println((i+1));
        System.out.println("Id: "+products.get(i).getId()+"\nCategory: "+products.get(i).getCategory()+"\nPrice: "+products.get(i).getPrice()+"\nAvailable: "+products.get(i).isAvailable()+"\n");
        }
        
        for(i=0;i<products.size();i++){
             if(products.get(i).getId()==id){
                 break;
             }
        } 
        if(i!=products.size()){
        System.out.println(products.get(i).getId());
                 products.remove(i);
                 System.out.println("true");
                 return true;
        }  
        else{
        System.out.println("false");
        return false;
        }
        
   }*/

    int size() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
 
}
