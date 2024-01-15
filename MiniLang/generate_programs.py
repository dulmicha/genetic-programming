import random
from enum import Enum, auto
from dataclasses import dataclass, field

# INDENT = "\t"
INDENT = "  "


class NodeType(Enum):
    LOOP = 0
    IF = auto()
    ASSIGNMENT = auto()
    PRINT = auto()
    CONDITION = auto()
    CONDITION_BODY = auto()
    INPUT = auto()
    EXPRESSION = auto()
    MATH_EXPRESSION = auto()
    BLOCK_STATEMENT = auto()
    VAR = auto()
    NONZERO_DIGIT = auto()
    INTEGER = auto()
    BOOLEAN = auto()


class ArithmeticOperator(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

    def __str__(self) -> str:
        return self.value


class ComparisonOperator(Enum):
    EQUAL = "=="
    NOT_EQUAL = "!="
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_OR_EQUAL = ">="
    LESS_THAN_OR_EQUAL = "<="

    def __str__(self) -> str:
        return self.value


class LogicalOperator(Enum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return self.value


@dataclass
class Node:
    n_type: NodeType
    children: list = field(default_factory=list)
    parent: "Node" = None
    value: str = ""
    is_root: bool = False
    level: int = 0
    variables: list = field(init=False, default_factory=list)
    attributes: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.parent:
            self.variables = self.parent.variables
            self.level = (
                self.parent.level + 1
                if not self.n_type == NodeType.BLOCK_STATEMENT
                else self.parent.level
            )

    def get_random_variable(self):
        if random.random() < 0.5 and self.variables:
            return random.choice(self.variables)
        return self._generate_variable_name()

    def _generate_variable_name(self):
        variable_name = f"X_{len(self.variables)}"
        self.variables.append(variable_name)
        return variable_name

    def __str__(self) -> str:
        match self.n_type:
            case NodeType.LOOP:
                return f'for {self.attributes["iterations"]} {self.children[0]}'
            case NodeType.IF:
                return f'if ({self.attributes["condition"]}) {self.children[0]}'
            case NodeType.ASSIGNMENT:
                return f"{self.children[0]} = {self.children[1]};\n"
            case NodeType.PRINT:
                return f"print({self.children[0]});\n"
            case NodeType.CONDITION:
                return f"{self.children[0]}"
            case NodeType.CONDITION_BODY:
                return f'{self.children[0]} {self.attributes["operator"]} {self.children[1]}'
            case NodeType.INPUT:
                return f"input()"
            case NodeType.EXPRESSION:
                return f"{self.children[0]}"
            case NodeType.MATH_EXPRESSION:
                return f'({self.children[0]} {self.attributes["operator"]} {self.children[1]})'
            case NodeType.BLOCK_STATEMENT:
                body = f'{"".join([self.level * INDENT + str(child) for child in self.children])}'
                if self.is_root:
                    return body
                return "{\n" + body + (self.level - 1) * INDENT + "}\n"
            case NodeType.VAR:
                return f"{self.value}"
            case NodeType.NONZERO_DIGIT:
                return f"{self.value}"
            case NodeType.INTEGER:
                return f"{self.children[0]}"
            case NodeType.BOOLEAN:
                return f"{self.value}"
            case _:
                raise Exception("Unknown node type")


@dataclass
class Program:
    max_depth: int = 0
    max_width: int = 1
    root: Node = field(init=False)

    def __post_init__(self):
        self.root = self._generate_program()

    def _generate_program(self):
        root = Node(NodeType.BLOCK_STATEMENT, is_root=True)
        for _ in range(self.max_width):
            root.children.append(self._generate_instruction(root))
        return root

    def _calculate_depth(self, node):
        if len(node.children) == 0:
            return 1
        return 1 + max([self._calculate_depth(child) for child in node.children])

    def _calculate_depth_to_root(self, node):
        if node.is_root:
            return 1
        return 1 + self._calculate_depth(node.parent)

    def _generate_block_statement(self, parent):
        node = Node(NodeType.BLOCK_STATEMENT, parent=parent, level=parent.level + 1)
        # for _ in range(random.randint(1, self.max_width)): depending on method
        for _ in range(self.max_width):
            node.children.append(self._generate_instruction(node))
        return node

    def _generate_instruction(self, parent):
        instruction_types = [NodeType.ASSIGNMENT, NodeType.PRINT]
        if self._calculate_depth_to_root(parent) < self.max_depth:
            instruction_types.extend([NodeType.LOOP, NodeType.IF])
        n_type = random.choice(instruction_types)
        if n_type == NodeType.LOOP:
            return self._generate_loop(parent)
        elif n_type == NodeType.IF:
            return self._generate_if(parent)
        elif n_type == NodeType.ASSIGNMENT:
            return self._generate_assignment(parent)
        elif n_type == NodeType.PRINT:
            return self._generate_print(parent)

    def _generate_loop(self, parent):
        node = Node(
            NodeType.LOOP,
            parent=parent,
            attributes={"iterations": self._generate_nonzero_digit()},
        )
        node.children.append(self._generate_block_statement(node))
        return node

    def _generate_print(self, parent):
        node = Node(NodeType.PRINT, parent=parent, level=parent.level)
        node.children.append(self._generate_expression(parent))
        return node

    def _generate_if(self, parent):
        node = Node(
            NodeType.IF,
            parent=parent,
            attributes={"condition": self._generate_condition(parent)},
        )
        node.children.append(self._generate_block_statement(node))
        return node

    def _generate_condition_body(self, parent):
        node = Node(
            NodeType.CONDITION_BODY,
            parent=parent,
            attributes={"operator": random.choice(list(ComparisonOperator))},
        )
        node.children.append(self._generate_expression(parent))
        node.children.append(self._generate_expression(parent))  # excluding boolean
        return node

    def _generate_condition(self, parent):
        node = Node(NodeType.CONDITION, parent=parent)
        node.children.append(
            self._generate_condition_body(parent)
        )  # excluding longer conditions
        return node

    def _generate_variable(self, parent):
        node = Node(NodeType.VAR, parent=parent)
        node.value = parent.get_random_variable()
        return node

    def _generate_assignment(self, parent):
        node = Node(NodeType.ASSIGNMENT, parent=parent)
        node.children.append(self._generate_variable(parent))
        if random.random() < 0.5:
            node.children.append(self._generate_input(parent))
        else:
            node.children.append(self._generate_expression(parent))
        return node

    def _generate_input(self, parent):
        node = Node(NodeType.INPUT, parent=parent)
        return node

    def _count_nested_expressions(self, node):
        nested_expressions = 0
        while node.parent:
            if node.n_type in [NodeType.EXPRESSION, NodeType.MATH_EXPRESSION]:
                nested_expressions += 1
            node = node.parent
        return nested_expressions

    def _generate_expression(self, parent):
        node = Node(NodeType.EXPRESSION, parent=parent)
        expr_types = [NodeType.VAR, NodeType.INTEGER]
        if self._count_nested_expressions(parent) < self.max_width:
            expr_types.append(NodeType.MATH_EXPRESSION)
        _expr_type = random.choice(expr_types)
        if _expr_type == NodeType.VAR:
            node.children.append(self._generate_variable(parent))
        elif _expr_type == NodeType.INTEGER:
            node.children.append(self._generate_integer(parent))
        elif _expr_type == NodeType.MATH_EXPRESSION:
            node.children.append(self._generate_math_expression(parent))
        return node

    def _generate_math_expression(self, parent):
        node = Node(
            NodeType.MATH_EXPRESSION,
            parent=parent,
            attributes={"operator": random.choice(list(ArithmeticOperator))},
        )
        node.children.append(self._generate_expression(parent))
        node.children.append(self._generate_expression(parent))
        return node

    def _generate_integer(self, parent):
        node = Node(NodeType.INTEGER, parent=parent)
        node.children.append(self._generate_nonzero_digit())
        return node

    def _generate_nonzero_digit(self):
        node = Node(NodeType.NONZERO_DIGIT)
        node.value = str(random.randint(1, 9))
        return node

    def __str__(self):
        return str(self.root)


program = Program(2, 2)
print(program)
