import flet as ft
from views.app_view import create_view

def main(page: ft.Page):
    page.title = "I LOVE PYTHON ..... "
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    create_view(page)

ft.app(target=main)