package app;

public class App {
     public static void main(String []args){
        java.util.ArrayList<Product> products=new java.util.ArrayList<>(); 
        ProductRepository product=new ProductRepository();
       //add
        products.add(new Product(01,"natraj hb","pencil",5.6,true));
        products.add(new Product(101,"classmate","notebook",30,true));
        products.add(new Product(12,"goldex","pen",5,true));
        products.add(new Product(13,"camel","pencil",6,false));
        products.add(new Product(1,"camel","geometry box",5.6,false));
        
       //print
       int i;
        for( i=0;i<products.size();i++){
        System.out.println(i+1);
        System.out.println("Id: "+products.get(i).getId()+"\nCategory: "+products.get(i).getCategory()+"\nPrice: "+products.get(i).getPrice()+"\nAvailable: "+products.get(i).isAvailable()+"\n");
        }
        for( i=0;i<products.size();i++){
             String str="geometry box";
             if(products.get(i).getCategory().equals(str)){
                 System.out.println(str+" found at "+(i+1));
             }
            /* if(i==products.size()){
                 System.out.println(str+" not found");
             }*/
             int id=10;
             if(products.get(i).getId()==id){
                System.out.println(id+" found at "+(i+1));
             }
             /*if(i==products.size()-1){
                System.out.println(id+" not found");
             }*/
             str="goldex";
             if(products.get(i).getName().equals(str)){
                System.out.println(str+" found at "+(i+1));
             }
            /* if(i==products.size()-1){
                System.out.println(str+" not found");
             }*/
             double d=5;
             if(products.get(i).getPrice()==d){
                System.out.println(d+" found at "+(i+1)+"\n");
             }
             /*if(i==products.size()-1){
                System.out.println(d+" not found\n");
             }*/
        }
        if(i==products.size()){
                 System.out.println(" not found");
             }
        //products.remove(0);
       /* if(product.removeById(10)){
            System.out.println("deleted");
        }
        System.out.println("not forund");*/
       System.out.println("\n\nsize of array:"+products.size());
        //print
        for(i=0;i<products.size();i++){
        System.out.println((i+1));
        System.out.println("Id: "+products.get(i).getId()+"\nCategory: "+products.get(i).getCategory()+"\nPrice: "+products.get(i).getPrice()+"\nAvailable: "+products.get(i).isAvailable()+"\n");
        }
       products.sort((p,q)->p.getName().compareTo(q.getName()));
       System.out.println("\n sort by name");
        for(i=0;i<products.size();i++){
        System.out.println((i+1));
        System.out.println("Id: "+products.get(i).getId()+" Name:"+products.get(i).getName()+" Category: "+products.get(i).getCategory()+" Price: "+products.get(i).getPrice()+" Available: "+products.get(i).isAvailable()+"\n");
        }
         products.sort((p,q)->{
             if(p.getPrice()==q.getPrice())
             return 0;
             if(p.getPrice()>q.getPrice())
                 return 1;
             return -1;
         });
         System.out.println("\n sort by price");
        for(i=0;i<products.size();i++){
        System.out.println((i+1));
        System.out.println("Id: "+products.get(i).getId()+" Name:"+products.get(i).getName()+" Category: "+products.get(i).getCategory()+" Price: "+products.get(i).getPrice()+" Available: "+products.get(i).isAvailable()+"\n");
        }
        System.out.println("\n sort by Id");
        products.sort((p,q)->p.getId()-q.getId());
         for(i=0;i<products.size();i++){
        System.out.println((i+1));
        System.out.println("Id: "+products.get(i).getId()+" Name:"+products.get(i).getName()+" Category: "+products.get(i).getCategory()+" Price: "+products.get(i).getPrice()+" Available: "+products.get(i).isAvailable()+"\n");
        }
         
     }
     
}
