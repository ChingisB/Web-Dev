function unique(arr) {
  let ans = [];
  for(let name in arr){
    if(!ans.includes(name)){
        ans.push(name);
    }
  }
  return ans;
  
}

let strings = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

alert( unique(strings) ); // Hare, Krishna, :-O