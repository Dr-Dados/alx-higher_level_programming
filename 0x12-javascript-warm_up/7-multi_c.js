#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 2) console.log('Missing number of occurrences');
else for (let i = 0; i < argv.length - 1; i++) console.log('C is fun');
