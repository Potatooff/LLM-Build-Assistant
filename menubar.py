from dearpygui import dearpygui as dpg
import Node

with dpg.menu_bar(parent="APP"):
    with dpg.menu(tag="parameters", label="Model Settings"):

        
        # DEFAULT NODES
        dpg.add_menu_item(label=Node.Top_k.name, callback=Node.Top_k.block)
        dpg.add_menu_item(label=Node.Top_p.name)
        dpg.add_menu_item(label=Node.Min_p.name)
        dpg.add_menu_item(label=Node.System_Prompt.name)
        dpg.add_menu_item(label=Node.Prompt.name)
        dpg.add_menu_item(label=Node.Repeat_Penalty.name)
        dpg.add_menu_item(label=Node.Temperature.name)
        dpg.add_menu_item(label=Node.Prompt_Template.name)
        dpg.add_menu_item(label=Node.Query.name)
        dpg.add_menu_item(label=Node.LLM_Response.name)


        # ADD YOUR CUSTOM NODE HERE FOLLOWING THE SAME STRUCTURE

        

    with dpg.menu(tag="about", label="About"):

        # Information about app :)
        dpg.add_menu_item(label="Github Repository")
        dpg.add_menu_item(label="Version v0.1.0")
        dpg.add_menu_item(label="Author Potatooff")

    