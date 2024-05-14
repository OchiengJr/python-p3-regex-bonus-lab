def pytest_itemcollected(item):
    # Get the test class and test method objects
    test_class = item.parent.obj
    test_method = item.obj
    
    # Extract docstrings from the test class and test method, or default to class/method name
    class_doc = test_class.__doc__.strip() if test_class.__doc__ else test_class.__class__.__name__
    method_doc = test_method.__doc__.strip() if test_method.__doc__ else test_method.__name__
    
    # Concatenate the test class and test method names
    test_name = ' '.join([part for part in [class_doc, method_doc] if part])
    
    # Assign the concatenated name to the test item's nodeid
    item._nodeid = test_name
