
class Parent {
    constructor(){
        this.name = "name";
    }
}

class MiddleParent extends Parent{
    constructor() {
        super()
    }
}

class LastParent extends MiddleParent{

}

class LastParent2 extends MiddleParent{

}

class Child extends LastParent{

}


const parent = new Parent();
const middle = new MiddleParent();
const last = new LastParent();
const last2 = new LastParent2();
const child = new Child();

console.dir(last2);

console.dir(child);

