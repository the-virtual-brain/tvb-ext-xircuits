from argparse import Namespace
from typing import TypeVar, Generic, Tuple

from xai_components.logger.builder import get_logger

LOGGER = get_logger(__name__)

T = TypeVar('T')


class InArg(Generic[T]):
    value: T

    def __init__(self, value: T) -> None:
        self.value = value

    @classmethod
    def empty(cls):
        return InArg(None)


class OutArg(Generic[T]):
    value: T

    def __init__(self, value: T) -> None:
        self.value = value

    @classmethod
    def empty(cls):
        return OutArg(None)

class InCompArg(Generic[T]):
    value: T

    def __init__(self, value: T) -> None:
        self.value = value

    @classmethod
    def empty(cls):
        return InCompArg(None)


def xai_component(*args, **kwargs):
    # Passthrough element without any changes.
    # This is used for parser metadata only.
    if len(args) == 1 and callable(args[0]):
        # @xai_components form
        return args[0]
    else:
        # @xai_components(...) form
        def passthrough(f):
            return f
        return passthrough

class ExecutionContext:
    args: Namespace

    def __init__(self, args: Namespace):
        self.args = args


class BaseComponent:

    def __init__(self):
        all_ports = self.__annotations__
        for key, type_arg in all_ports.items():
            if isinstance(type_arg, InArg[any].__class__):
                setattr(self, key, InArg.empty())
            elif isinstance(type_arg, InCompArg[any].__class__):
                setattr(self, key, InCompArg.empty())
            elif isinstance(type_arg, OutArg[any].__class__):
                setattr(self, key, OutArg.empty())
            elif type_arg == str(self.__class__):
                setattr(self, key, None)

    @classmethod
    def set_execution_context(cls, context: ExecutionContext) -> None:
        cls.execution_context = context

    def execute(self, ctx) -> None:
        pass

    def do(self, ctx) -> Tuple[bool, 'BaseComponent']:
        pass


class Component(BaseComponent):
    next: BaseComponent
    done: bool

    def __init__(self):
        super().__init__()
        self.done = False

    def do(self, ctx) -> Tuple[bool, BaseComponent]:
        LOGGER.info(f"\nExecuting: {self.__class__.__name__}")
        self.execute(ctx)

        return self.done, self.next

    def debug_repr(self) -> str:
        return "<h1>Component</h1>"


class SubGraphExecutor:

    def __init__(self, component):
        self.comp = component

    def do(self, ctx):
        comp = self.comp

        while comp is not None:
            is_done, comp = comp.do(ctx)
        return is_done, None


def execute_graph(args: Namespace, start: BaseComponent, ctx) -> None:
    BaseComponent.set_execution_context(ExecutionContext(args))

    if 'debug' in args and args['debug']:
        import pdb
        pdb.set_trace()

        current_component = start
        next_component = current_component.do(ctx)
        while next_component:
            current_component = next_component
            next_component = current_component.do(ctx)
    else:
        next_component = start.do(ctx)
        while next_component:
            next_component = next_component.do(ctx)
