let objects = {}

function A() { 
    return objects;
}
function B() {
    return objects;
}

let a = new A();
let b = new B();

alert( a == b ); // true