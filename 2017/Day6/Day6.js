// var puzzleInput = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]
var puzzleInput =[0,2,7,0];

function day6PartOne (puzzleInput) {
  var database = puzzleInput;
  // console.log(database);
  var seenVariations = new Set();
  // console.log(seenVariations);
  var count = 0;

  while (seenVariations.has(database) == false) {
    var redistribution = redistribute(database);
    // console.log(redistribution);
    seenVariations.add(redistribution);
    // console.log(seenVariations);
    count += 1;
    // console.log(count);
    database = redistribution;
    // console.log(database)
  };
  
  return count;
};

function redistribute(database) {
  var startingPoint = findStartingPoint(database);
  var blocksToBeDistributed = database[startingPoint];

  database[startingPoint] = 0;

  while (blocksToBeDistributed != 0) {
    for (let i = startingPoint + 1; i < database.length; i++){
      database[i] += 1;
      blocksToBeDistributed -= 1;
      if (i == database.length - 1) {
        i = 0;
      };
    };
  };

  return database;
};

function findStartingPoint (database) {
  var startingPoint = 0;

  var max = database[0];

  for (let i = 1; i < database.length; i++){
    if (database[i] > max) {
      startingPoint = 0;
      max = database[i];
    }
  };

  return startingPoint;
};

console.log(day6PartOne(puzzleInput));