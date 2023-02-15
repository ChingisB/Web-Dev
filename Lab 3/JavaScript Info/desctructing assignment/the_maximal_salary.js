function topSalaries(obj){
    let ans = null;
    for(let [key, val] of obj){
        if(!ans){
            ans = {'key': key, 'val': val};
        }
        if(ans['val'] < val){
            [ans['key'], ans['val']] = key, val;
        }
    }
    return ans['key'];
}