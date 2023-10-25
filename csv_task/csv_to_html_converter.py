class CsvToHtmlConverter:
    def __init__(self):
        self.__csv_file = None
        self.__html_file = None

    @staticmethod
    def __add_tags_on_top(path):
        with open(path, 'w', encoding='utf-8') as html_file:
            html_file.write('<!DOCTYPE html>\n')
            html_file.write('<html lang="ru">\n')
            html_file.write('\t<head>\n')
            html_file.write('\t\t<meta charset="UTF-8">\n')
            html_file.write('\t\t<title>Convert CSV to HTML</title>\n')
            html_file.write('\t</head>\n')
            html_file.write('\t<body>\n')
            html_file.write('\t\t<table border="1">\n')

    @staticmethod
    def __add_tags_on_bottom(path):
        with open(path, 'a', encoding='utf-8') as html_file:
            html_file.write('\t\t</table>\n')
            html_file.write('\t</body>\n')
            html_file.write('</html>\n')

    def __convert(self):
        quotes_count = 0

        for line in self.__csv_file:
            if line == '\n':
                continue

            if quotes_count == 0:
                self.__html_file.write('\t\t\t<tr>\n')
                self.__html_file.write('\t\t\t\t<td>')

            i = 0

            while i < len(line):
                if line[i] == '"':
                    quotes_count += 1

                    if i != 0 and line[i - 1] == '"':
                        if quotes_count % 2 != 0 and quotes_count != 1:
                            self.__html_file.write(line[i])

                    i += 1
                    continue

                if line[i] == ',':
                    if quotes_count % 2 != 0:
                        self.__html_file.write(line[i])
                        i += 1
                        continue

                    self.__html_file.write('</td>\n')
                    self.__html_file.write('\t\t\t\t<td>')
                    i += 1
                    continue

                if line[i] == '&':
                    self.__html_file.write('&amp;')
                    i += 1
                    continue

                if line[i] == '<':
                    self.__html_file.write('&lt;')
                    i += 1
                    continue

                if line[i] == '>':
                    self.__html_file.write('&gt;')
                    i += 1
                    continue

                if line[i] == '\n':
                    if quotes_count % 2 != 0:
                        self.__html_file.write('<br>')
                        i += 1
                        continue

                    self.__html_file.write('\t\t\t\t</td>\n')
                    self.__html_file.write('\t\t\t</tr>\n')
                    quotes_count = 0
                    i += 1
                    continue

                self.__html_file.write(line[i])
                i += 1

    def convert(self, csv_file_path, html_file_path):
        self.__add_tags_on_top(html_file_path)

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as self.__csv_file, \
                    open(html_file_path, 'a', encoding='utf-8') as self.__html_file:
                self.__convert()
        except FileNotFoundError:
            raise FileNotFoundError('File not find')

        self.__add_tags_on_bottom(html_file_path)
