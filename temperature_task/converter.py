from temperature_task.scale import Scale


class Converter:
    @staticmethod
    def convert_celsius_temperature(temperature, result):
        result[Scale.CELSIUS] = temperature
        result[Scale.KELVIN] = temperature + 273.15
        result[Scale.FAHRENHEIT] = temperature * 1.8 + 32

    @staticmethod
    def convert_kelvin_temperature(temperature, result):
        result[Scale.CELSIUS] = temperature - 273.15
        result[Scale.KELVIN] = temperature
        result[Scale.FAHRENHEIT] = 1.8 * temperature - 459.67

    @staticmethod
    def convert_fahrenheit_temperature(temperature, result):
        result[Scale.CELSIUS] = (temperature - 32) / 1.8
        result[Scale.KELVIN] = (temperature - 32) / 1.8 + 273.15
        result[Scale.FAHRENHEIT] = temperature

    def convert(self, input_temperature, input_scale):
        result = {scale: 0 for scale in list(Scale)}

        if input_scale == Scale.CELSIUS:
            self.convert_celsius_temperature(input_temperature, result)

        if input_scale == Scale.KELVIN:
            self.convert_kelvin_temperature(input_temperature, result)

        if input_scale == Scale.FAHRENHEIT:
            self.convert_fahrenheit_temperature(input_temperature, result)

        return result
