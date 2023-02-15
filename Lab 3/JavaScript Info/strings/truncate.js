function truncate(message, count){
    if(count >= message.length){
        return message;
    }
    return message.slice(0, count - 1) + '...' 
}