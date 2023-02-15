let map = new Map();

map.set("name", "John");

let keys = map.keys();

// Error: keys.push is not a function
keys.push("more");

//we should redefine it or make an array from it
//like following
keys = Array.from(key);