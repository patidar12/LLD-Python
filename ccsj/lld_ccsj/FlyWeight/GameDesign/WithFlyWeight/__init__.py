'''

Observer and understand, when to use this pattern:
    When Memory is Limited
    When Object shared data:
    - Intrinsic data: shared among objects and remain same once defined one value.
            ex: type, body
    - Extrinsic data: changed based on client input and differs from one object to another.
            ex: cordinate_x, cordinate_y
    Creation of object is expensive.

    This is how it resolve the issue:
    - From object, remove all the Extrinsic data and keep Intrinsic Data (this is called Flyweight Object)
    - This Fliweight can be immutable.
    - Extrinsic data can be passed to the Flyweight class as method parameter.
    - Once the Flyweight Object is created, it is cached and reused whenever required.

To correctly implement this, please check WithFlyewight folder.

'''