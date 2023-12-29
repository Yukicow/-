import java.util.*;

class CarList{

    public static final String color_Red = "레드";
    public static final String color_blue = "블루";

    public static final int lot_dis = 500;
    public static final int normal_dis = 300;
    public static final int les_dis = 100;

    public static final String normal_tire= "일반 타이어";
    public static final String luxury_tire= "고급 타이어";

    public static final String normal_handle= "일반 핸들";
    public static final String luxury_handle= "고급 핸들";
}

class Car{

    private int tax = 0;

    public String color;
    public String tire;
    public int displacement;
    public String handle;

    Car(String color, String tire, int displacement, String handle){
        this.color = color;
        this.tire = tire;
        this.displacement = displacement;
        this.handle = handle;
        GetSpec();
    }

    private int GetSpec(){
        System.out.println("색상 : " + this.color);
        System.out.println("타이어 : " + this.tire);
        System.out.println("배기량 : " + this.displacement);
        System.out.println("핸들 : " + this.handle);
        System.out.println("\n*********************\n");
        if(displacement >= 500) return tax += 1500;
        else if(displacement >= 300 && displacement < 500) return tax += 1000;
        else return tax += 500;
        
    }

    public void GetTax(){
        System.out.println("세금 : " + tax);
    }
}


public class project2 {
    
    public static void main(String[] arg){

        Car car = new Car(CarList.color_Red, CarList.luxury_tire, CarList.normal_dis, CarList.luxury_handle);
        
        car.GetTax();

    }
}
