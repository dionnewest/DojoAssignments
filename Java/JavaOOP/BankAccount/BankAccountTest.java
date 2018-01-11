public class BankAccountTest{
    public static void main(String[] args){
        BankAccount acct1 = new BankAccount();
        acct1.deposit(6.42, "checking");
        acct1.deposit(700, "savings");
        acct1.withdrawl(5, "checking");
        acct1.accountInfo();
        acct1.withdrawl(7, "checking");
        acct1.accountInfo();

        BankAccount acct2 = new BankAccount();
        acct2.deposit(73.28, "checking");
        acct2.deposit(5, "savings");
        acct2.accountInfo();

        acct1.bankInfo();
        acct2.bankInfo();
    }
}