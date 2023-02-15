function sortByAge(arr){
    arr.sort((user1, user2) => {
        if(user1.age > user2.age){
            return 1;
        }
        if(user1.age == user2.age){
            return 0;
        }
        return -1;
    })
}


let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };

let arr = [ pete, john, mary ];

sortByAge(arr);

// now: [john, mary, pete]
alert(arr[0].name); // John
alert(arr[1].name); // Mary
alert(arr[2].name); // Pete