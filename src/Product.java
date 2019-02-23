import java.util.HashSet;
import java.util.Objects;
import java.util.Scanner;

public class Product {
    private int productId;
    private String name;
    private int quantity;
    private double rate;
    private String unit;
    private double totalPerProduct = 0.0;

    public Product(){
        this.productId=productId;
        this.name = name;
        this.quantity = quantity;
        this.rate = rate;
        this.unit = unit;
        this.totalPerProduct = rate * quantity;
    }
    public Product(int productId,String name, int quantity, double rate, String unit) {
        this.productId=productId;
        this.name = name;
        this.quantity = quantity;
        this.rate = rate;
        this.unit = unit;
        this.totalPerProduct = rate * quantity;
    }

    public String getName() {
        return name;
    }

    public int getProductId() {
        return productId;
    }

    public void setProductId(int productId) {
        this.productId = productId;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getRate() {
        return rate;
    }

    public void setRate(double rate) { ;
        this.rate = rate;
    }

    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public double getTotalPerProduct() {
        return totalPerProduct;
    }

    public void setTotalPerProduct(double totalPerProduct) {
        this.totalPerProduct = totalPerProduct;
    }


    @Override
    public int hashCode() {
        int hash = 7;
        hash = 13 * hash + Objects.hashCode(this.productId);
        hash = 13 * hash + (int) (Double.doubleToLongBits(this.rate) ^ (Double.doubleToLongBits(this.rate) >>> 32));
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Product other = (Product) obj;
        if (this.productId != other.productId) {
            return false;
        }
        if (Double.doubleToLongBits(this.rate) != Double.doubleToLongBits(other.rate)) {
            return false;
        }
        return true;
    }

}
