var puzzleInput = {
  1: [5806, 6444, 1281, 38,	267,	1835,	223,	4912,	5995,	230,	4395,	2986,	6048,	4719,	216,	1201],
  2: [74,	127,	226,	84,	174,	280,	94,	159,	198,	305,	124,	106,	205,	99,	177,	294],
  3: [1332,	52,	54,	655,	56,	170,	843,	707,	1273,	1163,	89,	23,	43,	1300,	1383,	1229],
  4: [5653,	236,	1944,	3807,	5356,	246,	222,	1999,	4872,	206,	5265,	5397,	5220,	5538,	286,	917],
  5: [3512,	3132,	2826,	3664,	2814,	549,	3408,	3384,	142,	120,	160,	114,	1395,	2074,	1816,	2357],
  6: [100,	2000,	112,	103,	2122,	113,	92,	522,	1650,	929,	1281,	2286,	2259,	1068,	1089,	651],
  7: [646,	490,	297,	60,	424,	234,	48,	491,	245,	523,	229,	189,	174,	627,	441,	598],
  8: [2321,	555,	2413,	2378,	157,	27,	194,	2512,	117,	140,	2287,	277,	2635,	1374,	1496,	1698],
  9: [101,	1177,	104,	89,	542,	2033,	1724,	1197,	474,	1041,	1803,	770,	87,	1869,	1183,	553],
  10: [1393,	92,	105,	1395,	1000,	85,	391,	1360,	1529,	1367,	1063,	688,	642,	102,	999,	638],
  11: [4627,	223,	188,	5529,	2406,	4980,	2384,	2024,	4610,	279,	249,	2331,	4660,	4350,	3264,	242],
  12: [769,	779,	502,	75,	1105,	53,	55,	931,	1056,	1195,	65,	292,	1234,	1164,	678,	1032],
  13: [2554,	75,	4406,	484,	2285,	226,	5666,	245,	4972,	3739,	5185,	1543,	230,	236,	3621,	5387],
  14: [826,	4028,	4274,	163,	5303,	4610,	145,	5779,	157,	4994,	5053,	186,	5060,	3082,	2186,	4882],
  15: [588,	345,	67,	286,	743,	54,	802,	776,	29,	44,	107,	63,	303,	372,	41,	810],
  16: [128,	2088,	3422,	111,	3312,	740,	3024,	1946,	920,	131,	112,	477,	3386,	2392,	1108,	2741],
}

function dayTwoPartOneSolve(puzzleInput) {
  // loops through the object to go row by row to find
  // the max and min numbers and sum it
  var sum = 0;

  for (let i = 1; i <= 16; i++) {
    sum = sum + (findMaxValue(puzzleInput[i]) - findMinValue(puzzleInput[i]));
  }

  return sum;
};

function findMaxValue(puzzleInput) {
  // this finds the max value of the row by comparing every number with the 
  // current highest at that point in time in the loop
  var maxValue = 0;
  
  for (let i = 0; i < puzzleInput.length; i++) {
    if (puzzleInput[i] > maxValue) {
      maxValue = puzzleInput[i];
    }
  };

  return maxValue;
};

function findMinValue(puzzleInput){
  // this finds the min value of the row by comparing every number with the 
  // current highest at that point in time in the loop
  var minValue = puzzleInput[0];

  for (let i = 0; i < puzzleInput.length; i++) {
    if (puzzleInput[i] < minValue) {
      minValue = puzzleInput[i];
    }
  };

  return minValue;

};

// console.log(dayTwoPartOneSolve(puzzleInput));

function dayTwoPartTwoSolve(puzzleInput) {
  // loops through the object to go row by row to find
  // the divisible number and sum it
  var sum = 0;

  for (let i = 1; i <= 16; i++) {
    sum = sum + findDivisibleValue(puzzleInput[i]);
  }

  return sum;
};

function findDivisibleValue(puzzleInput) {
  // finds the divisible number by looping through and
  // using modulo checks to see if fully divisible
  for (let i = 0; i < puzzleInput.length; i++) {
    for (let j = 0; j < puzzleInput.length; j++){
      if (puzzleInput[i] === puzzleInput[j]) {
      } else if (puzzleInput[i] % puzzleInput[j] === 0) {
        return puzzleInput[i] / puzzleInput[j];
      } else if (puzzleInput[j] % puzzleInput[i] === 0) {
        return puzzleInput[j] / puzzleInput[i];
      };
    };
  };
};

console.log(dayTwoPartTwoSolve(puzzleInput));