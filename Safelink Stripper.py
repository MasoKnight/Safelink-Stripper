from urllib.parse import unquote

def clean_text(input_text):
    # Step 1: Remove text between the first and second occurrences of "http"
    http_sections = input_text.split("http", 2)
    if len(http_sections) > 2:
        input_text = http_sections[0] + "http" + http_sections[2]

    # Step 2: Remove everything from "&data" onwards
    data_index = input_text.find("&data")
    if data_index != -1:
        input_text = input_text[:data_index]

    # Step 3: URL decode the cleaned text
    return unquote(input_text)

# Continuous input loop
if __name__ == "__main__":
    while True:
        input_text = input("\nPaste the safelink here (or type 'exit' to quit): ").strip()
        if input_text.lower() == "exit":
            print("Exiting program.")
            break

        cleaned_text = clean_text(input_text)
        print("\nCleaned and decoded text:\n")
        print(cleaned_text)
