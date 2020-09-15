#!/usr/bin/node
if (!process.argv[2]) {
  console.log(0);
} else if (!process.argv[3]) {
  console.log(0);
} else {
  const orderValues = process.argv.slice(2).sort();
  console.log(orderValues[orderValues.length - 2]);
}
