import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Login  extends JFrame implements ActionListener{
    JButton login,signup,clear;
    JTextField cardteTextField;
    JPasswordField pinTextField;
    Login(){
        setLayout(null);
        setTitle("BANK MANAGEMENT SYSTEM");
        getContentPane().setBackground(Color.WHITE);

        JLabel text=new JLabel("WELCOME TO THE BANK");
        text.setFont(new Font("Osward",Font.BOLD,38));
        text.setBounds(200,40,400,40);
        add(text);

        JLabel cardno=new JLabel("CARDNO:");
        cardno.setFont(new Font("Raleway",Font.BOLD,28));
        cardno.setBounds(120,150,150,40);
        add(cardno);

        cardteTextField=new JTextField();
        cardteTextField.setBounds(300,150,250,30);

        add(cardteTextField);



        JLabel pin=new JLabel("PIN:");
        pin.setFont(new Font("Raleway",Font.BOLD,28));
        pin.setBounds(120,220,250,40);
        add(pin);
        
        pinTextField=new JPasswordField();
        pinTextField.setBounds(300,220,250,30);
        add(pinTextField);

        login=new JButton("sign in");
        login.setBackground(Color.BLACK);
        login.setForeground(Color.WHITE);
        login.setBounds(300,300,100,40);
        login.addActionListener(this);
        add(login);

        clear=new JButton("clear");
        clear.setBackground(Color.BLACK);
        clear.setForeground(Color.WHITE);
        clear.setBounds(420,300,100,40);
        clear.addActionListener(this);
        add(clear);

        signup=new JButton("sign up");
        signup.setBackground(Color.BLACK);
        signup.setForeground(Color.WHITE);
        signup.setBounds(300,350,200,40);
        signup.addActionListener(this);
        add(signup);

        setSize(800,800);
        setLocation(350,200);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent ae){
        if (ae.getSource() == clear){
            cardteTextField.setText("");
            pinTextField.setText("");

        }else if (ae.getSource()==login){

        }else if (ae.getSource()==signup){

        }
            
        

    }

    public static void main(String args[]){
        new Login();

    }

}