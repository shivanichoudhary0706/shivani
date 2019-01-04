package product;

import product.ProductRepository;
import product.Product;

public class main {
    public static void main(String args[]){
        ProductRepository pr = new ProductRepository();

        pr.add1(new Product(1,"Pencil","Nataraj HB 6",true,5.6,10.5));
        pr.add1(new Product(2,"notebook","classmate",false,30,15.00));
        pr.add1(new Product(3,"pen","goldex",true,10,20.34));
        pr.add1(new Product(4,"pencil","camel",true,5,17.04));

        for(Product p : pr.getProducts())
            System.out.println(p.getId()+"  "+p.getName()+"  "+p.getUnit()+" "+p.getRate()+" "+p.getDiscount());

        pr.removeId(10);
        System.out.println(pr.removeId(1));
       // pr.getId(20).setRate(4.5);

       /* pr.get(20).setUnit("KG");*/
       /* for(Product p : pr.getProducts()) {
            System.out.println(p.getId()+"  "+p.getName()+"  "+p.getUnit()+" "+p.getRate()+" "+p.getDiscount());
        }*/


    }
    
}
