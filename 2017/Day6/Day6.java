//import java.util.HashMap;
//import java.util.HashSet;
//import java.util.Map;
//import java.util.Map.Entry;
//import java.util.Set;
//
//
//public class Day6 {
//  //do things here
//  int puzzleInput[] = new int[] {10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6};
//
//  public static void main (int[] puzzleInput) {
//    int database[] = new int []{puzzleInput};
//    Set<puzzleInput> seenVariations = new HashSet<>();
//    int count = 0;
//
//    while (seenVariations.add(database) == true) {
//      int redistribution[] = redistribute(database);
//      seenVariations.add(redistribution);
//      count += 1;
//      database = redistribution;
//    };
//
//    System.out.print(count);
//  };
//
//  private static int[] redistribute(int database) {
//    int startingPoint = findStartingPoint(database);
//    int blocksToBeDistributed = database[startingPoint];
//
//    database[startingPoint] = 0;
//
//    while (blocksToBeDistributed != 0) {
//      for (let i = startingPoint + 1; i < database.length; i++){
//        database[i] += 1;
//        blocksToBeDistributed -= 1;
//        if (i == database.length - 1) {
//          i = 0;
//        };
//      };
//    };
//
//    return new int[] {database};
//  };
//
//  private static int findStartingPoint (int[] database) {
//    int startingPoint = 0;
//
//    int max = database[0];
//
//    for (let i = 1; i < database.length; i++){
//      if (database[i] > max) {
//        startingPoint = 0;
//        max = database[i];
//      }
//    };
//
//    return startingPoint;
//  };
//};
