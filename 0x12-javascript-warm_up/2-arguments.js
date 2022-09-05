#!/usr/bin/node
const count = process.argv.length;
(count < 3 ? console.log('No arguement') : count === 3 ? console.log('Argument found') : console.log('Arguements found'));
