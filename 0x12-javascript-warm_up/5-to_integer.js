#!/usr/bin/node
if (!process.argv[2] || !Number(process.argv[2])) {
  console.log('No argument');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}
