function getWeekDay(date){
    let num = date.getDay();
    if(num == 0){
        return "SU";
    }
    if(num == 1){
        return "MO";
    }
    if(num == 2){
        return "TU";
    }
    if(num == 3){
        return "WED";
    }
    if(num == 4){
        return "TH";
    }
    if(num == 5){
        return "FR";
    }
    return "SA"
}