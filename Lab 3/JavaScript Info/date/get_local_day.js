function getLocalDay(date){
    let ans = date.getDay();
    if(ans == 0){
        ans = 7;
    }
    return ans;
}