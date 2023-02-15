function Calculator(){

    this.methods = {
        "+": (a, b) => a + b,
        "-": (a, b) => a - b
    }

    this.addMethod = function(opName, op){
        this.methods[opName] = op    
    }

    this.calculate = function(expression){
        expression = expression.split(' ')
        let a = +expression[0];
        let op = expression[1];
        let b = +expression[2];
        if(!this.methods[b] || isNaN(a) || isNaN(b)){
            return NaN;
        }
        return this.methods[expression[0]]
    }
}