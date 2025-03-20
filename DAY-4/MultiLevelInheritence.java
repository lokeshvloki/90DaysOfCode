// Parent class
class Animal {
    void eat() {
        System.out.println("This animal eats food.");
    }
}

// Intermediate class
class Mammal extends Animal {
    void walk() {
        System.out.println("Mammals can walk.");
    }
}

// Child class
class Human extends Mammal {
    void speak() {
        System.out.println("Humans can speak.");
    }
}

public class MultilevelInheritance {
    public static void main(String[] args) {
        Human h = new Human();
        h.eat();
        h.walk();
        h.speak();
    }
}
