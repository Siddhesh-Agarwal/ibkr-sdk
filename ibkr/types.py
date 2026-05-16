from enum import StrEnum


class OrderStatus(StrEnum):
    INACTIVE = "Inactive"
    PENDING_SUBMIT = "PendingSubmit"
    PRE_SUBMITTED = "PreSubmitted"
    SUBMITTED = "Submitted"
    FILLED = "Filled"
    PENDING_CANCEL = "PendingCancel"
    CANCELLED = "Cancelled"
    WARN_STATE = "WarnState"


class TimeInForce(StrEnum):
    DAY = "DAY"
    GTC = "GTC"
    IOC = "IOC"
    FOK = "FOK"
    GTX = "GTX"
    CLOSE = "CLOSE"


class Side(StrEnum):
    BUY = "BUY"
    SELL = "SELL"


class PutOrCall(StrEnum):
    PUT = "P"
    CALL = "C"
