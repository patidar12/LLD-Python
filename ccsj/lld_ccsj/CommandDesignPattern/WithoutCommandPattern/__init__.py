'''
Problem:
No abstraction,
Exposed main logic to client. Client need to handle all the operation.
in good programming practice, Client should only know the things that he is intersted in.

Because if we made any changes in any functionality of ac conditioner then client need to update the code.
That is not good. Because ac conditioner may be used on multiple places. And it can break on some places.
Also it is not extendable as if we wan't to add any other commands like BulbOn, BulbOff then we have to implement seprate thing.
And client need to handle it seprate. ALso we are not handling any undo/redo functionality here.

To resolve aboce issues we can use cmmand design pattern.
'''