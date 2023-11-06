from converters import *

if __name__ == '__main__':
    window = Tk()
    window.resizable(False, False)
    window.geometry("550x300")
    window.iconphoto(False, PhotoImage(file="assets/icon.png"))
    window.title("Ultimate Unit Converter")

    categories_label = Label(window, text="Choose a category:")
    categories_label.pack(pady=10)

    categories = ttk.Notebook(window)
    categories.pack()

    # Copyright
    Label(window, text="© Maksym Petukhov").pack(pady=10)

    # Input category buttons
    length = ttk.Frame(categories)
    categories.add(length, text="Length")

    temperature = ttk.Frame(categories)
    categories.add(temperature, text="Temperature")

    area = Frame(categories)
    categories.add(area, text="Area")

    volume = Frame(categories)
    categories.add(volume, text="Volume")

    weight = Frame(categories)
    categories.add(weight, text="Weight")

    time = Frame(categories)
    categories.add(time, text="Time")

    # Windows
    length_window = Length(length)
    temperature_window = Temperature(temperature)
    area_window = Area(area)
    volume_window = Volume(volume)
    weight_window = Weight(weight)
    time_window = Time(time)

    # Start
    window.mainloop()
