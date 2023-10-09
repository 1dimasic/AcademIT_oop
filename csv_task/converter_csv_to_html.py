class ConverterCsvToHtml:
    def __init__(self):
        self.__string = None
        self.__csv_file_name = None
        self.__directory = None
        self.__html_file_name = None

    def __add_tags_to_html(self, position):
        if position == 'top':
            with open(self.__directory + self.__html_file_name, 'w', encoding='utf-8') as html_file:
                html_file.write('<!DOCTYPE html>\n')
                html_file.write('<html>\n')
                html_file.write('\t<head>\n')
                html_file.write('\t\t<meta charset = "UTF-8">\n')
                html_file.write('\t\t<title>Convert CSV to HTML</title>\n')
                html_file.write('\t</head>\n')
                html_file.write('\t<body>\n')
                html_file.write('\t\t<table border="1">\n')

        if position == 'bottom':
            with open(self.__directory + self.__html_file_name, 'a', encoding='utf-8') as html_file:
                html_file.write('\t\t</table>\n')
                html_file.write('\t</body>\n')
                html_file.write('</html>\n')

    def convert(self, path_to_csv_file, output_file_name):
        self.__csv_file_name = path_to_csv_file[path_to_csv_file.rfind('\\') + 1:]
        self.__directory = path_to_csv_file[:path_to_csv_file.rfind('\\') + 1]
        self.__html_file_name = output_file_name

        self.__add_tags_to_html('top')

        with open(path_to_csv_file, 'r', encoding='utf-8') as csv_file:
            input_line = ''
            output_line = ''
            quotes_count = 0

            for line in csv_file:
                if line == '\n':
                    continue

                for symbol in line:
                    if symbol == '"':
                        quotes_count += 1

                input_line += line

                if quotes_count % 2 != 0:
                    continue

                current_index = 0
                quotes_count = 0

                for i in range(len(input_line)):
                    if input_line[i] == '"':
                        quotes_count += 1
                        continue

                    if input_line[i] == ',':
                        if quotes_count == 0:
                            output_line += input_line[current_index:i] + ';'
                            current_index = i + 1
                            continue

                        if quotes_count % 2 == 0:
                            output_line += input_line[current_index + 1:i - 1] + ';'
                            current_index = i + 1
                            quotes_count = 0

                if quotes_count == 0:
                    output_line += input_line[current_index:]
                else:
                    output_line += input_line[current_index + 1:-1]

                i = 0

                while i < len(output_line) - 1:
                    if output_line[i] == '"' and output_line[i + 1] == '"':
                        output_line = output_line[:i] + output_line[i + 1:]

                    i += 1

                i = 0

                while i < len(output_line):
                    if output_line[i] == '&':
                        output_line = output_line[:i + 1] + 'amp' + output_line[i + 1:]
                        i += 4

                    if output_line[i] == '<':
                        output_line = output_line[:i] + '&lt' + output_line[i + 1:]
                        i += 3

                    if output_line[i] == '>':
                        output_line = output_line[:i] + '&gt' + output_line[i + 1:]
                        i += 3

                    if output_line[i] == '\n':
                        output_line = output_line[:i] + '<br/>' + output_line[i + 1:]
                        i += 4

                    i += 1

                self.__string = output_line[:]
                self.__write_html()

                input_line = ''
                output_line = ''
                quotes_count = 0

        self.__add_tags_to_html('bottom')

    def __write_html(self):
        with open(self.__directory + self.__html_file_name, 'a', encoding='utf-8') as html_file:
            i = 0
            current_index = 0
            html_file.write('\t\t\t<tr>\n')

            while i < len(self.__string):
                if self.__string[i] == ';':
                    html_file.write('\t\t\t\t<td>' + self.__string[current_index:i] + '</td>\n')
                    current_index = i + 1

                i += 1

            html_file.write('\t\t\t\t<td>' + self.__string[current_index:] + '</td>\n')

            html_file.write('\t\t\t</tr>\n')
