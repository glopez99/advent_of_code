/* Part 3  & 4
Now the arrays don't alternate numbers but
are guaranteed to be increasing. Combine
them.
ex. array1 = [1,2,3] array2 =[4,5,6]
What if an array is empty?
Try and do this only using push.
*/

// var array1 = [1,2,3];
// var array2 = [4,5,6];
var array1 = [];
var array2 = [2,4,6];
// var array1 = [4,5,6];
// var array2 = [1,2,3];
// var array1 = [1,2,3,7,8,9];
// var array2 = [4];


function combineLists(array1, array2) {
/* combines the two inputs from the lowest number to highest
by treating each array like a deck of cards with only 1
card showing. Compare the two cards. Take the lowest. Put in
a middle deck. Repeatuntil one deck is empty. 
Then combine the remaining deck in order.
*/
    var combinedLists = [];

    do {
        combinedLists.push(getLowestNumber(array1, array2));
        getLowestArray(array1, array2).shift();
        shortestArray = getShortestArrayLength(array1, array2);
    } while (shortestArray !== 0);

    var longestArray = getLongestArray(array1, array2);

    combinedLists = [...combinedLists, ...longestArray];

    return combinedLists;
};

function getLowestNumber (array1, array2) {
    /* this returns the lowest number in position 0
    out of the two arrays */
    if (array1[0] < array2[0]) {
        return array1[0];
    } else {
        return array2[0];
    }
};

function getLowestArray (array1, array2) {
    /* this returns the entire array that has the lowest number
    so that that number can be removed from the array */
    if (array1[0] < array2[0]) {
        return array1;
    } else {
        return array2;
    }
};

function getLongestArray(array1, array2) {
    // this returns the longest array out of the two
    if (array1.length > array2.length) {
        return array1;
    } else {
        return array2;
    }
};

function getShortestArrayLength (array1, array2) {
    // this returns the length of the shortest array
    if (array1.length < array2.length) {
        return array1.length;
    } else {
        return array2.length;
    }
};

console.log(combineLists(array1, array2));


/* Part 2
 In your method take two arrays that are guaranteed
 to be increasing in order and combine them.
 So you might get two like [1,3,5] and [2,4,6]. 
 See if you can figure out how to make it efficient.

var array1 = [1,3,5];
var array2 = [2,4,6];

function combineLists(array1, array2) {
    // combines the lists by pushing array1[i] followed by array2[i]
    var combinedLists = [];

    for (let i = 0; i < array1.length; i++){
        combinedLists.push(array1[i], array2[i]);
    };

    return combinedLists;
};

console.log(combineLists(array1, array2)); */





/* Part 1 combine two lists and sort from lowest to highest

var array1 = [1,9,3,7,5];
var array2 = [2,10,4,8,6];

function combineLists(array1, array2) {
    var combinedLists = [];

     for (let i = 0; i < array1.length; i++) {
         combinedLists.push(array1[i], array2[i]);
     };
     return combinedLists.sort((l,r) => l - r);
};

console.log(combineLists(array1, array2)); */