import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

public class Day1{
  public static void main(String[] args) {
    Day1 day1 = new Day1();
    File puzzleInput = new File("PuzzleInput.txt");
    ArrayList<Integer> puzzleArray = day1.putInIntArrayList(puzzleInput);
    int partOne = day1.partOne(puzzleArray);
    int partTwo = day1.partTwo(puzzleArray);

    System.out.println("The answer to part 1 is " + partOne);
    System.out.println("The answer to part 2 is " + partTwo);
  }

  private int partOne(ArrayList<Integer> puzzleArray) {
    int increase = 0;

    for (int i = 1; i < puzzleArray.size(); i++) {
      if (puzzleArray.get(i) > puzzleArray.get(i - 1))
        increase++;
    }

    return increase;
  }

  private int partTwo(ArrayList<Integer> puzzleArray) {
    int increase = 0;
    int previousDepth = puzzleArray.get(0) + puzzleArray.get(1) + puzzleArray.get(2);

    for (int i = 1; i < puzzleArray.size()-2; i++) {
      int newDepth = puzzleArray.get(i) + puzzleArray.get(i + 1) + puzzleArray.get(i +2);
      if (newDepth > previousDepth) {
        increase++;
      }
      previousDepth = newDepth;
    }

    return increase;
  }

  private ArrayList<Integer> putInIntArrayList(File puzzleInput) {
    ArrayList<Integer> input = new ArrayList<Integer>();
    try {
      Scanner sc = new Scanner(puzzleInput);

      while (sc.hasNextLine()) {
        input.add(Integer.valueOf(sc.nextLine().replace("\n", "")));
      }
    } catch (Exception e) { }

    return input;
  }
}