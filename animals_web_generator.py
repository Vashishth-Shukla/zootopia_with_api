from dotenv import load_dotenv
from jinja2 import Template

import data_fetcher

# Load the environment variables from the .env file
load_dotenv()


def generate_website(animal_name, animal_data):
    """
    Generates an HTML website displaying the animal information.
    The template is now an external HTML file.
    """
    # Read the template from the file
    with open("templates/animal_template.html", "r") as file:
        html_template = file.read()

    # Create a Template instance and render it with the animal data
    template = Template(html_template)
    rendered_html = template.render(animal_name=animal_name, animal_data=animal_data)

    # Save the generated HTML to a file
    with open("animals.html", "w") as file:
        file.write(rendered_html)


def main():
    """
    Main function that interacts with the user to fetch animal data,
    generate an HTML page, and save it to a file.
    """
    animal_name = input("Please enter an animal: ")
    animal_data = data_fetcher.fetch_data(animal_name)

    # Ensure characteristics is a dictionary (if available)
    if animal_data:
        for animal in animal_data:
            # Check if 'characteristics' exists and is a dictionary
            if isinstance(animal.get("characteristics"), dict):
                pass  # It's already in the right format
            else:
                animal["characteristics"] = {}  # Default to empty if not a dictionary

    generate_website(animal_name, animal_data)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
