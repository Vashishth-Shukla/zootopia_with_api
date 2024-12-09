# Zootopia with API

This project allows you to generate an HTML website displaying animal information fetched from the Animals API by API Ninja.

## Installation

1. Clone this repository to your local machine.
2. Create a `.env` file with your API key from API Ninja (as detailed below).
3. Install dependencies:

```bash
pip install -r requirements.txt


Usage
To generate a website with animal information:

Run the animals_web_generator.py script:
bash

python animals_web_generator.py
Enter the name of the animal (e.g., "Fox").

The website will be generated in the animals.html file.


Setup your API key
Go to API Ninja and sign up for an account.
Find your API key in the dashboard.
Create a .env file in the project root directory and add your API key:
plaintext
Copy code
API_KEY=your_api_key_here