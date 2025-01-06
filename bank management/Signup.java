import javax.swing.*;
import java.awt.*;
import java.util.*;


public class Signup extends JFrame{
    Signup(){
        setLayout(null);

        Random ran =new Random();
        long random=Math.abs((ran.nextLong()% 9000l)+1000l);

        JLabel formno =new JLabel("Application form no."+random);
        formno.setFont(new Font("Raleway" ,Font.BOLD,38));
        formno.setBounds(140,20,600,40);
        add(formno);

        JLabel personaldetails =new JLabel("page 1:personal details");
        personaldetails.setFont(new Font("Raleway" ,Font.BOLD,20));
        personaldetails.setBounds(290,80,400,30);
        add(personaldetails);

        JLabel name =new JLabel("Name:");
        name.setFont(new Font("Raleway" ,Font.BOLD,20));
        name.setBounds(100,140,100,30);
        add(name);

        JTextField namTextField=new JTextField();
        namTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        namTextField.setBounds(300,140,400,30);
        add(namTextField);

        JLabel fname =new JLabel("Fahter's Name:");
        fname.setFont(new Font("Raleway" ,Font.BOLD,20));
        fname.setBounds(100,190,200,30);
        add(fname);

        JTextField fnamTextField=new JTextField();
        fnamTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        fnamTextField.setBounds(300,190,400,30);
        add(fnamTextField);

        JLabel DOB =new JLabel("Date Of Birth:");
        DOB.setFont(new Font("Raleway" ,Font.BOLD,20));
        DOB.setBounds(100,240,400,30);
        add(DOB);

        JTextField DOBTextField=new JTextField();
        DOBTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        DOBTextField.setBounds(300,240,200,30);
        add(DOBTextField);
         
        JLabel gender =new JLabel("Gender:");
        gender.setFont(new Font("Raleway" ,Font.BOLD,20));
        gender.setBounds(100,290,400,30);
        add(gender);

        JRadioButton male =new JRadioButton("Male");
        male.setBounds(300,290,120,30);
        male.setBackground(Color.WHITE);
        add(male);

        JRadioButton female =new JRadioButton("Female");
        female.setBounds(450,290,120,30);
        female.setBackground(Color.WHITE);
        add(female);

        ButtonGroup Gendergroup=new ButtonGroup();
        Gendergroup.add(male);
        Gendergroup.add(female);

        JLabel email =new JLabel("Email Adderss:");
        email.setFont(new Font("Raleway" ,Font.BOLD,20));
        email.setBounds(100,340,400,30);
        add(email);

        JTextField emailTextField=new JTextField();
        emailTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        emailTextField.setBounds(300,340,400,30);
        add(emailTextField);

        JLabel marital =new JLabel("Marital Status:");
        marital.setFont(new Font("Raleway" ,Font.BOLD,20));
        marital.setBounds(100,390,400,30);
        add(marital);

        JRadioButton married =new JRadioButton("Married");
        married.setBounds(300,390,100,30);
        married.setBackground(Color.WHITE);
        add(married);

        JRadioButton unmarried =new JRadioButton("unmarried");
        unmarried.setBounds(450,390,100,30);
        unmarried.setBackground(Color.WHITE);
        add(unmarried);

        JRadioButton other =new JRadioButton("others");
        other.setBounds(630,390,100,30);
        other.setBackground(Color.WHITE);
        add(other);

        ButtonGroup maritalgroup=new ButtonGroup();
        maritalgroup.add(married);
        maritalgroup.add(unmarried);
        maritalgroup.add(other);

        JLabel address =new JLabel("Adderss:");
        address.setFont(new Font("Raleway" ,Font.BOLD,20));
        address.setBounds(100,440,400,30);
        add(address);

        JTextField addressTextField=new JTextField();
        addressTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        addressTextField.setBounds(300,440,400,30);
        add(addressTextField);

        JLabel city =new JLabel("City:");
        city.setFont(new Font("Raleway" ,Font.BOLD,20));
        city.setBounds(100,490,400,30);
        add(city);
        
        JTextField cityTextField=new JTextField();
        cityTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        cityTextField.setBounds(300,490,400,30);
        add(cityTextField);

        JLabel state =new JLabel("State:");
        state.setFont(new Font("Raleway" ,Font.BOLD,20));
        state.setBounds(100,540,400,30);
        add(state);

        JTextField stateTextField=new JTextField();
        stateTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        stateTextField.setBounds(300,540,400,30);
        add(stateTextField);

        JLabel pincode =new JLabel("Pincode:");
        pincode.setFont(new Font("Raleway" ,Font.BOLD,20));
        pincode.setBounds(100,590,400,30);
        add(pincode);

        JTextField pinTextField=new JTextField();
        pinTextField.setFont(new Font("Raleway" ,Font.BOLD,14));
        pinTextField.setBounds(300,590,400,30);
        add(pinTextField);

        JButton next=new JButton("Next");
        next.setBackground(Color.BLACK);
        next.setForeground(Color.WHITE);
        next.setFont(new Font("Raleway",Font.BOLD,14));
        next.setBounds(620,660,80,30);
        add(next);


        getContentPane().setBackground(Color.WHITE);
        setSize(850,800);
        setLocation(350,10);
        setVisible(true);

    }
    public static void main(String args[]){
        new Signup();
    }
    
}
