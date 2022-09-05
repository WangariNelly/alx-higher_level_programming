#!/usr/bin/node
let str1 = process.argv[2];
let str2 = process.argv[3];
if (str1 === undefined){
   str1 = "undefined";
}
else if (str2 === undefined){
   str2 = "undefined";
}
console.log(str1.concat(" is ", str2))
