#!/usr/bin/node
const { argv } = require('process');
if (!argv[2]) console.log('no argument');
else console.log(argv[2]);
