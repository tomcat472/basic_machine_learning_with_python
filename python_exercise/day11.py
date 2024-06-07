## ternary operators
# def main():
#     val=8
#     text="Condition is true" if val < 4 else "Condition is false"
#     print(text)
#     print()
#     print("Hello" if val == 5 else "Goodbye")
# main()
# ___________________________________________________________________________
# def greet():
#     print("Hello")
#     print(1/0)

# def main():
#     try:
#         greet()
#     except:
#         print("something went wrong")
# main()
# ___________________________________________________________________________
# def do_greet():
#     greet()

# def greet():
#     print("Hello")
#     print(1/0)
    
# def main():
#     try:
#         do_greet()
#     except:
#         print("something went wrong")
# main()
# ___________________________________________________________________________
# def do_greet():
#     d=dict()
#     print(d["hello"])
#     greet()
    
# def greet():
#     print("Hello")
#     print(1/0)
    
# def main():
#     try:
#         do_greet()
#     # except ZeroDivisionError:
#     #     print("Tried to divided by Zero")
#     except ZeroDivisionError as zde:
#         print(f"Error: {zde}")
#     # except KeyError :
#     #     print("A key error occured")
#     except KeyError as ke :
#         print(f"key error: {ke}")
#     except:
#         print("something unknown error occurred")

# main()
# # __________________________________________________________________________
# def do_greet():
#     d=dict()
#     # raise KeyError("not a real key error")
#     greet()
    
# def greet():
#     print("Hello")
#     print(1/0)
    
# def main():
#     try:
#         do_greet()
#     except Exception as e:
#         print(f"General error: {e}")
#     except ZeroDivisionError as zde:
#         print(f"Error: {zde}")
#     except KeyError as ke :
#         print(f"key error: {ke}")
#     except:
#         print("something unknown error occurred")

# main()
# ___________________________________________________________________
# def do_greet():
#     d=dict()
#     # raise KeyError("not a real key error")
#     greet()
    
# def greet():
#     print("Hello")
#     print(1/0)
    
# def main():
#     try:
#         while True:
#             print("Hello")
#         do_greet()
#     except Exception as e:
#         print(f"General error: {e}")
#     except ZeroDivisionError as zde:
#         print(f"Error: {zde}")
#     except KeyError as ke :
#         print(f"key error: {ke}")
#     except KeyboardInterrupt:
#         print("Keyboard interrupt: program ending")
#     except:
#         print("something unknown error occurred")
# main()
# ___________________________________________________________________
# def main():
#     try:
#         pass
#     except (ZeroDivisionError,KeyError) as e:
#         print(e)
#     else:
#         print("No exception occured")
#     finally:
#         print("finally was executed")
# main()
# ___________________________________________________________________
# def feet_to_miles(feet):
#     return feet * 1.89E-4

# def main():
#     while True:
#         feet=input("Enter distance in feet > ")
    
#         if feet == "quit":
#             break
        
#         try:
#             feet=feet.replace(",","")
#             miles=feet_to_miles(int(feet))
#             print(f"{feet} is equivalent to {miles:.3f}")
#             break
#         except:
#             print("Invalid input.")
# main()
# _____________________________________________________________________________________
def divide(a, b):
    # Assert that the denominator is not zero
    assert b != 0, "Denominator cannot be zero"
    return a / b

def test_divide():
    # Test with normal values
    assert divide(10, 2) == 5, "Test case 1 failed"
    
    # Test with negative values
    assert divide(-10, 2) == -5, "Test case 2 failed"
    
    # Test with float values
    assert divide(9, 0.5) == 18, "Test case 3 failed"
    
    # Test with zero numerator
    assert divide(0, 5) == 0, "Test case 4 failed"
    
    print("All test cases pass")

# Run the test cases
test_divide()


# divide(10, 0)  # This will raise an AssertionError
# with the message "Denominator cannot be zero"
