import itertools
import streamlit as st

def process_word(word, word_list):
    """
    Processes a word, generates permutations, and filters them against a word list.

    Args:
        word: The input word.
        word_list: A list of words to check against.

    Returns:
        A dictionary where keys are permutation lengths and values are lists of 
        valid permutations.
    """
    word_len = len(word)
    result_dict = {}

    for i in range(3, word_len + 1):
        permutations = set(itertools.permutations(word, i))
        filtered_permutations = ["".join(perm) for perm in permutations if "".join(perm) in word_list]
        result_dict[i] = sorted(filtered_permutations)
    
    return result_dict

# Load words from file
@st.cache_data
def load_word_list():
    try:
        with open("sowpods.txt", "r") as file:
            for _ in range(4):  # Skip the first four lines
                next(file)
            return {line.strip().lower() for line in file}
    except FileNotFoundError:
        st.error("Error: 'sowpods.txt' not found.")
        return set()

# Streamlit App
st.title("World of word Solutions")

word_list = load_word_list()
input_word = st.text_input("Enter your letters :").strip().lower()

if input_word:
    output = process_word(input_word, word_list)
    
    for key, value in output.items():
        if value:
            with st.expander(f"Words with {key} letters"):
                st.write(", ".join(value))
        else:
            st.write(f"No valid permutations found for length {key}.")
