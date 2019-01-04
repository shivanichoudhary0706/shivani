package country;

import java.util.*;

public class CountryState {
    public static void main(String args[]){
       /* HashMap<String,HashMap<String,HashMap<Integer,String>>> c=new HashMap<>();
        //add country
        c.put("India",new HashMap<>());
        c.put("Japan",new HashMap<>());
        //add State
        c.get("India").put("Gujarat",new HashMap<>());
        c.get("India").put("Bihar",new HashMap<>());
        c.get("Japan").put("Tokoyo",new HashMap<>());
        //add city
        c.get("India").get("Gujarat").put(384002,"Mahesana");
        c.get("India").get("Gujarat").put(123456,"Ahemdabad");
        c.get("India").get("Bihar").put(456987,"Darbhanga");
        c.get("India").get("Bihar").put(145632,"Madhubani");
        c.get("Japan").get("Tokoyo").put(456321,"jijang");
        for(String country:c.keySet()){
            System.out.println(country);
            for(String state:c.get(country).keySet()){
                System.out.println("\t\t"+state);
                for(Integer pincode:c.get(country).get(state).keySet()){
                    System.out.println("\t\t\t"+pincode+" "+c.get(country).get(state).get(pincode));
                }
            }
        }*/
      // public static void main(String[] args) {
        HashMap<String,HashMap<String,HashMap<Integer,String>>> c = new HashMap<>();

        c.put("India",new HashMap<>());
        c.put("U.S",new HashMap<>());

        c.get("India").put("Gujarat",new HashMap<>());
        c.get("India").put("Maharashtra",new HashMap<>());
        c.get("U.S").put("California",new HashMap<>());
        c.get("U.S").put("New York",new HashMap<>());

        c.get("India").get("Gujarat").put(384265,"Patan");
        c.get("India").get("Gujarat").put(384315,"Mahesana");
        c.get("India").get("Maharashtra").put(400003,"Mumbai");
        c.get("India").get("Maharashtra").put(422003,"Nashik");
        c.get("U.S").get("California").put(92083,"Vista");
        c.get("U.S").get("California").put(90291,"Venice");
        c.get("U.S").get("New York").put(10504,"Armonk");
        c.get("U.S").get("New York").put(10467,"Bronx");

        for(String country : c.keySet()) {
            System.out.println(country);
            for (String state : c.get(country).keySet()) {
                System.out.println("\t\t"+state);
                for(Integer pincode : c.get(country).get(state).keySet()) {
                    System.out.print("\t\t\t\t"+pincode+"  "+c.get(country).get(state).get(pincode)+"\n");
                }
            }
        }
    }
}
