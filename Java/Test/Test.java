public class Test {
    public static void main(String[] args) {
        double randDouble = Math.floor(Math.random() * 2) + 1;
        
        if (randDouble == 2) {
            System.out.println("Error, you've got JACKED!!!");
        } else {
            System.out.println("You're safe, for now...");
        }
        
        String myString = "Josue";
        double score = (Math.floor(Math.random() * (2 - 1))); // Excluded the + 1 at the end to get 0 in range
        System.out.println(score);
        if (score == 0 && myString.equals("Josue")) {
            System.out.println("You're score is zero!");
            System.out.println("Oddly enough, that means you win!");
            System.out.println("You're score is " + score);
        } else {
            System.out.println("You're score is NOT zero...");
            System.out.println("That means you actually lose!");
        }

    }
}
