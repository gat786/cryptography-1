//VernamCipher.java - cipher based on random pad
import java.io.*;
import java.util.*;   //random number methods
import tio.*;

class VernamCipher{

  public static void main(String[] args)
    throws IOException
  {
    if (args.length < 2) {
      System.out.println("Usage: " +
          "java VernamCipher clearFile codeFile");
      System.exit(1);
    }
    ReadInput in = new ReadInput(args[0]);
    PrintWriter out = 
      new PrintWriter(new FileWriter(args[1]));
    Random r = new Random(7);

    while (in.hasMoreElements()){
      out.println(encrypt(in.readLine(), r));
    }
    out.close();
  }
  public static String encrypt(String message,
                               Random r)
  {
    System.out.println(message);
    char c;
    StringBuffer cipher = 
                   new StringBuffer(message.length());
    for (int i = 0; i < message.length(); i++){
      c = message.charAt(i);
      if (Character.isLetter(c))
        cipher.append( (char)
           ((Character.toUpperCase(c) - 'A' +
            (int)(r.nextDouble() * 26)) % 26 + 'A'));
      else
        cipher.append(c);
  }
    System.out.println(cipher.toString());
    return cipher.toString();
  }
}