import java.sql.*;

class InsertQuery
{
public static void main(String[] args) throws Exception
{
String url= "jdbc:mysql://localhost:3306/nava";;
String user="root";
String password = "1234";
Connection con = DriverManager.getConnection(url,user,password);
System.out.println("Connection Established Successfully......! \n");
con.close();
}}