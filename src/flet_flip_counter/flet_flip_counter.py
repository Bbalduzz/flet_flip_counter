from typing import Any, Optional, Union

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber
from flet.core.types import PaddingValue
from flet.core.animation import Animation
from flet.core.text_style import TextStyle
from flet.core.ref import Ref


class FlipCounter(ConstrainedControl):
    """
    FletFlipCounter Control - Un contatore animato che mostra transizioni fluide tra numeri.
    Basato sul pacchetto Flutter 'animated_flip_counter'.
    """

    def __init__(
        self,
        value: float = 0.0,
        duration_ms: int = 300,
        animation: Optional[Animation] = None,
        whole_digits: Optional[int] = None,
        fraction_digits: Optional[int] = None,
        hide_leading_zeroes: Optional[bool] = None,
        thousand_separator: Optional[str] = None,
        decimal_separator: Optional[str] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        infix: Optional[str] = None,
        padding: Optional[PaddingValue] = None,
        text_style: Optional[TextStyle] = None,
        
        # Proprietà di Control
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        
        # Proprietà di ConstrainedControl
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        self.value = value
        self.duration_ms = duration_ms
        self.animation = animation
        self.whole_digits = whole_digits
        self.fraction_digits = fraction_digits
        self.hide_leading_zeroes = hide_leading_zeroes
        self.thousand_separator = thousand_separator
        self.decimal_separator = decimal_separator
        self.prefix = prefix
        self.suffix = suffix
        self.infix = infix
        self.padding = padding
        self.text_style = text_style

    def _get_control_name(self):
        return "flet_flip_counter"

    # value
    @property
    def value(self) -> float:
        return self._get_attr("value", data_type="float", def_value=0.0)

    @value.setter
    def value(self, value: float):
        self._set_attr("value", value)

    # duration_ms
    @property
    def duration_ms(self) -> int:
        return self._get_attr("duration_ms", data_type="int", def_value=300)

    @duration_ms.setter
    def duration_ms(self, value: int):
        self._set_attr("duration_ms", value)

    # animation
    @property
    def animation(self) -> Optional[Animation]:
        return self._get_attr("animation")

    @animation.setter
    def animation(self, value: Optional[Animation]):
        self._set_attr_json("animation", value)

    # whole_digits
    @property
    def whole_digits(self) -> Optional[int]:
        return self._get_attr("whole_digits", data_type="int")

    @whole_digits.setter
    def whole_digits(self, value: Optional[int]):
        self._set_attr("whole_digits", value)

    # fraction_digits
    @property
    def fraction_digits(self) -> Optional[int]:
        return self._get_attr("fraction_digits", data_type="int")

    @fraction_digits.setter
    def fraction_digits(self, value: Optional[int]):
        self._set_attr("fraction_digits", value)

    # hide_leading_zeroes
    @property
    def hide_leading_zeroes(self) -> Optional[bool]:
        return self._get_attr("hide_leading_zeroes", data_type="bool")

    @hide_leading_zeroes.setter
    def hide_leading_zeroes(self, value: Optional[bool]):
        self._set_attr("hide_leading_zeroes", value)

    # thousand_separator
    @property
    def thousand_separator(self) -> Optional[str]:
        return self._get_attr("thousand_separator")

    @thousand_separator.setter
    def thousand_separator(self, value: Optional[str]):
        self._set_attr("thousand_separator", value)

    # decimal_separator
    @property
    def decimal_separator(self) -> Optional[str]:
        return self._get_attr("decimal_separator")

    @decimal_separator.setter
    def decimal_separator(self, value: Optional[str]):
        self._set_attr("decimal_separator", value)

    # prefix
    @property
    def prefix(self) -> Optional[str]:
        return self._get_attr("prefix")

    @prefix.setter
    def prefix(self, value: Optional[str]):
        self._set_attr("prefix", value)

    # suffix
    @property
    def suffix(self) -> Optional[str]:
        return self._get_attr("suffix")

    @suffix.setter
    def suffix(self, value: Optional[str]):
        self._set_attr("suffix", value)

    # infix
    @property
    def infix(self) -> Optional[str]:
        return self._get_attr("infix")

    @infix.setter
    def infix(self, value: Optional[str]):
        self._set_attr("infix", value)

    # padding
    @property
    def padding(self) -> Optional[PaddingValue]:
        return self._get_attr("padding")

    @padding.setter
    def padding(self, value: Optional[PaddingValue]):
        self._set_attr("padding", value)

    # text_style
    @property
    def text_style(self) -> Optional[TextStyle]:
        return self.__text_style

    @text_style.setter
    def text_style(self, value: Optional[TextStyle]):
        self.__text_style = value
        self._set_attr_json("textStyle", value)