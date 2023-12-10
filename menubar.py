from dearpygui import dearpygui as dpg

with dpg.menu_bar(parent="APP"):
    with dpg.menu(tag="parameters", label="Model Settings"):
        pass

    with dpg.menu(tag="about", label="About"):
        dpg.add_menu_item(label="Github Repository")
        dpg.add_menu_item(label="Version v0.1.0")
        dpg.add_menu_item(label="Author ...")
