import justpy as jp
import definition


class Dictionary:

    path = "/dictionary"
    
    @classmethod
    def serve(cls, requestsOjb):
        # in previous line, cls is the same as self, but just cls to make it clear
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-grey-50 h-screen")
        jp.Div(a=div, text="Instant Dictionary", classes= "text-4xl m-2")
        jp.Div(a=div, text="Gets the definition of any English word instantly as you type.", classes="text-lg")
        
        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        #Input has a value component
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv = output_div,
                  classes="m-2, bg-gray-100 border-2 border-gray-200 rounded w-64 "
                  "focus:bg-white focus:outline-none focus:boarder-purple-500 "
                  "py-2 px-4")
        
        input_box.on('input', cls.get_definition)

        
        
        #send input_box to Button because this is the event handler
        #removing button to make it so as soon as the user finishes typing, we get the definition
        #leaving it in the code so I can reference later.
        #jp.Button(a=input_div, text="Get Definition", classes="border-2 text-gray-500", 
        #          click=cls.get_definition, outputdiv=output_div, inputbox=input_box)
         

        return wp
    
    @staticmethod
    def get_definition(widget, msg):
        #event handlers get a widget and msg parameter
        #widget gets as a value the value of the widget creating the event - input_box
        #value of widget is whatever people enter in input_box
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
