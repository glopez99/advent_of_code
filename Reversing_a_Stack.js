/*  Question from Matt Flower:
 *  Reverse a stack and a linked list.
 */

 class Stack {
   constructor () {
    this._storage = [];
    this._head = null;
   }

  push(item) {
    if (!item) {
      throw `This ${item} is invalid.`;
    }

    if (this.isEmpty()) {
      this._head = {
        item: item,
        next: null,
      };
    } else {
      this._head = {
        item: item,
        next: this._head.item,
      };
    }

    if (this.isEmpty()) {
      this._storage = [...this._storage, this._head];
    } else {
      this._storage = [this._head, ...this._storage];
    };

  }

  pop(){
    if(this.isEmpty()) {
      throw `This is an empty stack`;
    }

    const toReturn = this._head.item;
    this._head = this._head.next;

    for (i = 0; i < this._storage.length; i++) {
      this._storage[i] = this._storage[i + 1];
    };

    return toReturn;
  };

  peek() {
    if(this.isEmpty()) {
      throw `This is an empty stack.`;
    } else {
      return this._head.item;
    }
  };

  isEmpty() {
    return this._head === null;
  };

  printStack() {
    return this._storage;
  };

  reverseStackOrder() {
    var reversedStack = [];
    this._head = null;
    for (let i = 0; i < this._storage.length; i++){
      if (this._storage[this._storage.length - (2 + i)] != undefined){
        this._head = this._storage[this._storage.length - (2 + i)].item;
      } else {
        this._head = null;
      }
      
      var item = {
        item: this._storage[this._storage.length - (1 + i)].item,
        next: this._head,
      }
      reversedStack = [...reversedStack, item];
    };

    this._storage = reversedStack;
  };
 };

 
var stack = new Stack;

stack.push('apple');
stack.push('orange');
stack.push('banana');
stack.push('peach');

console.log(stack.printStack());

stack.reverseStackOrder();

console.log(stack.printStack());

 