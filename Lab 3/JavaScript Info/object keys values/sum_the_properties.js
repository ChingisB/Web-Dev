function sumSalaries(obj){
  let ans = 0;
  for(let item in Object.keys(obj)){
    ans += item;
  }
  return ans;
}

let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};

alert( sumSalaries(salaries) ); // 650