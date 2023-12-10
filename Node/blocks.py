from dearpygui import dearpygui as dpg

class Temperature_Holder:


    name = "Temperature"
    value = 0.5

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[10, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_slider_float(
                    default_value=self.value,
                    width=175
                )




class Top_k_Holder:

    name = "Top_k"
    value = 40

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[0, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_slider_float(
                    default_value=self.value,
                    width=175
                )    

class Top_p_Holder:

    name = "Top_p"
    value = 0.9

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[20, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_slider_float(
                    default_value=self.value,
                    width=175
                )

    
class Min_p_Holder:

    name = "Min_p"
    value = None

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[30, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_slider_float(
                    default_value=self.value,
                    width=175
                )


class Prompt_Holder:

    name = "Prompt"
    default_prompt = True
    value = "Hello, how are you?"

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[40, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)
                if self.default_prompt:

                    dpg.add_input_text(
                        default_value=self.value,
                        width=400,
                        #height=400
                    )
                else:
                    self.value = ""
                    dpg.add_input_text(
                    width=400,
                    #height=400
                )
    

class Prompt_Template_Holder:

    name = "Prompt Template"
    value = ""

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[50, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_slider_float(
                    default_value=self.value,
                    width=175
                )


class Repeat_Penalty_Holder:

    name = "Repeat Penalty"
    value = "1.2"

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[60, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_slider_float(
                    default_value=self.value,
                    width=175
                )

    
class System_Prompt_Holder:

    name = "System Prompt"
    default_system_prompt = True
    value = "Helpful assistant"

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[70, 10],
        ):
            dpg.add_node_attribute(attribute_type=dpg.mvNode_Attr_Input)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)
                if self.default_system_prompt:

                    dpg.add_input_text(width=400, height=400, default_value=self.value)
                
                else:
                    dpg.add_input_text(width=400, height=400)


class Query_Holder:


    name = "User Query"
    value = "How to cook rice ?"

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[10, 50],
        ):

            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_input_text(
                    default_value=self.value,
                    width=500
                )

class LLM_Response_Holder:


    name = "LLM Response"
    value = "You can follow this simple step to cook some rice:\n"

    def block(self):
        with dpg.node(
            label=self.name, 
            parent='MainEditor',
            pos=[10, 50],
        ):

            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input):
                dpg.add_text(self.name)
                
                dpg.add_spacer(height=5)

                dpg.add_input_text(
                    default_value=self.value,
                    width=500
                )
    
    
Temperature = Temperature_Holder()
System_Prompt = System_Prompt_Holder()
Top_k = Top_k_Holder()
Top_p = Top_p_Holder
Min_p = Min_p_Holder()
Prompt = Prompt_Holder()
Repeat_Penalty = Repeat_Penalty_Holder()
Prompt_Template = Prompt_Template_Holder()
Query = Query_Holder()
LLM_Response = LLM_Response_Holder()