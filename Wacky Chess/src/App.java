import javax.swing.*;

class App {
    public static void main(String args[]){

       JFrame frame = new JFrame("Wacky Chess");




       ImageIcon background = new ImageIcon("imgs/background.jpeg");
       JLabel label = new JLabel(background);
       JLayeredPane layeredPane = new JLayeredPane();


       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       frame.setSize(300,300);





       JButton button = new JButton("Press");



       frame.getContentPane().add(button); // Adds Button to content pane of frame


       
       
       frame.setVisible(true);


       
    }
}