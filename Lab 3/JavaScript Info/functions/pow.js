function pow(x, n){
    let res = 1;
    for(let i = 0; i < n; i++){
        res *= x;
    }
    return res;
}

alert(pow(2, 10))