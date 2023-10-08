# workflow

import pytest

from src.simple_queue import Queue

"""
methods

- enqueue(element)
- dequeue(element)
- peek()
- isEmpty()
- size()

"""

@pytest.fixture
def my_queue():
    return Queue()

def test_queue_initial_state(my_queue):
    assert my_queue.is_empty()

def test_enqueue(my_queue):
    my_queue.enqueue("Jhon Doe")
    my_queue.enqueue("Jackson")
    assert my_queue.size() == 2

def test_enqueue_dequeue(my_queue):
    my_queue.enqueue("Jhon Doe")
    my_queue.enqueue("Jackson")
    my_queue.dequeue()
    
    assert my_queue.size() == 1
    assert my_queue.peek() == "Jackson"

def test_clear_queue(my_queue):
    my_queue.enqueue("Jhon Doe")
    my_queue.enqueue("Jackson")
    
    my_queue.clear()

    assert my_queue.is_empty()

def test_dequeue_empty_queue(my_queue):
    with pytest.raises(Exception) as excp:
        my_queue.dequeue()
    assert str(excp.value) == "Queue is empty"
    assert my_queue.is_empty()

def test_peek_empty_queue(my_queue):
    assert my_queue.peek() == -1