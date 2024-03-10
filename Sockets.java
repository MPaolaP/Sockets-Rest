package paola.sockets;
import java.io.*;
import java.net.*;

public class Sockets {
    public static void main(String[] args) {
        String hostName = "localhost";  // Dirección del servidor
        int portNumber = 65432;  // El puerto debe coincidir con el servidor

        try (
            Socket socket = new Socket(hostName, portNumber);
            PrintWriter out =
                new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in =
                new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));
            BufferedReader stdIn =
                new BufferedReader(
                    new InputStreamReader(System.in))
        ) {
            System.out.println("Escribe un mensaje para el servidor:");
            String userInput;
            while ((userInput = stdIn.readLine()) != null) {
                out.println(userInput);
                System.out.println("Respuesta del servidor: " + in.readLine());
            }
        } catch (UnknownHostException e) {
            System.err.println("No se conoce el host: " + hostName);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("No se pudo obtener I/O para la conexión a " +
                hostName);
            System.exit(1);
        } 
    }
}