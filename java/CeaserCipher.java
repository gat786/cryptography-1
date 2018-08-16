public class CeaserCipher
{
    public static StringBuffer encrypt(String string, int shift)
    {
        StringBuffer result = new StringBuffer();
        for(int i=0;i<string.length();i++)
        {
            char character = string.charAt(i); 
            if(Character.isUpperCase(character))
            {
                result.append((char)(((int) character + shift - 65) % 26 + 65));
            }
            else
            {
                result.append((char)(((int) character + shift - 97) % 26 + 97));
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
                result.append((char)(((int) character - shift + 65) % 26 + 65));
            }
            else
            {
                result.append((char)(((int) character - shift - 97) % 26 + 97));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        CeaserCipher ceasercipher = new CeaserCipher();
        String encryptedText = ceasercipher.encrypt("HelloWorldxyz",4).toString();
        String decryptedText = ceasercipher.decrypt(encryptedText, 4).toString();
        System.out.println("Encrypted Text: " + encryptedText);
        System.out.println("Decrypted Text: " + decryptedText);
        System.out.println(ceasercipher.decrypt(ceasercipher.encrypt("WWww",4).toString(),4).toString());
    }
}