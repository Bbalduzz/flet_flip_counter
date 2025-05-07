# Introduction

FletFlipCounter for Flet.

## Examples

```
import flet as ft

from flet_flip_counter import FletFlipCounter


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletFlipCounter(
                    tooltip="My new FletFlipCounter Control tooltip",
                    value = "My new FletFlipCounter Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[FletFlipCounter](FletFlipCounter.md)


