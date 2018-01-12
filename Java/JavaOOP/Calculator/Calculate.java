public class Calculate{
    public double num1;
    public double num2;
    public String operator;

    Calculate(double a, String b, double c){
        num1 = a;
        operator = b;
        num2 = c;
    }

    public void setNum1(double a){
        num1 = a;
    }

    public void setNum2(double a){
        num2 = a;
    }

    public void setOperator(String a){
        operator = a;
    }

    public Object performOperation(){
        Object result = 0;
        if(operator == "+"){
            result = num1 + num2;
        } else if(operator == "-"){
            result = num1 - num2;
        } else if(operator == "*"){
            result = num1*num2;
        } else if(operator =="/"){
            result = num1/num2;
        } else {
            result = "Cannot calculate these numbers. Please enter '+', '-', '*' or '/'";
        }
        System.out.println(result);
        return result;
    }
}