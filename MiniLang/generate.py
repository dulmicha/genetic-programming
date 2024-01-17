import random
from enum import Enum, auto
from dataclasses import dataclass, field

from MiniLang.errors import InvalidGenerationError

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
    level: int = 1
    variables: list = field(init=False, default_factory=list)
    attributes: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.parent:
            self.variables = self.parent.variables.copy()
            self.level = (
                self.parent.level + 1
                if not self.n_type == NodeType.BLOCK_STATEMENT
                else self.parent.level
            )

    def get_or_generate_variable(self, generation_probability=0.5):
        if random.random() > generation_probability and self.variables:
            return random.choice(self.variables)
        return self._generate_variable_name()

    def _generate_variable_name(self):
        variable_name = f"X_{len(self.variables)}"
        p = self
        while p.n_type != NodeType.BLOCK_STATEMENT:
            p.variables.append(variable_name)
            p = p.parent
        p.variables.append(variable_name)
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
            case NodeType.MATH_EXPRESSION:
                return f'({self.children[0]} {self.attributes["operator"]} {self.children[1]})'
            case NodeType.BLOCK_STATEMENT:
                body = f'{"".join([(self.level - 1) * INDENT + str(child) for child in self.children])}'
                if self.is_root:
                    return body
                return "{\n" + body + (self.level - 1) * INDENT + "}\n"
            case NodeType.VAR:
                return f"{self.value}"
            case NodeType.INTEGER:
                return f"{self.value}"
            case NodeType.BOOLEAN:
                return f"{self.value}"
            case _:
                raise NotImplementedError(f"Node type: {self.n_type}")


class GenerationMethod(Enum):
    FULL = 0
    GROW = 1
    HALF_HALF = 2


@dataclass
class Program:
    max_depth: int = 0
    max_width: int = 1
    method: GenerationMethod = GenerationMethod.GROW
    max_iterations: int = 100
    min_integer: int = 0
    max_integer: int = 10
    root: Node = field(init=False)

    def __post_init__(self):
        if self.method == GenerationMethod.HALF_HALF:
            raise InvalidGenerationError(
                "Generation method HALF_HALF is used for population generation."
            )
        self.root = self._generate_program()

    def _generate_program(self):
        root = Node(NodeType.BLOCK_STATEMENT, is_root=True)
        if self.max_depth == 0:
            return root
        for _ in range(random.randint(1, self.max_width)):
            root.children.append(self._generate_instruction(root))
        return root

    def _calculate_depth(self, node):
        if len(node.children) == 0:
            return 1
        return 1 + max([self._calculate_depth(child) for child in node.children])

    def _generate_block_statement(self, parent):
        node = Node(NodeType.BLOCK_STATEMENT, parent=parent, level=parent.level + 1)
        for _ in range(random.randint(1, self.max_width)):
            node.children.append(self._generate_instruction(node))
        return node

    def _generate_instruction(self, parent):
        if self.method == GenerationMethod.GROW:
            instruction_types = [NodeType.ASSIGNMENT, NodeType.PRINT]
            if self.max_depth - parent.level > 0:
                instruction_types.extend([NodeType.LOOP, NodeType.IF])
        elif self.method == GenerationMethod.FULL:
            if self.max_depth - parent.level > 0:
                instruction_types = [NodeType.LOOP, NodeType.IF]
            else:
                instruction_types = [NodeType.ASSIGNMENT, NodeType.PRINT]
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
            attributes={"iterations": random.randint(1, self.max_iterations)},
        )
        node.children.append(self._generate_block_statement(node))
        return node

    def _generate_print(self, parent):
        node = Node(NodeType.PRINT, parent=parent, level=parent.level)
        node.children.append(
            self._generate_expression(node, var_generation_probability=0)
        )
        return node

    def _generate_if(self, parent):
        node = Node(
            NodeType.IF,
            parent=parent,
        )
        node.attributes = {"condition": self._generate_condition(node)}
        node.children.append(self._generate_block_statement(node))
        return node

    def _generate_condition_body(self, parent):
        node = Node(
            NodeType.CONDITION_BODY,
            parent=parent,
            attributes={"operator": random.choice(list(ComparisonOperator))},
        )
        node.children.append(
            self._generate_expression(node, var_generation_probability=0)
        )
        node.children.append(
            self._generate_expression(node, var_generation_probability=0)
        )  # excluding boolean
        return node

    def _generate_condition(self, parent):
        node = Node(NodeType.CONDITION, parent=parent)
        node.children.append(
            self._generate_condition_body(node)
        )  # excluding longer conditions
        return node

    def _generate_variable(self, parent, generation_probability=0.5):
        node = Node(NodeType.VAR, parent=parent)
        node.value = node.get_or_generate_variable(
            generation_probability=generation_probability
        )
        return node

    def _generate_assignment(self, parent):
        node = Node(NodeType.ASSIGNMENT, parent=parent)
        node.children.append(self._generate_variable(node))
        if random.random() < 0.5:
            node.children.append(self._generate_input(node))
        else:
            var = node.children[0]
            while var.value == node.children[0].value:
                var = self._generate_expression(node, var_generation_probability=0)
            node.children.append(var)
        return node

    def _generate_input(self, parent):
        node = Node(NodeType.INPUT, parent=parent)
        return node

    def _count_nested_expressions(self, node):
        nested_expressions = 0
        while node.parent:
            if node.n_type == NodeType.MATH_EXPRESSION:
                nested_expressions += 1
            node = node.parent
        return nested_expressions

    def _generate_expression(self, parent, var_generation_probability=0.5):
        expr_types = [NodeType.INTEGER]
        if parent.variables:
            expr_types.append(NodeType.VAR)
        if (
            self._count_nested_expressions(parent) < self.max_width
            and parent.level < self.max_depth
        ):
            expr_types.append(NodeType.MATH_EXPRESSION)
        _expr_type = random.choice(expr_types)
        if _expr_type == NodeType.VAR:
            return self._generate_variable(
                parent, generation_probability=var_generation_probability
            )
        elif _expr_type == NodeType.INTEGER:
            return self._generate_integer(parent)
        elif _expr_type == NodeType.MATH_EXPRESSION:
            return self._generate_math_expression(parent)

    def _generate_math_expression(self, parent):
        node = Node(
            NodeType.MATH_EXPRESSION,
            parent=parent,
            attributes={"operator": random.choice(list(ArithmeticOperator))},
        )
        node.children.append(self._generate_expression(node))
        node.children.append(self._generate_expression(node))
        return node

    def _generate_integer(self, parent):
        node = Node(
            NodeType.INTEGER,
            parent=parent,
            value=str(random.randint(self.min_integer, self.max_integer)),
        )
        return node

    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    program = Program(max_depth=3, max_width=3, method=GenerationMethod.FULL)
    print(program)