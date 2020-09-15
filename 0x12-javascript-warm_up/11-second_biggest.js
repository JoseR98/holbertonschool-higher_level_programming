#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const orderValues = process.argv.slice(2).sort();
  console.log(orderValues[orderValues.length - 2]);
}
