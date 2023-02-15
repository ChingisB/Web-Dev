function sumInput(){
    let array = new Array();
    while(true){
        let a = prompt("Insert a number or anything else to quit");
        if(isFinite(a)){
            array.push(+a);
        }
        break;
    }
    let sum = 0;
    for(let num in array){
        sum += num;
    }
    return sum;
}