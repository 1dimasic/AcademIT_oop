from temperature_task.scale import Scale


class Converter:
    @staticmethod
    def convert_celsius_kelvin_temperature(temperature, reverse=False):
        if not reverse:
            return temperature + 273.15

        return temperature - 273.15

    @staticmethod
    def convert_celsius_fahrenheit_temperature(temperature, reverse=False):
        if not reverse:
            return temperature * 1.8 + 32

        return (temperature - 32) / 1.8

    @staticmethod
    def convert_kelvin_fahrenheit_temperature(temperature, reverse=False):
        if not reverse:
            return 1.8 * temperature - 459.67

        return (temperature - 32) / 1.8 + 273.15

    def convert(self, input_temperature, input_scale, output_scale) -> str:
        result = ''

        if input_scale in output_scale:
            result += f'Temperature in {input_scale} scale = ' + str(input_temperature) + '\n'

        if input_scale == Scale.CELSIUS:
            if Scale.KELVIN in output_scale:
                output_temperature = round(self.convert_celsius_kelvin_temperature(input_temperature), 2)
                result += f'Temperature in {Scale.KELVIN} scale = ' + str(output_temperature) + '\n'

            if Scale.FAHRENHEIT in output_scale:
                output_temperature = round(self.convert_celsius_fahrenheit_temperature(input_temperature), 2)
                result += f'Temperature in {Scale.FAHRENHEIT} scale = ' + str(output_temperature) + '\n'

        elif input_scale == Scale.KELVIN:
            if Scale.CELSIUS in output_scale:
                output_temperature = round(self.convert_celsius_kelvin_temperature(input_temperature, reverse=True), 2)
                result += f'Temperature in {Scale.CELSIUS} scale = ' + str(output_temperature) + '\n'

            if Scale.FAHRENHEIT in output_scale:
                output_temperature = round(self.convert_kelvin_fahrenheit_temperature(input_temperature), 2)
                result += f'Temperature in {Scale.FAHRENHEIT} scale = ' + str(output_temperature) + '\n'

        else:
            if Scale.CELSIUS in output_scale:
                output_temperature = round(self.convert_celsius_fahrenheit_temperature(input_temperature,
                                                                                       reverse=True), 2)
                result += f'Temperature in {Scale.CELSIUS} scale = ' + str(output_temperature) + '\n'

            if Scale.KELVIN in output_scale:
                output_temperature = round(self.convert_kelvin_fahrenheit_temperature(input_temperature,
                                                                                      reverse=True), 2)
                result += f'Temperature in {Scale.KELVIN} scale = ' + str(output_temperature) + '\n'

        return result
