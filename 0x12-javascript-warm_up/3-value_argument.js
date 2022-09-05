#!/usr/bin/node
let output = process.argv[2];
if (output === undefined){
   console.log("No argument");
}
else {
   console.log(output);
}
