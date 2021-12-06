import java.util.ArrayList;

public class ComputingDiagnostics {
  public char findMostCommon(String binary) {
    int zeroCount = 0;
    char[] binarySplit = binary.toCharArray();

    for (char number : binarySplit) {
      if (number == '0') {
        zeroCount++;
      }

      if (zeroCount > binarySplit.length/2){
        return '0';
      }
    }

    return '1';
  }

  public char findLeastCommon(String binary) {
    int zeroCount = 0;
    char[] binarySplit = binary.toCharArray();

    for (char number : binarySplit) {
      if (number == '0') {
        zeroCount++;
      }

      if (zeroCount > binarySplit.length/2){
        return '1';
      }
    }

    if (zeroCount == binarySplit.length/2) {
      return '0';
    }

    return '0';
  }

  public String findOxygenRate(ArrayList<String> puzzleInput) {
    ReaderAndParse rp = new ReaderAndParse();
    String oxygenRate = new String();
    char mostCommon = '0';
    ArrayList<String> filteredInput = puzzleInput;

    for (int i = 0; i < puzzleInput.get(0).length(); i++) {
      if (filteredInput.size() == 1) {
        oxygenRate = filteredInput.get(0);
        break;
      }

      if (i == 0) {
        ArrayList<String> inputSplitByPosition = rp.splitByPosition(filteredInput);
        mostCommon = findMostCommon(inputSplitByPosition.get(i));
        oxygenRate = oxygenRate + mostCommon;
      } else {
        filteredInput = rp.filterInput(filteredInput, mostCommon, i - 1);
        ArrayList<String> inputSplitByPosition = rp.splitByPosition(filteredInput);
        mostCommon = findMostCommon(inputSplitByPosition.get(i));
        oxygenRate = oxygenRate + mostCommon;
      }
    }
    return oxygenRate;
  }

  public String findCO2Scrubber(ArrayList<String> puzzleInput) {
    ReaderAndParse rp = new ReaderAndParse();
    String co2Scrubber = new String();
    char leastCommon = '0';
    ArrayList<String> filteredInput = puzzleInput;

    for (int i = 0; i < puzzleInput.get(0).length(); i++) {
      if (filteredInput.size() == 1) {
        co2Scrubber = filteredInput.get(0);
        break;
      }

      if (i == 0) {
        ArrayList<String> inputSplitByPosition = rp.splitByPosition(filteredInput);
        leastCommon = findLeastCommon(inputSplitByPosition.get(i));
        co2Scrubber = co2Scrubber + leastCommon;
      } else {
        filteredInput = rp.filterInput(filteredInput, leastCommon, i - 1);
        ArrayList<String> inputSplitByPosition = rp.splitByPosition(filteredInput);
        leastCommon = findLeastCommon(inputSplitByPosition.get(i));
        co2Scrubber = co2Scrubber + leastCommon;
      }
    }

    return co2Scrubber;
  }
}