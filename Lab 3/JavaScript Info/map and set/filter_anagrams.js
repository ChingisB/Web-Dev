function aclean(arr){
    let map = new Map();
    for(let word in arr){
        let clean = word.toLowerCase().split('').sort().join('');
        map.set(clean, word);
    }
    return Array.from(map.values);
}


let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

alert( aclean(arr) ); // "nap,teachers,ear" or "PAN,cheaters,era"