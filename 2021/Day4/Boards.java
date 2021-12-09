import java.util.HashSet;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Boards {
  private ArrayList<ArrayList<String>> board = new ArrayList<ArrayList<String>>();
  private boolean winner = false;

  public void setBoard(List<String> input) {
    ArrayList<String> line = new ArrayList<String>();

    for (String number : input) {
      if (number.isEmpty()) {
        continue;
      }

      line.add(number);
    }

    board.add(line);
  }

  public ArrayList<ArrayList<String>> getBoard() {return board;}

  public void checkForCalledNumber(String calledNumber) {
    for (ArrayList<String> line : board) {
      if (line.contains(calledNumber)) {
        line.set(line.indexOf(calledNumber),"x");

        if (horizontalWin(line) || veritcalWin()) {
          winner = true;
        }

        break;
      }
    }
  }

  public boolean checkForWinner() {
    return winner;
  }

  public Integer sumRemainingNumbers() {
    Integer sumOfRemaining = 0;

    for (ArrayList<String> line : board) {
      for (String number : line) {
        if (number.equals("x")) {
          continue;
        }
        sumOfRemaining += Integer.valueOf(number);
      }
    }

    return sumOfRemaining;
  }

  private boolean horizontalWin(ArrayList<String> line) {
    Integer count = 0;
    for (String number : line) {
      if (number.equals("x"))
        count += 1;
    }

    if (count == 5) {
      return true;
    }

    return false;
  }

  private boolean veritcalWin(){
    HashSet<Integer> positionsOfCalled = new HashSet<Integer>();
    Integer count = 0;

    for (ArrayList<String> line : board) {
      HashSet<Integer> linePositions = new HashSet<Integer>();

      if (line.contains("x")){
        count ++;
        for (String number : line) {
          if (number.equals("x")) {
            linePositions.add(line.indexOf(number));
          }
        }

        if (positionsOfCalled.isEmpty() && count == 1){
          positionsOfCalled = linePositions;
        } else if (positionsOfCalled.isEmpty() && count < 1) {
          return false;
        } else {
          positionsOfCalled.retainAll(linePositions);
        }
      }
    }

    if (positionsOfCalled.isEmpty()) {
      return false;
    }

    if (count < 5) {
      return false;
    }

    return true;
  }
}