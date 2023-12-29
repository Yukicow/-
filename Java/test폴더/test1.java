import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.*;

import javax.swing.event.SwingPropertyChangeSupport;


public class test1{


    public static void main(String[] arg){

        interface MyFunction { 

            int calc(int x, int y);
            
            }

        MyFunction myf = (int x, int y) -> {return 0;};

        System.out.println(myf.calc(1, 2));
        }
}