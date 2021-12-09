import java.io.File;
import java.util.ArrayList;

public class Day4 {
  public static void main(String[] args){
    Day4 day4 = new Day4();
    ReadAndParse rp = new ReadAndParse();

    File numbers = new File("PuzzleNumberInput.txt");
    File boards = new File("PuzzleBoardsInput.txt");
    ArrayList<String> drawnNumbers = rp.drawNumbers(numbers);
    ArrayList<Boards> allBoards = rp.setUpBoards(boards);

    Integer partOneAnswer = day4.partOneAnswer(drawnNumbers, allBoards);
    Integer partTwoAnswer = day4.partTwoAnswer(drawnNumbers, allBoards);
    System.out.println("The answer to part one is " + partOneAnswer);
    System.out.println("The answer to part two is " + partTwoAnswer);
  }

  private Integer partOneAnswer(ArrayList<String> drawnNumbers, ArrayList<Boards> allBoards) {
    String lastCalledNumber;

    for (String number : drawnNumbers) {
      lastCalledNumber = number;
      Integer sumOfRemaining = checkBoards(number, allBoards);

      if (sumOfRemaining > 0){
       return Integer.valueOf(lastCalledNumber) *  sumOfRemaining;
      }
    }

    return 0;
  }

  private Integer partTwoAnswer(ArrayList<String> drawnNumbers, ArrayList<Boards> allBoards) {
    String lastWinningCalledNumber = "0";
    Integer sumOfLastWinning = 0;
    ArrayList<Boards> remainingBoards = allBoards;

    for (String number : drawnNumbers) {
      Integer checkForWinner = checkBoards(number, remainingBoards);

      if (checkForWinner > 0) {
        lastWinningCalledNumber = number;
        System.out.println("last winning number: " + lastWinningCalledNumber);
        sumOfLastWinning = checkForWinner;
        System.out.println("sum of last winner: " + sumOfLastWinning);
        remainingBoards = removeWinner(remainingBoards);
        System.out.println("remaining boards: " + remainingBoards.size());
      }
    }

    return Integer.valueOf(lastWinningCalledNumber) * sumOfLastWinning;
  }

  private Integer checkBoards(String numberCalled, ArrayList<Boards> allBoards) {

    for (Boards board : allBoards) {
      board.checkForCalledNumber(numberCalled);

      if (board.checkForWinner()) {
        return board.sumRemainingNumbers();
      }
    }

    return 0;
  }

  private ArrayList<Boards> removeWinner(ArrayList<Boards> boards) {
    ArrayList<Boards> nonWinners = new ArrayList<Boards>();
    for (Boards board : boards) {
      if (!board.checkForWinner()) {
        nonWinners.add(board);
      }
    }

    return nonWinners;
  }
}