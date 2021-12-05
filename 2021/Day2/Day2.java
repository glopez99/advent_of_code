import java.io.File;
import java.util.Scanner;

public class Day2 {
  public static void main(String[] args) {
    Day2 day2 = new Day2();
    File puzzleInput = new File("PuzzleInput.txt");
    int partOneAnswer = day2.partOne(puzzleInput);
    int partTwoAnswer = day2.partTwo(puzzleInput);

    System.out.println("The answer to part one is " + partOneAnswer);
    System.out.println("The answer to part two is " + partTwoAnswer);
  }

  public int partTwo(File directions) {
    int horizontal = 0;
    int depth = 0;
    int aim = 0;

    try {
      Scanner sc = new Scanner(directions);

      while (sc.hasNextLine()) {
        String[] splitLine = sc.nextLine().split(" ", -1);
        String direction = splitLine[0];
        int distance = Integer.valueOf(splitLine[1]);

        if (direction.contains("up")) {
          aim -= distance;
        } else if (direction.contains("down")) {
          aim += distance;
        } else {
          horizontal += distance;
          depth += (aim * distance);
        }
      }
    } catch (Exception e) {
      System.out.println("There is no file.");
    }

    return horizontal * depth;
  }

  public int partOne(File directions) {
    int horizontal = 0;
    int depth = 0;

    try {
      Scanner sc = new Scanner(directions);

      while (sc.hasNextLine()) {
        String[] splitLine = sc.nextLine().split(" ", -1);
        String direction = splitLine[0];
        int distance = Integer.valueOf(splitLine[1]);

         if (direction.contains("forward")) {
           horizontal += distance;
         } else if (direction.contains("up")) {
           depth -= distance;
         } else {
           depth += distance;
         }
      }
    } catch (Exception e) {
      System.out.println("there was no file");
    }

    return horizontal * depth;
  }
}