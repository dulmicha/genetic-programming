class InstructionLimitExceededException(Exception):
    """Raised when instruction limit is exceeded."""
    pass


class OutputLimitExceededException(Exception):
    """Raised when output limit is exceeded."""
    pass


class VariableNotInitializedException(Exception):
    """Raised when variable is not initialized."""
    pass
