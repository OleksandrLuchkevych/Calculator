from functions import Calculator
import app_settings as ap
import memory as mh

def main():
    calculator = Calculator()
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Perform Calculation")
        print("2. Change Decimal Places")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")
        
        match choice:
            case '1':
                calculator.get_input()
                calculator.perform_operation()
                calculator.display_result()

                mh.handle_memory(calculator.result)

                if mh.show_history_prompt():
                    print(mh.show_history())

            case '2':
                ap.set_decimal_places()

            case '3':
                print("Exiting the calculator.")
                return

            case _:
                print("Invalid choice! Please try again.")

main()
