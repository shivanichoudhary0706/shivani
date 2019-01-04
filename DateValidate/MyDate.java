package DateValidate;
import java.util.Scanner;
public class MyDate {
    static int maxDay(int m,int y){
        MyDate md=new MyDate();
            if(m==2){
                if(md.leapYear(y))
                    return 29;
                else
                    return 28;
            }
           
          // int check= m==2&&md.leapYear(y)?29:28;
int check= m<=7 && m%2!=0 || 7<m && m<=12 && m%2==0?31:30;
               /* if(m<=7&& m%2!=0 ||7<m && m<=12 && m%2==0)
                    return 31;
                if(m<=7 && m%2==0||7<m && m<=12 && m%2>0 )
                    return 30;*/
   /* int check;
    check=m<=7 && m%2!=0 || 7<m && m<=12 && m%2==0?31:30;*/
            return(check);
    }
    static boolean isValid(int d,int m,int y){
        MyDate md=new MyDate();
        int no=md.maxDay(m,y);
       boolean isvalid= no>=d?true:false;
       return isvalid;
    }
    
    static boolean leapYear(int y){
       boolean leapyear=y%4==0?true:false;
            return (leapyear);
    }
    static int yourAge(int d,int m,int y){
        MyDate md=new MyDate();
        int yourage;
          if(md.isValid(d,m,y)){
              Scanner s2=new Scanner(System.in);
              System.out.print("enter yor birthyear:-");
              int y2=s2.nextInt();
              yourage= y> y2 ?(y-y2):(y2-y);
             /* if(y>y2)
                return(y-y2);
              else
               return(y2-y);*/
          return yourage;
          }
          return 0;
}
}

class Test{
    public static void main(String [] args){
        Scanner s=new Scanner(System.in);
        System.out.println("enter date:-");
        int d=s.nextInt();
        System.out.println("enter month:-");
        int m=s.nextInt();
        System.out.println("enter year:-");
        int y=s.nextInt();
        boolean n=MyDate.isValid(d,m,y);
        System.out.println("max day in "+m +" month:-"+MyDate.maxDay(m,y));
        System.out.println("is date valid:-"+n);
        System.out.println("year is a leap year:-"+MyDate.leapYear(y));
        System.out.println("age="+MyDate.yourAge(d,m,y));
       /* int max= d>m && y>m ?d:m;
        System.out.println("max="+max);*/
    }
        
}
