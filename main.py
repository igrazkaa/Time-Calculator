from time_calculator import add_time
from unittest import main

if __name__ == '__main__':
    print(add_time("9:15 PM", "5:30"))  # expected = "2:45 AM (next day)"
    print(add_time("11:59 PM", "24:05"))  # expected = "12:04 AM (2 days later)"
    print(add_time("9:15 PM", "5:30"))  # expected = "2:45 AM (next day)"
    print(add_time("11:40 AM", "0:25"))  # expected = "12:05 PM"

    # Run unit tests automatically
    main(module='test_module', exit=False)
