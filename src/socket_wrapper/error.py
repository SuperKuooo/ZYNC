class Error(enumerate):
    EmptyResult = -1
    NoFile = 1
    NoRecvTarget = 2
    FailToSend = 3
    FailToInitialize = 4
    FailSocketOp = 5
    NoSuchOp = 6
    CloseSocket = 7

    Other = 99