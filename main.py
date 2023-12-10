import pretty_errors # -> Output errors
import dearpygui.dearpygui as dpg
import Node

dpg.create_context()
dpg.create_viewport(title='Model Designer', width=900, height=850)

with dpg.window(
    tag="APP", 
    label="Main Window",
    pos = [0, 0],
    autosize=True,
    no_resize=True,
    no_move=True,
    no_collapse=True,
    no_scrollbar=True,
    no_close=True
):

    import menubar # Add menubar



    with dpg.node_editor(callback=lambda sender, app_data: dpg.add_node_link(app_data[0], app_data[1], parent=sender, tag="MainEditor"), 
                                delink_callback=lambda sender, app_data: dpg.delete_item(app_data), minimap=True, minimap_location=dpg.mvNodeMiniMap_Location_TopRight):

        # ADD DEFAULT NODE TO POP UP WHEN APP RUN
        Node.Temperature.block() 
        Node.Query.block()
        Node.LLM_Response.block()

    

    







dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("APP", True)
dpg.start_dearpygui()
dpg.destroy_context()