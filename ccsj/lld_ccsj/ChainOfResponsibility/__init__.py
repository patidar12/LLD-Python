''''
Chain of responsibility:

Where the request can be fulfile by one or more processor or class.

For ex:
 ATM:
    Where a user can request of 3000 rs.
    first request will go to 2000rs proceesor if it is have 2000 note it fullfil.
    and for rest of 1000 request went to 500rs processor. where if in ATM only 1 note of 500 available
    then it request hope to 100rs processor. and if ATM have enough 100 rs note then it fullfill it.
    Else it can't fullfil it.

Logger:
    Same logger here we designed by using chain of responsibility principle.


'''