
function Parent(name) {
    this.name = name
    this.fuc = function(){
        return "hello";
    }
}

function MiddleParent(name, value) {
    Parent.call(this, name);
    this.value = value

    this.sayHi = function sayHi() {
        return "hi";
    }
}

function LastParent(name, value) {
    MiddleParent.call(this, name, value);
}

function LastParent2() {
}

function Child() {
}


/* Parent.prototype.constructor = LastParent;

MiddleParent.prototype = new Parent();


const middle = new MiddleParent();
const middle2 = new MiddleParent();

console.log(middle); */





const middle = new LastParent();

console.log(middle);
console.log(middle.fuc());
console.log(middle.sayHi());

