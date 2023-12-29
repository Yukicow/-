public class Example{

    private String example_variable;

    public static Example ex1 = new Example();
    public static Example ex2 = new Example();
    public static Example ex3 = new Example();
    public static void main(String[] arg) throws Exception{


    
            new Thread(() -> {
                for(int i = 0; i < 100; i++){
                    ex1.example_method2("thread1");
                    }}).start();

            new Thread(() -> {
                for(int i = 0; i < 100; i++){ 
                    ex2.example_method1("thread2");
                    }}).start();

            // new Thread(() -> {
            //     for(int i = 0; i < 100; i++){ 
            //         ex1.example_method3("thread2");
            //         }}).start();
        
    }

    public void example_method1(String thread_name) {


        synchronized(ex2){
            example_variable = thread_name;
        try {
            Thread.sleep(500);
        } catch (Exception e) {
            System.out.println("오류");
        }
    

        if(!example_variable.equals(thread_name)){System.out.println("중간에 값이 바뀜.");}
        System.out.println("ex 1 잘 작동 중");
    }
    }

    public void example_method2(String thread_name) {

        // example_variable = thread_name;
        synchronized(ex2){
            example_variable = thread_name;
        try {
            Thread.sleep(500);
        } catch (Exception e) {
            System.out.println("오류");
        }

        if(!example_variable.equals(thread_name)){System.out.println("중간에 값이 바뀜.");}
        System.out.println("ex 2 잘 작동 중");
    }
}


public void example_method3(String thread_name) {


    synchronized(Example.class){
        example_variable = thread_name;
    try {
        Thread.sleep(500);
    } catch (Exception e) {
        System.out.println("오류");
    }


    if(!example_variable.equals(thread_name)){System.out.println("중간에 값이 바뀜.");}
    System.out.println("ex 3 잘 작동 중");
}
}
}