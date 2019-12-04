/*
--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station.
During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central
port and extend outward on a grid. You trace the path each wire takes as it leaves the central port,
one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit,
you need to find the intersection point closest to the central port. Because the wires are on a grid,
use the Manhattan distance for this measurement. While the wires do technically cross right at the central
port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o),
it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?

*/
const wire1 = ["R999","D586","L462","D725","L236","U938","R366","D306","R263","D355","R354","D332","L599",
  "U48","R829","U210","R697","D534","L19","U991","L110","U981","L954","U323","R851","U290","R76","D513","R844",
  "D780","L257","D24","L586","U865","L341","U572","L122","D304","R398","D641","L221","U726","R270","D321","R503",
  "D112","L151","D179","R439","U594","R242","U1","L484","D259","L604","U760","R362","D93","R29","D647","R482","U814",
  "L214","D510","R281","U327","L170","D993","R191","D33","L305","D657","L897","U609","R512","D866","R654","U980","L899",
  "D602","L141","D365","L13","D584","L706","U404","L238","U720","L732","U716","R672","U979","L49","D352","R712","U396","L843",
  "D816","L276","U906","L375","D410","R275","U664","R487","D158","L713","D451","L859","U194","L736","D51","R659",
  "U632","R586","U342","L222","U184","R741","U989","L175","D521","R820","U183","L950","D888","R54","D149","R776","D200",
  "R939","U529","L377","D226","R769","U395","R392","U570","L398","D358","L644","D975","R578","D687","L133","D884","R822","D226",
  "L527","U439","R175","D388","L539","D450","L391","U392","L131","U134","R873","U741","R761","U620","R667","D31","R481","D945","L373",
  "D463","R57","D402","R181","U340","L835","U81","R908","U257","R592","U702","R713","D352","R418","D486","L904","U866","R828","D545",
  "R578","U469","L845","D437","R371","D246","L996","D920","L171","U83","R471","D152","R550","U344","L390","U287","L126","D883","L576",
  "U303","L68","U854","L463","D915","R184","D282","L513","U909","R770","U638","L751","U168","R354","D480","R19","U144","R381","D554",
  "R594","D526","L957","D464","R267","D802","L709","U306","L907","D266","L871","U286","R975","D549","L732","U721","R825","U753","R443","U465",
  "L966","U982","L833","D62","L5","U299","R500","D168","R155","D102","R455","D855","L376","D479","L469","D6","R588","U301","R329","U19","L63","D488",
  "L936","D238","L798","D452","L231","D652","R935","D522","L401","U234","L20","U285","L949","D88","L120","D159","R641","D960","L946","U516","L530",
  "D447","R23","U962","R860","D352","R904","D241","R702","U108","L155","U99","L43","D401","R19"
];
const wire2 = ["L1008","U23","L793","D944","L109","U830","L103","U255","L391","D574","R433","U468","R800","D831","L39","U8",
  "L410","D467","R655","D287","R550","U467","L627","D529","R361","D865","L755","D895","L148","U110","R593","U567","L646","D89","L133",
  "D552","R576","U228","L119","U734","R591","U680","L163","D498","L394","U884","R217","U46","R684","D499","L522","U373","L322","U347","R48",
  "D459","L692","U569","R267","U296","L949","U915","R599","D113","R770","U322","R304","U920","L880","D257","R915","D672","L950","U209","R601",
  "U663","R461","D514","R415","U82","L396","U233","R606","U500","R70","D696","R945","D686","L405","U176","R728","U562","L710","D35","R707","D931",
  "L857","U792","R337","D490","L963","U731","R909","U532","R375","D990","L154","U660","L17","U32","R593","U529","R136","U835","R717","U255","L93",
  "D295","L473","U608","L109","D858","R719","U207","R60","D36","R790","D382","L684","D233","R988","U625","R410","U804","R552","D578","L440","D749",
  "R653","U362","L900","U549","R790","D870","R672","U503","R343","D343","R738","D270","R494","D527","L182","U654","R933","D594","R447","U933","R4",
  "U364","L309","U967","R648","U537","R990","U203","R584","D474","L852","U736","R305","D781","R774","D92","L398","U207","R472","D664","R369","U807",
  "L474","U588","R339","D536","R305","D506","R516","U772","R177","U450","L211","U850","R777","U483","L595","U104","L916","U548","R256","U173","L27",
  "D167","L574","D288","R569","U192","R771","D98","R432","U165","L651","D524","L582","D698","L393","D152","L280","U461","R573","D771","R833","D409",
  "R991","U996","R780","U617","R63","U563","L844","D63","R15","U634","R643","D124","L147","D583","R716","D28","L799","D59","R819","D723","L43","D975",
  "L755","D635","R118","U325","L969","D445","R374","D797","L821","U118","R962","D643","R127","U267","R768","D50","L343","U80","R281","U575","R618",
  "D718","L74","U146","R242","D547","L492","U71","R826","D483","L402","U953","R184","U707","L973","D550","L593","U281","L652","D247","L254","D60",
  "R908","U581","L731","D634","R286","D186","R9","D983","L181","U262","R241","D674","R463","U238","R600"
];

function calculatePath(wire) {
  const path = [{x: 0, y: 0 }];
  for (vector of wire) {
    // R, U, L, D
    const direction = vector[0];
    // The steps traveled in a direction
    const steps = parseInt(vector.substring(1), 10);
    for (let p = 0; p < steps; p++) {
      // Start where we left off last iteration
      const lastPoint = path.slice(-1)[0];
      let { x, y } = lastPoint;
      switch(direction) {
        case "R":
          x = x + 1;
          break;
        case "U":
          y = y + 1;
          break;
        case "L":
          x = x - 1;
          break;
        case "D":
          y = y - 1;          
          break;
        default:
          console.error('Unknown direction:', direction);
      }
      path.push({ x, y });
    }    
  }
  // We don't need 0, 0
  return path.slice(1);
}

// Return all the points that intersect
function findIntersections(path1, path2) {
  return path1.filter(p => path2.find(p2 => p.x === p2.x && p.y === p2.y));
}

// Find the shortest Manhattan distance
function findClosestIntersectionDistance(intersections) {
  return intersections.map(point => Math.abs(point.x) + Math.abs(point.y))
    .reduce((min, distance) => min < distance ? min : distance);
}

const hrstart = process.hrtime();

const path1 = calculatePath(wire1);
const path2 = calculatePath(wire2);
const intersections = findIntersections(path1, path2);
const closestIntersectionDistance = findClosestIntersectionDistance(intersections);

console.log('Part 1:', closestIntersectionDistance);

/*
--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the
intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times,
use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location,
including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the
first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes
only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
*/

// Find the shortest combined steps to intersection
function findFewestStepsToIntersection(intersections, path1, path2) {
  return intersections
    .map(intersection => {
      const path1Steps = path1.findIndex(point => point.x === intersection.x && point.y === intersection.y) + 1;
      const path2Steps = path2.findIndex(point => point.x === intersection.x && point.y === intersection.y) + 1;
      return path1Steps + path2Steps;
    })
    .reduce((min, steps) => min < steps ? min : steps);
}

const fewestStepsToIntersection = findFewestStepsToIntersection(intersections, path1, path2);
console.log('Part 2:', fewestStepsToIntersection);

const hrend = process.hrtime(hrstart);
console.info('Execution time: %dms', hrend[1] / 1000000);