class Parent{
  void show(){System.out.println("parent");}  
}
class Child extends Parent{
  void show() {System.out.println("child");}
}
 
class Main {  
  public static void main(String args[]) { 
    // Parent pa=(가) Child();
    Parent pa=new Child();
    pa.show();
  } 
}
// 한번 더 분석해보기
