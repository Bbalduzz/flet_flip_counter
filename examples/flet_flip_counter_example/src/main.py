import flet as ft
from flet_flip_counter import FlipCounter


def main(page: ft.Page):
    page.title = "AnimatedFlipCounter Demo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    current_value = 0.0
    
    counter1 = FlipCounter(
        value=current_value,
        text_style=ft.TextStyle(
            size=32
        ),
    )
    
    counter2 = FlipCounter(
        value=current_value,
        whole_digits=4,
        fraction_digits=2,
        hide_leading_zeroes=True,
        thousand_separator=",",
        text_style=ft.TextStyle(
            size=32,
            color=ft.colors.BLUE,
            weight=ft.FontWeight.BOLD
        ),
        duration_ms=1000,
        animation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT),
    )
    
    counter3 = FlipCounter(
        value=current_value,
        prefix="€ ",
        whole_digits=6,
        fraction_digits=2,
        thousand_separator=".",
        decimal_separator=",",
        text_style=ft.TextStyle(
            size=40,
            color=ft.colors.GREEN,
            shadow=ft.BoxShadow(
                blur_radius=4,
                color=ft.colors.YELLOW_100,
                offset=ft.Offset(2, 2)
            )
        ),
        duration_ms=800,
        animation=ft.animation.Animation(300, ft.AnimationCurve.ELASTIC_OUT),
    )
    
    def update_value(e, amount):
        nonlocal current_value
        current_value += amount
        
        counter1.value = current_value
        counter2.value = current_value
        counter3.value = current_value
        
        if current_value < 0:
            counter3.text_style.color = ft.colors.RED
        else:
            counter3.text_style.color = ft.colors.GREEN
        
        page.update()
    
    buttons_row = ft.Row(
        [
            ft.Column([
                ft.ElevatedButton(
                    text=f"+{amt}",
                    on_click=lambda e, amt=amt: update_value(e, amt)
                ),
                ft.ElevatedButton(
                    text=f"-{amt}",
                    on_click=lambda e, amt=amt: update_value(e, -amt)
                ),
            ]) 
            for amt in [0.01, 0.5, 1, 10, 100]
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
    )
    
    page.add(
        ft.Text("Simple Counter:", size=16),
        counter1,
        ft.Divider(height=20),
        
        ft.Text("Formatted Counter::", size=16),
        counter2,
        ft.Divider(height=20),
        
        ft.Text("Counter with prefix:", size=16),
        counter3,
        ft.Divider(height=40),
        
        buttons_row,
    )


ft.app(main)