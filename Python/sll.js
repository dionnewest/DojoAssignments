function SLL(){
	this head= null;
	this.printList = function(){
		var current = this.head
		while(current){
			console.log(current.val);
			current = current.next
		}
	}
	this.insert = function(val){
		var newNode = newNode(val);
	}
}