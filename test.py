import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoJSON file with German states
# Make sure to replace 'path_to_german_states_geojson' with the actual path to your GeoJSON file
german_states = gpd.read_file('path_to_german_states_geojson.json')
def ColorCountry(states_colors):
# Prepare the figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))

    # Plot each state with its corresponding color
    for state, color in states_colors.items():
        german_states[german_states['name'].str.upper() == state.upper()].plot(ax=ax, color=color, edgecolor='black')

    # Remove axis off
    ax.set_axis_off()

    plt.title('Map of Germany with States')
    plt.show()

# ColorCountry(states_colors)