let salaries = {
  John: 100,
  Ann: 160,
  Pete: 130
}

let ans = 0;
for(key in salaries){
    ans += salaries[key];
}
alert(ans);