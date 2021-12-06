import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;

public class ReaderAndParse {
  public ArrayList<String> readPuzzleInput(File puzzleInput) {
    ArrayList<String> inputAsArray = new ArrayList<String>();

    try {
      Scanner sc = new Scanner(puzzleInput);
      while (sc.hasNextLine()) {
        inputAsArray.add(sc.nextLine());
      }
    } catch (Exception e) {
      System.out.println("There is no file.");
    }


    return inputAsArray;
  }

  public ArrayList<String> splitByPosition(ArrayList<String> puzzleInput) {
    ArrayList<String> inputByPosition = new ArrayList<String>();
    int count = 0;

    while(count < puzzleInput.size()) {
      char[] binarySplit = puzzleInput.get(count).toCharArray();

      for (int i = 0; i < binarySplit.length; i++) {
        if (count == 0) {
          inputByPosition.add(String.valueOf(binarySplit[i]));
        } else {
          inputByPosition.set(i, inputByPosition.get(i) + binarySplit[i]);
        }
      }
      count++;
    }

    return inputByPosition;
  }

  public ArrayList<String> filterInput(ArrayList<String> inputToBeFiltered, char numberToCheckAgainst, int position) {
    ArrayList<String> filteredInput = new ArrayList<String>();

    for (int i = 0; i < inputToBeFiltered.size(); i++) {
      char[] binarySplit = inputToBeFiltered.get(i).toCharArray();

      if (binarySplit[position] == numberToCheckAgainst) {
        filteredInput.add(inputToBeFiltered.get(i));
      }
    }

    return  filteredInput;
  }

}