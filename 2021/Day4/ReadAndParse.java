import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ReadAndParse {
  public ArrayList<Boards> setUpBoards(File boards) {
    ArrayList<Boards> allBoards = new ArrayList<Boards>();

    try {
      Scanner sc = new Scanner(boards);
      Integer count = 0;

      while (sc.hasNextLine()) {
        if (count <= 4) {
          Boards board = new Boards();

          while (count <= 4 ) {
            List<String> line = Arrays.asList(sc.nextLine().split(" "));

            if (line.size() > 0 ) {
              board.setBoard(line);
              count++;
            }
          }

          allBoards.add(board);
          sc.nextLine();
          count = 0;
        }
      }
    } catch (Exception e) {
      System.out.println("There is no file for setUpBoards.");
    }

    return allBoards;
  }

  public ArrayList<String> drawNumbers(File numbersInput){
    ArrayList<String> numbers = new ArrayList<String>();

    try {
      Scanner sc = new Scanner(numbersInput);
      String[] numbersSplit = sc.nextLine().split(",");

      for (String number : numbersSplit) {
        numbers.add(number);
      }
    } catch (Exception e) {
      System.out.println("There is no file for drawNumbers.");
    }

    return numbers;
  }
}