#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('No argument');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
