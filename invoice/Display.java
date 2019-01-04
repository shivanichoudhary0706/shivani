package invoice;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;
public class Display {
    public static void display(Customer cust){
        Scanner sc=new Scanner(System.in);
        System.out.println("-----enter products-----");
        int no=1;
        double total=0;
        ArrayList<Product> product=new ArrayList<>();
        do{
            System.out.print("\nenter product name :");
            String pName=sc.nextLine();
            
            System.out.print("\nenter quantity :");
            int pQuantity=sc.nextInt();
            System.out.print("\nenter price :");
            double pRate=sc.nextDouble();
            System.out.print("\nenter unit :");
            String pUnit=sc.nextLine();
            sc.nextLine();
            product.add(new Product(pName,pQuantity,pRate,pUnit));
            System.out.println("do you want to enter more: y or n");
           
        }while(!sc.nextLine().equals("n"));
        Date ms=new Date();
        Invoice inv = new Invoice(ms,cust,product);
        System.out.println(" ----------------------------------------");
        System.out.println("|Bill No: "+inv.getBillNo()
                +"\t\t\t\t |\n|Bill Date: "
                +inv.getBillDate()+" |\n|customer Name: "+cust.getName()
                +"\t\t\t |\n|customer address: "
                +cust.getAddress()+"\t |\n ----------------------------------------");
            System.out.println("\n Product     Qty    Price");
            System.out.println(" ---------   -----  -------");
        for(Product i:product){
            System.out.println("\n"+no+" "+i.getName()+"\n             "+i.getQuantity()+"      "+i.getRate());
            no++;
            total=total+i.getRate();
        }
        System.out.println("--------------------------------");
        System.out.println("\nTotal:              "+total+" Rs");
    }
}
