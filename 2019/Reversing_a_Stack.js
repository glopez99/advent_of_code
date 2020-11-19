/*  Question from Matt Flower:
 *  Reverse a stack and a linked list.
 */

 class Stack {
   constructor () {
    //this._storage = [];
    this._head = null;
   }

  push(item) {
    // adds an item to the stack
    if (!item) {
      throw `This ${item} is invalid.`;
    }

    this._head = {
      item: item,
      next: this._head,
    };


  }

  pop(){
    // returns the first item in the stack and gets rid of it
    if(this.isEmpty()) {
      throw `This is an empty stack`;
    }

    const toReturn = this._head.item;
    this._head = this._head.next;

    return toReturn;
  };

  peek() {
    // looks at the first item in the stack but doesn't get rid of it
    if(this.isEmpty()) {
      throw `This is an empty stack.`;
    } else {
      return this._head.item;
    }
  };

  isEmpty() {
    // tells us if the stack is empty
    return this._head === null;
  };

  printStack() {
    // prints the stack
    return this._head;
  };

  reverseStackOrder() {
    /* Reverses the stack by creating a new Stack and
     * pushing in the items starting with the front of
     * the current stack.
    */
    var reversedStack = new Stack();

    while (!this.isEmpty()) {
      reversedStack.push(this.pop());
    };

    this._head = reversedStack._head;
  };
 };

 
var stack = new Stack();

stack.push('apple');
stack.push('orange');
stack.push('banana');
stack.push('peach');

console.log(JSON.stringify(stack,null, 2));

stack.reverseStackOrder();

console.log(JSON.stringify(stack,null, 2));


/* Prints
 * [
 * { item: 'peach', next: 'banana' },
 * { item: 'banana', next: 'orange' },
 * { item: 'orange', next: 'apple' },
 * { item: 'apple', next: null }
 * ]
 * [
 * { item: 'apple', next: 'orange' },
 * { item: 'orange', next: 'banana' },
 * { item: 'banana', next: 'peach' },
 * { item: 'peach', next: null }
 * ]
 */