from csv_task.converter_csv_to_html import ConverterCsvToHtml

input_file = 'D:\\Python\\AcademIT_oop\\csv_task\\input.csv'
output_file_name = 'output.html'
csv_to_html = ConverterCsvToHtml()
csv_to_html.convert(input_file, output_file_name)
