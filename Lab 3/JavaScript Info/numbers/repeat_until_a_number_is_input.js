function readNumber(){
    let data = prompt("Please insert a number", '')
    while(!isFinite(data)){
        data = prompt("Please input a number", '')
    }
    if(data == null || data == ''){
        return null;
    }

    return +data;
}