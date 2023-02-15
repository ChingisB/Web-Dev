let calculator = {

    read: function(){
        this.a = +prompt("Insert first value", '');
        this.b = +prompt("Insert second value", '');
    },

    sum: function(){
        return this.a + this.b;
    },

    mul: function(){
        return this.a * this.b;
    }
}