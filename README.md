# world_of_word
This is a Streamlit app that generates valid word permutations from a given input word. The permutations are filtered against the SOWPODS word list to ensure correctness.

## Features

Generates combination of a given word for lengths 3 and above.

Filters permutations against a valid English word list.

Displays different sections for 3-letter, 4-letter, etc., words.

User-friendly Streamlit interface.

## Data Source

The word list used in this project is sourced from:
SOWPODS Word List

## Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/word-permutations-app.git
cd word-permutations-app

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Streamlit App Locally

- streamlit run app.py

- This will open the app in your browser at http://localhost:8501.

- Deployment to Streamlit Cloud

- Push the repository to GitHub:

- git add .
- git commit -m "Initial commit for Streamlit app"
- git push origin main

- Go to Streamlit Cloud.

- Click New App and select your GitHub repository.

- Set the App file path to app.py and click Deploy.

Your app will be live, and Streamlit Cloud will update it automatically when you push changes.

## Contributing

Feel free to fork the repository, open issues, and submit pull requests.

## License

This project is open-source and available under the MIT License.

