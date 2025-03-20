// Parent class
class Vehicle {
    void start() {
        System.out.println("Vehicle is starting.");
    }
}

// Child class 1
class Car extends Vehicle {
    void fourWheels() {
        System.out.println("Car has four wheels.");
    }
}

// Child class 2
class Bike extends Vehicle {
    void twoWheels() {
        System.out.println("Bike has two wheels.");
    }
}

public class HierarchicalInheritance {
    public static void main(String[] args) {
        Car c = new Car();
        c.start();
        c.fourWheels();

        Bike b = new Bike();
        b.start();
        b.twoWheels();
    }
}
