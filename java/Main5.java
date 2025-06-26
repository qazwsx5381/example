public class Main5 {
    static int[] MakeArray(){
   
    int[] tempArr = new int[4];
    
    for(int i=0; i<tempArr.Length;i++){
      tempArr[i] = i;
    }
    
    return tempArr;
    }
    
    public static void main5(String[] args){
    
    int[] intArr;
    intArr = MakeArray();
    
    for(int i=0; i < intArr.Length; i++)
    System.out.print(intArr[i]);
   
    }
  }