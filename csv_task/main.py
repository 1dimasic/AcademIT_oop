from csv_task.csv_to_html_converter import CsvToHtmlConverter

csv_file_path = 'D:\\Python\\AcademIT_oop\\csv_task\\input.csv'
html_file_path = 'D:\\Python\\AcademIT_oop\\csv_task\\output.html'
csv_to_html = CsvToHtmlConverter()
csv_to_html.convert(csv_file_path, html_file_path)
