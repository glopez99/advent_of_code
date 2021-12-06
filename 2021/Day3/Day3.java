import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

public class Day3 {
  public static void main (String[] args) {
    Day3 day3 = new Day3();
    ReaderAndParse rp = new ReaderAndParse();

    File puzzleInput = new File("PuzzleInput.txt");
    ArrayList<String> inputAsArray = rp.readPuzzleInput(puzzleInput);

    Integer partOne = day3.partOneAnswer(inputAsArray);
    Integer partTwo = day3.partTwoAnswer(inputAsArray);

    System.out.println("The answer to part one is " + partOne);
    System.out.println("The answer to part two is " + partTwo);
  }

  private Integer partOneAnswer(ArrayList<String> inputAsArray) {
    ReaderAndParse rp = new ReaderAndParse();
    ComputingDiagnostics compute = new ComputingDiagnostics();

    String gammaRate = new String();
    String epsilonRate = new String();
    ArrayList<String> inputSplitByPosition = rp.splitByPosition(inputAsArray);

    for (String binary : inputSplitByPosition) {
      char mostCommon = compute.findMostCommon(binary);
      char leastCommon;

      if (mostCommon == '0') {
        leastCommon = '1';
      } else {
        leastCommon = '0';
      }
      gammaRate = gammaRate + mostCommon;
      epsilonRate = epsilonRate + leastCommon;
    }

    return Integer.parseInt(gammaRate, 2) * Integer.parseInt(epsilonRate, 2);
  }

  private Integer partTwoAnswer(ArrayList<String> puzzleInput) {
    ComputingDiagnostics compute = new ComputingDiagnostics();

    String oxygenRate = compute.findOxygenRate(puzzleInput);
    String co2Scrubber = compute.findCO2Scrubber(puzzleInput);

    return Integer.parseInt(oxygenRate, 2) * Integer.parseInt(co2Scrubber, 2);

  }
}