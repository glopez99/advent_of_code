import calculatePerpendicularIntersections from '../Day3';
import getMin from '../Day3';
import getMax from '../Day3';

it('does this right:', () => {
    expect(calculatePerpendicularIntersections(
      {direction: 'V', same: 2, begin: 1, end: 5 },
      {direction: 'H', same: 3, begin: 5, end: 1 }
    )).toEqual([{cal: 'perp', x: 2, y: 3}]);
    });