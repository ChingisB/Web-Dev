function getSecondsToTomorrow(){
    let date = Date.now();
    let tomorrow = new Date(date.getFullYear(), date.getFullMonth(), date.getDate() + 1);
    return Math.round((tomorrow - date) / 1000);
}