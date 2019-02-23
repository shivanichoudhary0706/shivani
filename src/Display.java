import java.util.HashSet;
import java.util.Date;
import java.util.Scanner;
public class Display {
    public static void display(Customer cust){
        Invoice inv = new Invoice();
        System.out.println("-----enter products-----");
        int serialNo = 1;
        double total=0;
        HashSet<Product> product=new HashSet<>();
        do {
            Product pro = new Product();
            System.out.print("\nenter product Id :");
            int pId = new Scanner(System.in).nextInt();
            if(!inv.addSameProduct(pId)) {
                pro.setProductId(pId);
                System.out.print("\nenter product name :");
                pro.setName(new Scanner(System.in).nextLine());
                System.out.print("\nenter quantity :");
                pro.setQuantity(new Scanner(System.in).nextInt());
                System.out.print("\nenter price :");
                pro.setRate(new Scanner(System.in).nextDouble());
                System.out.print("\nenter unit :");
                pro.setUnit(new Scanner(System.in).nextLine());
                inv.addProduct(pro);// pUnit));
                pro.setTotalPerProduct(pro.getRate() * pro.getQuantity());
            }
            System.out.println("do you want to enter more: y or n");
        }while(!new Scanner(System.in).nextLine().equals("n"));
        inv.setBillDate(new Date());
        inv.setCustomer(cust);
        System.out.println("----------------------------------------");
        System.out.println("|Bill No: "+inv.getBillNo()
                +"\t\t\t\t |\n|Bill Date: "
                +inv.getBillDate()+" |\n|customer Name: "+cust.getName()
                +"\t\t\t |\n|customer address: "
                +cust.getAddress()+"\t |\n ----------------------------------------");
        System.out.println("\n Product     Qty    Price\tTotal Per Product");
        System.out.println(" ---------   -----  -------        -------------------");
        HashSet<Product> product1 = inv.getProducts();
       for(Product i:product1){
            System.out.println("\n"+serialNo+"\t"+i.getName()+"\t"+i.getQuantity()+"\t"+i.getRate()+ "\t"+i.getTotalPerProduct());
            serialNo++;
        }
        System.out.println("--------------------------------");
        inv.addNetAmount();
       System.out.println("\nTotal:              "+inv.getNetAmount()+" Rs");
    }
}