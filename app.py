import solara
from model import SchellingModel
from mesa.visualization import (  
    SolaraViz,
    make_space_component,
    make_plot_component,
)
from mesa.visualization.components import AgentPortrayalStyle

## Define agent portrayal: color, shape, and size
def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color = "blue" if agent.type == 1 else "red",
        marker= "s",
        size= 75,
    )

## Enumerate variable parameters in model: seed, grid dimensions, population density, agent preferences, vision, and relative size of groups.
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": {
        "type": "SliderInt",
        "value": 30,
        "label": "Width",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 30,
        "label": "Height",
        "min": 5,
        "max": 100,
        "step": 1,
    },
    "density": {
        "type": "SliderFloat",
        "value": 0.7,
        "label": "Population Density",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    # Add sliders for the lower and upper bounds on the group's likeness thresholds
    "group_0_pref_min": {
        "type": "SliderFloat",
        "value": 0.1,
        "label": "Agent Type 0 likeness ratio minimum",
        "min": 0,
        "max": 1,
        "step": 0.1,
    },
    "group_0_pref_max": {
        "type": "SliderFloat",
        "value": 0.3,
        "label": "Agent Type 0 likeness ratio maximum",
        "min": 0,
        "max": 1,
        "step": 0.1,
    },
    "group_1_pref_min": {
        "type": "SliderFloat",
        "value": 0.6,
        "label": "Agent Type 1 likeness ratio minimum",
        "min": 0,
        "max": 1,
        "step": 0.1,
    },
    "group_1_pref_max": {
        "type": "SliderFloat",
        "value": 0.8,
        "label": "Agent Type 1 likeness ratio maximum",
        "min": 0,
        "max": 1,
        "step": 0.1,
    },
    "group_one_share": {
        "type": "SliderFloat",
        "value": 0.7,
        "label": "Share Type 1 Agents",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
    "radius": {
        "type": "SliderInt",
        "value": 1,
        "label": "Vision Radius",
        "min": 1,
        "max": 5,
        "step": 1,
    },
}

## Instantiate model
schelling_model = SchellingModel()

## Define happiness over time plot
HappyPlot = make_plot_component({"share_happy": "tab:green"})

## Define space component
SpaceGraph = make_space_component(agent_portrayal, draw_grid=False)

## Instantiate page inclusing all components
page = SolaraViz(
    schelling_model,
    components=[SpaceGraph, HappyPlot],
    model_params=model_params,
    name="Schelling Segregation Model",
)
## Return page
page
    
