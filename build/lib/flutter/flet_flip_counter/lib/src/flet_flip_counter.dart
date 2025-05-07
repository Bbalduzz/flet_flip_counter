import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:animated_flip_counter/animated_flip_counter.dart';

class FlipCounterControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const FlipCounterControl({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    final value = control.attrDouble("value", 0.0)!;
    final durationMs = control.attrInt("duration_ms", 300)!;
    final duration = Duration(milliseconds: durationMs);
    
    final animationDetails = parseAnimation(control, "animation");
    final curve = animationDetails?.curve ?? Curves.linear;
    
    final textStyle = parseTextStyle(Theme.of(context), control, "textStyle") ?? 
        Theme.of(context).textTheme.bodyLarge;
    
    final wholeDigits = control.attrInt("whole_digits", 1);
    final fractionDigits = control.attrInt("fraction_digits", 0);
    final hideLeadingZeroes = control.attrBool("hide_leading_zeroes", false)!;
    final thousandSeparator = control.attrString("thousand_separator", "");
    final decimalSeparator = control.attrString("decimal_separator", ".");
    final prefix = control.attrString("prefix", "");
    final suffix = control.attrString("suffix", "");
    final infix = control.attrString("infix", "");
    
    EdgeInsets padding;
    var paddingValue = control.attrDouble("padding");
    if (paddingValue != null) {
      padding = EdgeInsets.all(paddingValue);
    } else {
      padding = const EdgeInsets.all(0);
    }
    
    Widget myControl = AnimatedFlipCounter(
      value: value,
      duration: duration,
      curve: curve,
      textStyle: textStyle,
      wholeDigits: wholeDigits ?? 1,
      fractionDigits: fractionDigits ?? 0,
      hideLeadingZeroes: hideLeadingZeroes,
      thousandSeparator: thousandSeparator,
      decimalSeparator: decimalSeparator ?? ".",
      prefix: prefix,
      suffix: suffix,
      infix: infix,
      padding: padding,
    );

    return constrainedControl(context, myControl, parent, control);
  }
}