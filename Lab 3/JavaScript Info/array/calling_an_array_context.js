let arr = ["a", "b"];

arr.push(function() {
  alert( this );
});

arr[2](); // string representation of array is shown a, b function{}