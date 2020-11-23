function findClosestOddSquare(number) {
  rootOfNumber = Math.sqrt(number);
  console.log("The root:" + rootOfNumber);

  oddFloorOfRoot = Math.floor(rootOfNumber);
  if (oddFloorOfRoot % 2 === 0) {
    oddFloorOfRoot = oddFloorOfRoot - 1;
  };
  console.log("The floor:" + oddFloorOfRoot);
  
  oddCeilingOfRoot = oddFloorOfRoot + 1;
  if (oddCeilingOfRoot % 2 === 0) {
    oddCeilingOfRoot = oddCeilingOfRoot + 1;
  };
  console.log("The ceiling is:" + oddCeilingOfRoot);

  floorSquare = Math.pow(oddFloorOfRoot, 2);
  console.log("The floor squared is:" + floorSquare);
  ceilingSquare = Math.pow(oddCeilingOfRoot, 2);
  console.log("The ceiling squared is:" + ceilingSquare);

  floorDistance = number - floorSquare;
  console.log("The distance for the floor is:" + floorDistance);
  ceilingDistance = ceilingSquare - number;
  console.log("the ceiling distance is:" + ceilingDistance);

  if (floorDistance < ceilingDistance) {
    return floorSquare;
  } else {
    return ceilingSquare;
  }
};

function dayThreePartOne(number) {
  closestOddSquare = findClosestOddSquare(number);
  console.log("The closest odd square:" + closestOddSquare);

  stepsForClosestOddSquare = Math.sqrt(closestOddSquare) - 1;
  console.log("The steps for the closest odd square:" + stepsForClosestOddSquare)

  if (closestOddSquare < number ) {
    steps = stepsForClosestOddSquare + 1 - (number - closestOddSquare - 1);
    return steps;
  } else {
    steps = stepsForClosestOddSquare - (closestOddSquare - number);
    return steps;
  }
};

console.log(dayThreePartOne(265149));

// part two done via google sheets. Why over think it right?