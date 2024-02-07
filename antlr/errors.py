class InstructionLimitExceededException(BaseException):
    """Raised when instruction limit is exceeded."""
    pass


class OutputLimitExceededException(BaseException):
    """Raised when output limit is exceeded."""
    pass


class VariableNotInitializedException(BaseException):
    """Raised when variable is not initialized."""
    pass
