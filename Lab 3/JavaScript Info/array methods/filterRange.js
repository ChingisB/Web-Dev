function filterRange(arr, start, end){
    for(let i = 0; i < arr.length; i++){
        if(arr[i] < start || arr[i] > end){
            arr.splice(i, 1);
            i--;
        }
    }
}

let arr = [5, 3, 8, 1];

let filtered = filterRange(arr, 1, 4);

alert( filtered ); // 3,1 (matching values)

alert( arr ); // 5,3,8,1 (not modified)