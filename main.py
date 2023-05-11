import pandas as pd
import keyboard


def read_csv_database(csv_file):
    """
    Reads the CSV database and returns it as a pandas DataFrame.
    """
    return pd.read_csv(csv_file)


def find_corresponding_value(database, selected_text):
    """
    Searches for the selected text in the database and returns the corresponding value.
    """
    row = database[database['Text'] == selected_text]
    if not row.empty:
        return row['Value'].values[0]
    else:
        return None


def main():
    # Specify the path to your CSV database file
    csv_file = 'path/to/database.csv'
    database = read_csv_database(csv_file)

    # Define the keyboard shortcut that triggers the script
    shortcut = 'ctrl+shift+c'

    # Register the keyboard shortcut
    keyboard.add_hotkey(shortcut, lambda: on_hotkey(database))

    # Wait for the user to press the keyboard shortcut
    keyboard.wait()


def on_hotkey(database):
    # Copy the selected text
    keyboard.press_and_release('cmd+c')

    # Access the clipboard contents
    selected_text = clipboard.paste()

    # Find the corresponding value in the database
    corresponding_value = find_corresponding_value(database, selected_text)

    if corresponding_value:
        # Copy the corresponding value
        clipboard.copy(corresponding_value)

        # Perform a tab keypress (to change the field in a form)
        keyboard.press_and_release('tab')
    else:
        print('Selected text not found in the database.')


if __name__ == '__main__':
    main()
