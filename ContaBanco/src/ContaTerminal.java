
import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) throws Exception {

        Scanner scan = new Scanner(System.in);


        System.out.println("Bem vindo(a) a nossa agencia. Por favor, digite os dados correspondentes: ");
        

        System.out.println("Digite o nome do cliente: ");
        String nomeCliente = scan.nextLine();

        System.out.println("Digite o número da Agência:");
        String agencia = scan.nextLine();

        System.out.println("Digite o numero da conta: ");
        int numero = scan.nextInt();

        System.out.println("Digite o valor do saldo: ");
        double saldo = scan.nextDouble();

        scan.close();

        System.out.println("Olá, " + nomeCliente + ". Obrigada por criar uma conta em nosso banco. ");
        System.out.println("Sua agência é: " + agencia + ", conta " + numero + " e seu saldo " + saldo + " já está disponivel para o saque.");


       
    }
}
