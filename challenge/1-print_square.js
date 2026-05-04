#!/usr/bin/node

if (process.argv.length <= 2) {
    process.exit(1);
}

let size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
    process.exit(1);
}

for (let i = 0 ; i < size ; i++) {
    let row = "";
    for (let j = 0 ; j < size ; j++) {
        row += "#";
    }
    console.log(row);
}
