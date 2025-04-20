import flet as ft

# from about import about

def main(page:ft.Page):
    page.title = "multiservice-git"
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    menubar = ft.MenuBar(
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                # on_open=handle_submenu_open,
                # on_close=handle_submenu_close,
                # on_hover=handle_submenu_hover,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("About"),
                        leading=ft.Icon(ft.Icons.INFO),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        # on_click=handle_menu_item_click,
                    ),
                ]
            )
        ]
    )

    upper_menu = ft.Row([menubar])

    page.add(
        ft.Container(height=20, content=upper_menu,),
    )

if __name__ == "__main__":
    ft.app(target=main)
