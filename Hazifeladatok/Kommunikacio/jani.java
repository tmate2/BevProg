import java.util.Scanner;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.io.FileWriter;

public class jani{
    public static void main(String[] args) throws IOException{
        
        RandomAccessFile f = new RandomAccessFile("chatroom.txt", "r");
        
        for(String s = f.readLine(); s!=null; s = f.readLine())
            System.out.println(s+"\n");

        f.close();

        Scanner sc = new Scanner(System.in);
        System.out.print("jani> ");
        String message = sc.nextLine();

        FileWriter wf = new FileWriter("chatroom.txt",true);
        wf.write("<jani> "+message+"\n");
        wf.close();
    }
}