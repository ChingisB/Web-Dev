while(true){
    let ans = prompt("Enter a number greater than 100", '');
    if(+ans >= 100){
        alert("Thank you");
        break;
    }
    alert("Please, repeat again");
}