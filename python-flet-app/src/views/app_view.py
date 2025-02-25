def create_view(page):
    page.title = "Hello Flet App"
    page.vertical_alignment = "center"
    
    greeting = flet.Text("Hello", size=40)
    page.add(greeting)