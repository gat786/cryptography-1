public class CeaserCipherTrial
{
    public static StringBuffer encrypt(String string, int shift)
    {
        StringBuffer result = new StringBuffer();
        for(int i=0;i<string.length();i++)
        {
            char character = string.charAt(i); 
            if(Character.isUpperCase(character))
            {
                result.append((char)((((int) character) + shift )));
            }
            else
            {
                result.append((char)((((int) character) + shift )));
            }
        }
        return result;
    }

    public static StringBuffer decrypt(String string, int shift)
    {
        StringBuffer result = new StringBuffer();
        for(int i=0;i<string.length();i++)
        {
            char character = string.charAt(i);
            if(Character.isUpperCase(character))
            {
                result.append((char)((((int) character) - shift )));
            }
            else
            {
                result.append((char)((((int) character) - shift )));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        CeaserCipher ceasercipher = new CeaserCipher();
        String encryptedText = ceasercipher.encrypt("Hello pqrstuvwxyz",4).toString();
        String decryptedText = ceasercipher.decrypt(encryptedText, 4).toString();

        
        String encryptedText1 = ceasercipher.encrypt("Hello PQRSTUVWXYZ",4).toString();
        String decryptedText1 = ceasercipher.decrypt(encryptedText, 4).toString();

        System.out.println("Encrypted Text: " + encryptedText);
        System.out.println("Decrypted Text: " + decryptedText);

        
        System.out.println("Encrypted Text: " + encryptedText1);
        System.out.println("Decrypted Text: " + decryptedText1);
        //System.out.println(ceasercipher.decrypt(ceasercipher.encrypt("WWww",4).toString(),4).toString());
    }
}