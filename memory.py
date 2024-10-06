from app_settings import get_decimal_places  # Import the function

memory_value = 0
history_file_path = './source/history_log.txt'

def store(value):
    global memory_value
    memory_value = round(value, get_decimal_places())

def add_to_memory(value):
    global memory_value
    memory_value = round(memory_value + value, get_decimal_places())

def clear_memory():
    global memory_value
    memory_value = 0

def recall_memory():
    return memory_value

def log_history(first_operand, operator, second_operand, result):
    entry = f"{first_operand} {operator} {second_operand} = {result}\n"
    
    with open(history_file_path, 'a') as file:
        file.write(entry)

def show_history():
    try:
        with open(history_file_path, 'r') as file:
            print("\n--- Calculation History ---")
            print(file.read())
    except FileNotFoundError:
        print("No history available.")

def handle_memory(result):
    choice = input("Would you like to store result in memory (MS), add to memory (M+), clear memory (MC), or skip? ").upper()
    match choice:
        case 'MS':
            store(result)
            print(f"Stored {round(result, get_decimal_places())} in memory.")
        case 'M+':
            add_to_memory(result)
            print(f"Added {round(result, get_decimal_places())} to memory. New memory value: {recall_memory()}")
        case 'MC':
            clear_memory()
            print("Memory cleared.")
        case _:
            print("No memory operation performed.")

def show_history_prompt():
    return input("Do you want to view history? (y/n): ").strip().lower() == 'y'
