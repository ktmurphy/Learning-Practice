import justpy as jp


class About:

    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-grey h-screen")
        jp.Div(a=div, text="This is the About page!", classes= "text-4xl m-2")
        jp.Div(a=div, text="""
        A web app that lets users type in a term in a text box and returns the English definition
of that term instantly as soon as the user has finished typing.
The web app consists of a website with a navigation menu, a Home, Dictionary, and About page.
""", classes="text-lg")
        return wp

