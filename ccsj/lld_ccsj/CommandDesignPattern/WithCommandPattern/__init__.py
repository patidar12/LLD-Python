'''
Command Design Pattern:
It seprates the logic of:

- Recevier (Who recevie the command ex: AcConditioner, Tv)
- Invoker (Who invoke the command ex: remote)
- Command (Command the provide to Recevier by Invoker)
- Client (Can be a user, Who usage the invoker to generate a command for particular recevier.
          For ex: As a user i can use remote and press a button, so when i press a button a command is generated
          for recevier(TV) and executed)
'''