import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Server {

    private Scanner file;
    private static ArrayList<Node> nodes;

    public Server() throws FileNotFoundException {

        File filePath = new File("src/data.csv");
        file = new Scanner(filePath);
        nodes = new ArrayList<Node>();
        while (hasAnotherLine()) {
            String line = getLine();
            String[] lineArray = line.split(",");
            Node n = new Node();
            n.setNodeID(Integer.valueOf(lineArray[0]));
            n.setYesID(Integer.valueOf(lineArray[1]));
            n.setNoID(Integer.valueOf(lineArray[2]));
            n.setDescription(lineArray[3]);
            n.setQuestion(lineArray[4]);
            nodes.add(n);



        }


    }


    public String getLine() {
        return file.nextLine();}

    public void Close() {
        file.close();}

    public boolean hasAnotherLine() {
        return file.hasNext();}

    public String toString() {
        String string = "";
        for (Node node : nodes) {
            string += node.toString() + "\n";}
        return string;
    }

    public static Node getNode(int nodeID){
        for(Node n: nodes){
            if(n.getNodeID() == nodeID){
                return n;
            }
        }
        return null;
    }


}
