from homework_6.src.task1_counter import instances_counter


@instances_counter
class TestCounter:
    pass


@instances_counter
class AdvanceTestCounter:
    print("in test class")
    some_attribute = "I'm in AdvanceTestCounter class"

    def __init__(self, something):
        print("in test init")
        self.something = something
        self.int_value = 1

    def some_method(self):
        return self.int_value + 1


@instances_counter
class ClassWithOneInit:
    # Class with __init__, that get only self
    def __init__(self):
        self.test = "It's work with one parameter in init (self)"


def test_initial_instances_of_class():
    assert TestCounter.get_created_instances() == 0


def test_initial_instances_of_counter_attr():
    assert TestCounter.counter == 0


def test_of_get_created_instances_function_on_instance():
    first, _, _ = TestCounter(), TestCounter(), TestCounter()

    assert first.get_created_instances() == 3


def test_of_reset_instances_counter_function():
    current_counter = TestCounter.reset_instances_counter()

    assert (current_counter == 3) and (TestCounter.counter == 0)


# Test of more complex classes (with there own init, attrs and methods)


def test_function_get_created_instances_on_complex_class():
    first = AdvanceTestCounter("first")
    second = AdvanceTestCounter("second")
    first_again = AdvanceTestCounter("first")

    assert first.get_created_instances() == 3


def test_function_reset_instances_counter_on_complex_class():
    current_counter = AdvanceTestCounter.reset_instances_counter()

    assert (current_counter == 3) and (AdvanceTestCounter.counter == 0)


def test_of_advanced_class_attr():
    some_instance = AdvanceTestCounter("something")
    assert some_instance.some_attribute == "I'm in AdvanceTestCounter class"


def test_of_advanced_class_method():
    some_instance = AdvanceTestCounter("something")
    assert some_instance.some_method() == 2


def test_of_advanced_class_init():
    some_instance = AdvanceTestCounter("something")
    assert some_instance.something == "something"


def test_of_one_param_in_init():
    some_instance = ClassWithOneInit()
    assert some_instance.test == "It's work with one parameter in init (self)"
