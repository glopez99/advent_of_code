/* Continue building out Intcode computer adding in Opcode3 & 4
and adding in position mode and immediate mode. Then using an input
find the only output that isn't a 0.
*/

var memory = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,61,225,101,34,121,224,1001,224,-49,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1101,67,29,225,1,14,65,224,101,-124,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,20,225,1102,27,15,225,1102,18,79,224,101,-1422,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,20,44,225,1001,69,5,224,101,-32,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,15,10,225,1101,6,70,225,102,86,40,224,101,-2494,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,25,15,225,1101,40,67,224,1001,224,-107,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,126,95,224,101,-1400,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1002,151,84,224,101,-2100,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,509,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1007,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,659,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226];
// var memory = [1,1,3,1,1002,9,3,9,99,33];


function diagnosticCode (input) {
    // this runs the Intcode computer with an input
    var code = [];

    for (let i = 0; i < memory.length; i += numberToIncreaseBy) {  
        var opcode = lastTwoDigits(memory[i]);
        var numberToIncreaseBy = instructionNumber(opcode);

        if (opcode === 1 ||
            opcode === 2) {
            testOpcode1And2(memory[i], memory[i + 1], memory[i + 2], memory[i + 3])
        } else if (opcode === 3) {
            //opcode3 takes an input and saves it to the only parameter
            memory[memory[i + 1]] = input;
        } else if (opcode === 4) {
            //opcode4 outputs the value at the only parameter
            var output = getMode(memory[i], 3, memory[i + 1]);
            code = [...code, output];
        } else if(opcode === 99) {
            return code;
        };
    };
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

console.log(diagnosticCode(1));

/* Part two - adds in opcode 5,6,7,8.
Parameter modes are still active, but instruction pointers
are now added so they don't jump a guaranteed 2 or 4 items.
The input is now 5.
-------
I also reworked the Intcode Computer to be better.
*/

function parse(memory,instructionPointer) {
    return {
        operation: ,// 1-8
        parameters: [], //already read out of memory and dereferenced
        skip: 2 || 4,
    }
};

function diagnosticCode(memory, instructionPointer) {
    while (memory[instructionPointer] !== 99) {
        op = parse(memory, instructionPointer);
        if (op.operation === 1) {
            memory[op.paramenters[2]] = op.parameters[0] +
            op.parameters[1];
            instructionPointer = instructionPointer + op.skip;
        } else if (...)
    }
}
