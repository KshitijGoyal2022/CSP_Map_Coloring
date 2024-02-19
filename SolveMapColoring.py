from AC3MRVLCVMapSolver import AC3MRVLCVMapSolver
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import geopandas as gpd
import matplotlib.pyplot as plt

def get_user_color_choices():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    color_choices = simpledialog.askstring("Color Choices", "Enter colors separated by commas (e.g., red,green,blue,yellow):")
    if color_choices:
        colors = {color.strip() for color in color_choices.split(",")}
        return colors
    else:
        messagebox.showinfo("Info", "No colors were entered. Using default colors.")
        return {"red", "green", "blue", "yellow"}  # Default colors

def get_user_country_choice():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Define the list of options
    options = ['Germany', 'France', 'Rwanda']
    country = simpledialog.askstring("Country Choice", "Enter a country (Germany, France, Rwanda):")
    if country and country.capitalize() in options:
        return country.capitalize()
    else:
        messagebox.showinfo("Info", "Invalid choice or no country was entered. Please enter one of the specific options.")
        return None


color_choices = get_user_color_choices()
print(color_choices)
country_choice = get_user_country_choice()
print(country_choice)


if country_choice == "Germany":
    neighbors = {
        "Schleswig-Holstein": ["Hamburg", "Mecklenburg-Vorpommern", "Niedersachsen"],
        "Hamburg": ["Schleswig-Holstein", "Niedersachsen"],
        "Mecklenburg-Vorpommern": ["Brandenburg", "Sachsen-Anhalt", "Niedersachsen"],
        "Bremen": ["Niedersachsen"],
        "Nordrhein-Westfalen": ["Niedersachsen", "Hessen", "Rheinland-Pfalz"],
        "Brandenburg": ["Berlin", "Mecklenburg-Vorpommern", "Sachsen-Anhalt", "Sachsen", "Niedersachsen"],
        "Hessen": ["Nordrhein-Westfalen", "Rheinland-Pfalz", "Baden-Württemberg", "Bayern", "Thüringen",
                   "Niedersachsen"],
        "Rheinland-Pfalz": ["Saarland", "Hessen", "Nordrhein-Westfalen", "Baden-Württemberg"],
        "Bayern": ["Baden-Württemberg", "Hessen", "Thüringen", "Sachsen"],
        "Saarland": ["Rheinland-Pfalz"],
        "Thüringen": ["Hessen", "Bayern", "Sachsen", "Sachsen-Anhalt", "Niedersachsen"],
        "Sachsen": ["Brandenburg", "Sachsen-Anhalt", "Thüringen", "Bayern"],
        "Niedersachsen": ["Bremen", "Hamburg", "Schleswig-Holstein", "Sachsen-Anhalt", "Thüringen", "Hessen",
                          "Nordrhein-Westfalen", "Mecklenburg-Vorpommern", "Brandenburg"],
        "Baden-Württemberg": ["Bayern", "Hessen", "Rheinland-Pfalz"],
        "Berlin": ["Brandenburg"]
    }  # German neighbors dictionary
    states = {
        "Schleswig-Holstein": None,
        "Hamburg": None,
        "Mecklenburg-Vorpommern": None,
        "Bremen": None,
        "Nordrhein-Westfalen": None,
        "Brandenburg": None,
        "Hessen": None,
        "Rheinland-Pfalz": None,
        "Bayern": None,
        "Saarland": None,
        "Thüringen": None,
        "Sachsen": None,
        "Niedersachsen": None,
        "Baden-Württemberg": None,
        "Berlin": None,
        "Sachsen-Anhalt": None
    }  # German states dictionary
elif country_choice == "France":
    neighbors = {
        "Auvergne-Rhône-Alpes": ["Bourgogne-Franche-Comté", "Occitanie", "Provence-Alpes-Côte d'Azur",
                                 "Nouvelle-Aquitaine"],
        "Bourgogne-Franche-Comté": ["Auvergne-Rhône-Alpes", "Centre-Val de Loire", "Grand Est", "Île-de-France",
                                    "Nouvelle-Aquitaine"],
        "Bretagne": ["Normandie", "Pays de la Loire"],
        "Centre-Val de Loire": ["Bourgogne-Franche-Comté", "Nouvelle-Aquitaine", "Pays de la Loire", "Île-de-France"],
        "Corse": [],
        "Grand Est": ["Bourgogne-Franche-Comté", "Hauts-de-France", "Île-de-France", "Auvergne-Rhône-Alpes"],
        "Hauts-de-France": ["Normandie", "Île-de-France", "Grand Est"],
        "Île-de-France": ["Hauts-de-France", "Normandie", "Centre-Val de Loire", "Bourgogne-Franche-Comté",
                          "Grand Est"],
        "Normandie": ["Bretagne", "Hauts-de-France", "Île-de-France", "Pays de la Loire"],
        "Nouvelle-Aquitaine": ["Occitanie", "Auvergne-Rhône-Alpes", "Centre-Val de Loire", "Bourgogne-Franche-Comté"],
        "Occitanie": ["Nouvelle-Aquitaine", "Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur"],
        "Pays de la Loire": ["Bretagne", "Centre-Val de Loire", "Normandie"],
        "Provence-Alpes-Côte d'Azur": ["Auvergne-Rhône-Alpes", "Occitanie"]
    }  # French neighbors dictionary
    states = {
        "Auvergne-Rhône-Alpes": None,
        "Bourgogne-Franche-Comté": None,
        "Bretagne": None,
        "Centre-Val de Loire": None,
        "Corse": None,
        "Grand Est": None,
        "Hauts-de-France": None,
        "Île-de-France": None,
        "Normandie": None,
        "Nouvelle-Aquitaine": None,
        "Occitanie": None,
        "Pays de la Loire": None,
        "Provence-Alpes-Côte d'Azur": None
    }  # French states dictionary
elif country_choice == "Rwanda":
    neighbors = {
        "Kigali City": ["Northern Province, Rwanda", "Southern Province, Rwanda", "East Province"],
        "East Province": ["Kigali City", "Northern Province, Rwanda", "Southern Province, Rwanda"],
        "Western Province, Rwanda": ["Southern Province, Rwanda", "Northern Province, Rwanda"],
        "Southern Province, Rwanda": ["Western Province, Rwanda", "Northern Province, Rwanda", "Kigali City",
                                      "East Province"],
        "Northern Province, Rwanda": ["Kigali City", "East Province", "Southern Province, Rwanda",
                                      "Western Province, Rwanda"]
    }  # Rwandan neighbors dictionary
    states = {
        "Kigali City": None,
        "East Province": None,
        "Western Province, Rwanda": None,
        "Southern Province, Rwanda": None,
        "Northern Province, Rwanda": None
    }  # Rwandan states dictionary
else:
    neighbors = {}
    states = {}

# Continue with the rest of your code using the selected neighbors and states
sol = AC3MRVLCVMapSolver()
sol.solveMapColoring(country_choice=country_choice,states=states, neighbors=neighbors, color_choices=color_choices)



