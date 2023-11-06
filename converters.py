from tkinter import *
from tkinter import ttk
from abc import ABC, abstractmethod


class Converter(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def convert(self):
        pass

    @abstractmethod
    def clear(self):
        pass


class Length(Converter):
    LENGTH_CONVERSIONS = {
        "mm": 1, "cm": 10, "m": 1000, "km": 1000000,
        "in": 25.4, "ft": 304.8, "yd": 914.4, "mi": 1609344
    }

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.render()

    def render(self):
        self.input = Entry(self.window, width=10)
        input_label = Label(self.window, text="From:")
        self.input_unit = ttk.Combobox(self.window, values=list(self.LENGTH_CONVERSIONS.keys()))
        self.output = Label(self.window, text="Output")
        output_label = Label(self.window, text="To:")
        self.output_unit = ttk.Combobox(self.window, values=list(self.LENGTH_CONVERSIONS.keys()))
        self.convert_button = Button(self.window, text="Convert", command=self.convert)
        self.clear_button = Button(self.window, text="Clear", command=self.clear)

        self.input.grid(row=0, column=0, padx=10, pady=10)
        input_label.grid(row=0, column=1, padx=10, pady=10)
        self.input_unit.grid(row=0, column=2, padx=10, pady=10)
        self.output.grid(row=1, column=0, padx=10, pady=10)
        output_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_unit.grid(row=1, column=2, padx=10, pady=10)
        self.convert_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            input_value = float(self.input.get())
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            if input_unit in self.LENGTH_CONVERSIONS and output_unit in self.LENGTH_CONVERSIONS:
                conversion_factor = self.LENGTH_CONVERSIONS[input_unit] / self.LENGTH_CONVERSIONS[output_unit]
                output_value = input_value * conversion_factor
            else:
                output_value = "Invalid unit"

            self.output.config(text=f"{output_value:.2f} {output_unit}")
        except ValueError:
            self.output.config(text="Invalid input")

    def clear(self):
        self.input.delete(0, END)
        self.output.config(text="Output")


class Temperature(Converter):
    UNITS = ["Celsius", "Fahrenheit", "Kelvin"]

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.render()

    def render(self):
        self.input = Entry(self.window, width=10)
        input_label = Label(self.window, text="From:")
        self.input_unit = ttk.Combobox(self.window, values=["Celsius", "Fahrenheit", "Kelvin"])
        self.output = Label(self.window, text="Output")
        output_label = Label(self.window, text="To:")
        self.output_unit = ttk.Combobox(self.window, values=["Celsius", "Fahrenheit", "Kelvin"])
        self.convert_button = Button(self.window, text="Convert", command=self.convert)
        self.clear_button = Button(self.window, text="Clear", command=self.clear)

        self.input.grid(row=0, column=0, padx=10, pady=10)
        input_label.grid(row=0, column=1, padx=10, pady=10)
        self.input_unit.grid(row=0, column=2, padx=10, pady=10)
        self.output.grid(row=1, column=0, padx=10, pady=10)
        output_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_unit.grid(row=1, column=2, padx=10, pady=10)
        self.convert_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            input_value = float(self.input.get())
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            if input_unit == "Celsius":
                if output_unit == "Fahrenheit":
                    output_value = input_value * 9 / 5 + 32
                elif output_unit == "Kelvin":
                    output_value = input_value + 273.15
                else:
                    output_value = input_value
            elif input_unit == "Fahrenheit":
                if output_unit == "Celsius":
                    output_value = (input_value - 32) * 5 / 9
                elif output_unit == "Kelvin":
                    output_value = (input_value - 32) * 5 / 9 + 273.15
                else:
                    output_value = input_value
            elif input_unit == "Kelvin":
                if output_unit == "Celsius":
                    output_value = input_value - 273.15
                elif output_unit == "Fahrenheit":
                    output_value = (input_value - 273.15) * 9 / 5 + 32
                else:
                    output_value = input_value
            else:
                output_value = "Invalid unit"

            self.output.config(text=f"{output_value:.2f} {output_unit}")
        except ValueError:
            self.output.config(text="Invalid input")

    def clear(self):
        self.input.delete(0, END)
        self.output.config(text="Output")


class Area(Converter):

    AREA_CONVERSIONS = {
        "Square Meters": {"Square Meters": 1, "Square Feet": 10.7639, "Square Yards": 1.19599,
                          "Square Miles": 3.861e-7},
        "Square Feet": {"Square Meters": 0.092903, "Square Feet": 1, "Square Yards": 0.111111,
                        "Square Miles": 2.2957e-8},
        "Square Yards": {"Square Meters": 0.836127, "Square Feet": 9, "Square Yards": 1, "Square Miles": 3.2283e-7},
        "Square Miles": {"Square Meters": 2590000, "Square Feet": 27878396.1, "Square Yards": 3097600,
                         "Square Miles": 1}
    }

    UNITS = ["Square Meters", "Square Feet", "Square Yards", "Square Miles"]

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.render()

    def render(self):
        self.input = Entry(self.window, width=10)
        input_label = Label(self.window, text="From:")
        self.input_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.output = Label(self.window, text="Output")
        output_label = Label(self.window, text="To:")
        self.output_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.convert_button = Button(self.window, text="Convert", command=self.convert)
        self.clear_button = Button(self.window, text="Clear", command=self.clear)

        self.input.grid(row=0, column=0, padx=10, pady=10)
        input_label.grid(row=0, column=1, padx=10, pady=10)
        self.input_unit.grid(row=0, column=2, padx=10, pady=10)
        self.output.grid(row=1, column=0, padx=10, pady=10)
        output_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_unit.grid(row=1, column=2, padx=10, pady=10)
        self.convert_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            input_value = float(self.input.get())
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            if input_unit in self.AREA_CONVERSIONS and output_unit in self.AREA_CONVERSIONS:
                conversion_factor = self.AREA_CONVERSIONS[input_unit][output_unit]
                output_value = input_value * conversion_factor
            else:
                output_value = "Invalid unit"
            self.output.config(text=f"{output_value:.2f} {output_unit}")
        except ValueError:
            self.output.config(text="Invalid input")

    def clear(self):
        self.input.delete(0, END)
        self.output.config(text="Output")


class Volume(Converter):

    VOLUME_CONVERSIONS = {
        "Cubic Meters": {"Cubic Meters": 1, "Cubic Feet": 35.3147, "Liters": 1000, "Gallons": 264.172},
        "Cubic Feet": {"Cubic Meters": 0.0283168, "Cubic Feet": 1, "Liters": 28.3168, "Gallons": 7.48052},
        "Liters": {"Cubic Meters": 0.001, "Cubic Feet": 0.0353147, "Liters": 1, "Gallons": 0.264172},
        "Gallons": {"Cubic Meters": 0.00378541, "Cubic Feet": 0.133681, "Liters": 3.78541, "Gallons": 1}
    }

    UNITS = ["Cubic Meters", "Cubic Feet", "Liters", "Gallons"]

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.render()

    def render(self):
        self.input = Entry(self.window, width=10)
        input_label = Label(self.window, text="From:")
        self.input_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.output = Label(self.window, text="Output")
        output_label = Label(self.window, text="To:")
        self.output_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.convert_button = Button(self.window, text="Convert", command=self.convert)
        self.clear_button = Button(self.window, text="Clear", command=self.clear)

        self.input.grid(row=0, column=0, padx=10, pady=10)
        input_label.grid(row=0, column=1, padx=10, pady=10)
        self.input_unit.grid(row=0, column=2, padx=10, pady=10)
        self.output.grid(row=1, column=0, padx=10, pady=10)
        output_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_unit.grid(row=1, column=2, padx=10, pady=10)
        self.convert_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            input_value = float(self.input.get())
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            if input_unit in self.VOLUME_CONVERSIONS and output_unit in self.VOLUME_CONVERSIONS:
                conversion_factor = self.VOLUME_CONVERSIONS[input_unit][output_unit]
                output_value = input_value * conversion_factor
            else:
                output_value = "Invalid unit"

            self.output.config(text=f"{output_value:.2f} {output_unit}")
        except ValueError:
            self.output.config(text="Invalid input")

    def clear(self):
        self.input.delete(0, END)
        self.output.config(text="Output")


class Weight(Converter):

    WEIGHT_CONVERSIONS = {
        "Kilograms": {"Kilograms": 1, "Pounds": 2.20462, "Ounces": 35.274, "Grams": 1000},
        "Pounds": {"Kilograms": 0.453592, "Pounds": 1, "Ounces": 16, "Grams": 453.592},
        "Ounces": {"Kilograms": 0.0283495, "Pounds": 0.0625, "Ounces": 1, "Grams": 28.3495},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.03527396, "Grams": 1}
    }

    UNITS = ["Kilograms", "Pounds", "Ounces", "Grams"]

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.render()

    def render(self):
        self.input = Entry(self.window, width=10)
        input_label = Label(self.window, text="From:")
        self.input_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.output = Label(self.window, text="Output")
        output_label = Label(self.window, text="To:")
        self.output_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.convert_button = Button(self.window, text="Convert", command=self.convert)
        self.clear_button = Button(self.window, text="Clear", command=self.clear)

        self.input.grid(row=0, column=0, padx=10, pady=10)
        input_label.grid(row=0, column=1, padx=10, pady=10)
        self.input_unit.grid(row=0, column=2, padx=10, pady=10)
        self.output.grid(row=1, column=0, padx=10, pady=10)
        output_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_unit.grid(row=1, column=2, padx=10, pady=10)
        self.convert_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            input_value = float(self.input.get())
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            if input_unit in self.WEIGHT_CONVERSIONS and output_unit in self.WEIGHT_CONVERSIONS:
                conversion_factor = self.WEIGHT_CONVERSIONS[input_unit][output_unit]
                output_value = input_value * conversion_factor
            else:
                output_value = "Invalid unit"

            self.output.config(text=f"{output_value:.2f} {output_unit}")
        except ValueError:
            self.output.config(text="Invalid input")

    def clear(self):
        self.input.delete(0, END)
        self.output.config(text="Output")

class Time(Converter):

    TIME_CONVERSIONS = {
        "Seconds": {"Seconds": 1, "Minutes": 0.0166667, "Hours": 0.000277778, "Days": 1.15741e-5},
        "Minutes": {"Seconds": 60, "Minutes": 1, "Hours": 0.0166667, "Days": 0.000694444},
        "Hours": {"Seconds": 3600, "Minutes": 60, "Hours": 1, "Days": 0.0416667},
        "Days": {"Seconds": 86400, "Minutes": 1440, "Hours": 24, "Days": 1}
    }

    UNITS = ["Seconds", "Minutes", "Hours", "Days"]

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.render()

    def render(self):
        self.input = Entry(self.window, width=10)
        input_label = Label(self.window, text="From:")
        self.input_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.output = Label(self.window, text="Output")
        output_label = Label(self.window, text="To:")
        self.output_unit = ttk.Combobox(self.window, values=self.UNITS)
        self.convert_button = Button(self.window, text="Convert", command=self.convert)
        self.clear_button = Button(self.window, text="Clear", command=self.clear)

        self.input.grid(row=0, column=0, padx=10, pady=10)
        input_label.grid(row=0, column=1, padx=10, pady=10)
        self.input_unit.grid(row=0, column=2, padx=10, pady=10)
        self.output.grid(row=1, column=0, padx=10, pady=10)
        output_label.grid(row=1, column=1, padx=10, pady=10)
        self.output_unit.grid(row=1, column=2, padx=10, pady=10)
        self.convert_button.grid(row=2, column=0, padx=10, pady=10)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def convert(self):
        try:
            input_value = float(self.input.get())
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            if input_unit in self.TIME_CONVERSIONS and output_unit in self.TIME_CONVERSIONS:
                conversion_factor = self.TIME_CONVERSIONS[input_unit][output_unit]
                output_value = input_value * conversion_factor
            else:
                output_value = "Invalid unit"

            self.output.config(text=f"{output_value:.2f} {output_unit}")
        except ValueError:
            self.output.config(text="Invalid input")

    def clear(self):
        self.input.delete(0, END)
        self.output.config(text="Output")
