 import java.util.Scanner;
public class Countinput {
   
    public static void main(String[] args) {
        Countinput ci=new Countinput();
        String strm;
        Scanner s=new Scanner(System.in);
        System.out.print("enter line:-");
        strm=s.nextLine();
        ci.count(strm);
    }
    void count(String str){
        char c[]=str.toCharArray();
        int l=0;
        int n=0;
        int sy=0;
        int sp=0;
        for(int i=0;i<=str.length();i++){
            if(Character.isLetter(c[i])){
                l=l+1;
            }
            else if(Character.isDigit(c[i])){
                n=n+1;
            }
            else if(Character.isSpaceChar(c[i])){
                sy=sy+1;
            }
            else{
                sp=sp+1;
            }
        }
            System.out.println("letter="+l);
            System.out.println("digit="+n);
            System.out.println("symbols="+sy);
            System.out.println("letter="+sp);
        
    }    
}
