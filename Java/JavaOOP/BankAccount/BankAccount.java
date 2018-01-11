import java.util.*;

public class BankAccount{
    public String accountNumber;
    public double checkingBalance;
    public double savingsBalance;
    public static int totalAccounts = 0;
    public static double totalMoney = 0;

    private String generateAccountNumber(){
        Random rand = new Random();
        int num = rand.nextInt(999999999) + 100000000;
        accountNumber = Integer.toString(num);
        return accountNumber;
    }

    BankAccount(){
        accountNumber = generateAccountNumber();
        totalAccounts++;
    }

    public Object deposit(double amount, String account){
        if (account == "checking"){
            totalMoney += amount;
            checkingBalance += amount;
            return checkingBalance;
        } else if (account == "savings"){
            totalMoney += amount;
            savingsBalance += amount;
            return savingsBalance;
        } else {
            String message = "Must enter 'checking' or 'savings' into account field";
            return message;
        }
    }

    public Object withdrawl(double amount, String account){
        if (account == "checking"){
            if(amount <= checkingBalance){
                totalMoney -= amount;
                checkingBalance -= amount;
                return checkingBalance;
            } else {
                String message = "Insufficient funds in checking account";
                System.out.println(message);
                return message;
            }
        } else if (account == "savings"){
            if(amount <= savingsBalance){
                totalMoney -= amount;
                savingsBalance -= amount;
                return savingsBalance;
            } else {
                String message = "Insufficient funds in savings account";
                System.out.println(message);
                return message;
            }
        } else {
            String message = "Must enter 'checking' or 'savings' into account field";
            System.out.println(message);
            return message;
        }
    }

    public void accountInfo(){
        System.out.println("Account Number: " + accountNumber + ", Checking Account Balance: $" + checkingBalance + ", Savings Account Balance: $" + savingsBalance);
    }

    public void bankInfo(){
        System.out.println("Total Number of Accounts: " + totalAccounts + ", Total Amount $" + totalMoney);
    }

}