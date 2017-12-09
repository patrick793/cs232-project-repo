public class TweetsVersusActual
{
   public static void main(String[] args) 
   {
       String electoralVotes ="rrrrdddddrrdrdrrrrrdddrdrrrrdddddrrrrdrdrrrrrdddrrr"; // moved DC from position 26 to position 9
       String twitcountVotes ="rrrrrrrrrrrrrrrrrrdrrrrrdrdrrrrdrrrrrrrrrdrrrdrrrrd";
       String twitcountVotesNotUU ="rrrrdrrrrrrrrrrrdrdrrdrrdrdrdrrdrrrrrrrrrrrrrdrdrrd";
       
       
       int diff = 0;
       for (int i = 0; i < twitcountVotes.length(); i++)
       {
           if (electoralVotes.substring(i, i+1).equals(twitcountVotes.substring(i, i+1)))
           diff ++;
        
       }
       
       System.out.println(diff + " out of " + electoralVotes.length());
       
       /////////////////////////////////
       // california had 50:50 won by 90 count margin
       // 7145 vs 7054
       // connecticut 50:50 won by 7 count margin 
       // 446 vs 439
       // maryland 50:50
       // 738 vs 734
       // massacusets 50:50 won by 6 count
       // 1364 vs 1359
       // vermont won by 1 count 
       // 54 vs 55
       ////////////////////////////////
       
       //String dizzy = "testtest";
       //String elphelt = "testicle";
       // should output = 4 out of perfect 8
   }
}
