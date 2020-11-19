/* Facts:
    1. it is a 6 digit number
    2. the value is within the range given.
    3. Two adjacent digits are the same (like 22 in 122345)
    4. Going from left to right, the digits never decrease, they only increase or stay the same.

Question: How many different passwords within the range given in your puzzle input meet these criteria? */

const inputMin = 245318;
const inputMax = 765747;

// const inputMin = 177777;
// const inputMax = 177789;

function isSixDigits(password) {
    if (password.length === 6) {
        return true;
    } 
    return false;
};

function isInRange(password) {
    password = +password;
    if (inputMin <= password && password <= inputMax){
        return true;
    }
    return false;
};  

function hasRepeatNumbers(password) {
    for (let i = 0; i < password.length - 1; i++) {
        if (password.charAt(i) === password.charAt(i + 1)) {
            return true;
        }
    }
    return false;
};

function neverDecreases(password){
    for (let i = 0; i < password.length - 1; i++) {
        if (password.charAt(i) > password.charAt(i + 1)) {
            return false;
        }
    }
    return true;
};

function hasAGroupOfExactlyTwo(password){
    if (password.charAt(0) === password.charAt(1) 
        && password.charAt(1) != password.charAt(2) ||
        password.charAt(1) === password.charAt(2) 
        && password.charAt(0) != password.charAt(1) 
        && password.charAt(2) != password.charAt(3) ||
        password.charAt(2) === password.charAt(3) 
        && password.charAt(1) != password.charAt(2) 
        && password.charAt(3) != password.charAt(4) ||
        password.charAt(3) === password.charAt(4) 
        && password.charAt(2) != password.charAt(3) 
        && password.charAt(4) != password.charAt(5) ||
        password.charAt(4) === password.charAt(5) 
        && password.charAt(3) != password.charAt(4) 
        && password.charAt(5) != password.charAt(6) ||
        password.charAt(5) === password.charAt(6) 
        && password.charAt(4) != password.charAt(5)) {
           return true;
        }
    return false;

};

function numberOfDifferentPasswords(min, max) {
    var totalPasswords = [];

    for (let i = min; i <= max; i++){
        totalPasswords.push(i + '');
    }

    return totalPasswords
    .filter(isSixDigits)
    .filter(isInRange)
    .filter(neverDecreases)
    .filter(hasAGroupOfExactlyTwo);
};

console.log(numberOfDifferentPasswords(inputMin, inputMax).length);
