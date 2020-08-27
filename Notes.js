var memory = [1002,4,3,4,33];

function diagnosticCode () {
    // this runs the intcomputer with an input
    // var instructionInput = input;
    var opcode = lastTwoDigits(memory[0]);
    console.log(opcode);

    if (opcode === 1 ||
        opcode === 2) {
        var output = testOpcode1And2(memory[0], memory[1], memory[2], memory[3])
        return output;
    };

    // for (let i = 0; i < memory.length; i += numberToIncreaseBy) {  
    //     var opcode = lastTwoDigits[memory[i]];
    //     var code = [];
    //     var numberToIncreaseBy = instructionNumber(opcode);

    //     if (opcode === 1 ||
    //         opcode === 2) {
    //         var output = testOpcode1And2(memory[i], memory[i + 1], memory[i + 2], memory[i + 3])
    //         console.log(output);
    //     } else {}
        // else if (opcode === 3) {
//             //opcode3 takes an input and saves it to only parameter
//             getMode(memory[i], 3, memory[i + 1]) = instructionInput;
//             console.log(getMode(memory[i], 3, memory[i + 1]));
//         } else {
//             //opcode4 outputs values at only parameter
//             var output = getMode(memory[i+1], 3);
//             console.log(output);
        //};

// // this probably isn't working the way I want it to. I need to think about this section
//         if (output != 0){
//             return output
//         } else {
//             var code = [...code, output];
//         };
//     }

//     console.log(code);
};

function testOpcode1And2(arrayStart, inputA, inputB, outputA){
    //runs the program for opcode 1 and 2
    var opcode = lastTwoDigits(arrayStart);
    var parameterA = getMode(arrayStart, 3, inputA); 
    var parameterB = getMode(arrayStart, 4, inputB);

    if (opcode === 1) {
        memory[outputA] = parameterA + parameterB;
    } else if (opcode === 2) {
        memory[outputA] = parameterA * parameterB;
        return memory[outputA];
    } else {
        throw 'There was an issue with testOpcode1and2 at ' + arrayStart + inputA + inputB + outputA;
    }
};

function instructionNumber(opcode){
    // tells the loop how many int to jump ahead
    if (lastTwoDigits(opcode) === 1
        || lastTwoDigits(opcode) === 2) {
       return 4;
    } else {
        return 2;
    }
};

function lastTwoDigits(number) {
    // returns the last two digits of opcode
    return number % 100;
};

function getDigit(number, digit) {
    // gets the appropriate digit to determine mode in opcode
    var modulus = Math.pow(10, digit);
    var divisor = Math.pow(10, digit - 1);
    return Math.floor(number % modulus / divisor);
};

function getMode (instruction, digit, parameter) {
    // looks at if it's position or immediate Mode
    var mode = getDigit(instruction, digit);
    if (mode === 1) {
        return parameter;
    } else {
        return memory[parameter];
    }
};

console.log(diagnosticCode());


// reverse a linked list or reverse a stack- learn what these are


/* From Tanya
https://github.com/whereistanya/miscellaneous-c/blob/master/stackoverflow.c
a) get a hello world program in C running on your laptop
b) then run this and see what happens :-) */