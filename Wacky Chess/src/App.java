import classes.*;

class App {
    public static void main(String args[]){

        Board board = new Board();
        board.startGame();
        System.out.println(board.toString());


    }
}