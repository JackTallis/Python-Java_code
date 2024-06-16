import java.io.FileNotFoundException;
import java.util.Scanner;

public class UserInteraction {

    public static void main(String[] args) throws FileNotFoundException {

        Server svr = new Server();

        //System.out.println(svr.toString());
        //start here
        Node n = Server.getNode(0);   //story start


        Scanner io = new Scanner(System.in); //accepting i/o

        while(true){
            System.out.println(n.toString());
            int input = io.nextInt();
            int NextNodeID = (0); //getting the next node

            if (input == 1){ //the input from the user for if the user enters 1 it will go to the response
                NextNodeID = n.getYesID(); //if the user enters 1 it goes to the node it is attached to and grabs it for the user and displays it
            } else if(input == 0){
                NextNodeID = n.getNoID();
            } else{
                System.out.println("invalid input, Please try again!");//this is for if the user
            }

            n = Server.getNode(NextNodeID);

        }

    }

}
