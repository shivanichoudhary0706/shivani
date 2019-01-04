package invoice;

import java.util.ArrayList;
import java.util.Scanner;
public class main {
     public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        do{
            System.out.print("enter name of customer : ");
            String cName=sc.nextLine();
            System.out.println("enter customer address :");
            String cAdd=sc.nextLine();
            Customer cust= new Customer(cName,cAdd);
            Display.display(cust);
            System.out.println("do you want to enter more customer :y or n");
        }while(!sc.nextLine().equals("n"));    
    }
}
