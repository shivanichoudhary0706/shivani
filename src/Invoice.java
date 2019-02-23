import java.util.ArrayList;
import java.util.HashSet;
import java.util.Date;
import java.util.Scanner;

public class Invoice {
    private static int billNo=0;
    private Date billDate;
    private Customer customer;
    private HashSet<Product> products;
    private double netAmount = 0.0;

    //Construct

    public Invoice() {
        this.products = new HashSet<>();
    }
    public Invoice(Date billDate, Customer customer, HashSet<Product> products) {
        this.billDate = billDate;
        this.customer = customer;
        this.products = products;
    }
    public Invoice(int billNo,Date billDate, Customer customer, HashSet<Product> products, double netAmount) {
        Invoice.billNo=billNo+1;
        this.billDate = billDate;
        this.customer = customer;
        this.products = products;
        this.netAmount = netAmount;
    }

    public int getBillNo() {
        return billNo;
    }

    public void setBillNo(int billNo) {
        Invoice.billNo=billNo;
    }

    public Date getBillDate() {
        return billDate;
    }

    public void setBillDate(Date billDate) {
        this.billDate = billDate;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

    public HashSet<Product> getProducts() {
        return products;
    }

    public void setProducts(HashSet<Product> products) {

        this.products = products;
    }

    public double getNetAmount() {
        return netAmount;
    }

    public void setNetAmount(double netAmount) {
        this.netAmount = netAmount;
    }

    // Add Net Amount
    public void addNetAmount(){
        double amountTotal = 0.0;
        for(Product product : products) {
            amountTotal = amountTotal + product.getTotalPerProduct();
        }
        setNetAmount(amountTotal);
    }

    public void addProduct(Product product){
        this.products.add(product);
    }

    public boolean addSameProduct(int productId){
        for(Product product : products) {
            if(productId == product.getProductId()) {
                System.out.print("\nenter quantity :");
                int quantity=new Scanner(System.in).nextInt();
                product.setQuantity(product.getQuantity()+quantity);
                product.setTotalPerProduct(product.getRate() * product.getQuantity());
                return true;
            }
        }
        return false;
    }

}
