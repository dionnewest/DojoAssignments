module.exports = function (){
  return {
    add: function(num1, num2){
    	console.log("the sum is: ", num1 + num2);
    },
    multiply: function(num1, num2) {
         console.log("the product is: ", num1 * num2);
    },
    square: function(num) {
         console.log("the square of "+ num +" is: ", num * num);
    },
    random: function(num1, num2) {
    	 var random_number = Math.random()
    	 console.log(random_number)
    	 if(num1<num2){
    	 	var range = num2 - num1;
    	 	random_number = random_number * range;
    	 	random_number = random_number + num1;
    	 	random_number = Math.round(random_number);
    	 }
         console.log("the product is: ", random_number);
    }
  }
};
