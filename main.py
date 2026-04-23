import flet as ft

def main(page: ft.Page):
    page.title = "Simple App"
    page.add(ft.Text("Hello from Python APK 🚀"))
    page.add(ft.ElevatedButton("Click me", on_click=lambda e: print("Clicked")))

ft.app(target=main)
