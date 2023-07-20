## Setup Instructions

1. Create a Python 3.10 virtual environmen:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

2. Install the required dependencies using the provided requirements.txt file:
   ```
   pip install -r requirements.txt
   ```

3. Add your API key to the api.txt file:
   - Open the api_key.txt file in the root directory of the project.
   - Save the file.

4. Add your knowledge to the tigersheet.csv file:
   - Open the tigersheet.txt file in the root directory of the project.
   - Add your knowledge as text.
   - Save the file.

## Run the Application

To query knowledge from the Tigersheet file, run the main.py file:
```
python langchanin_qa_over_docs.py
```

The application will prompt you to enter a query, and it will display answer based on your input.

```
