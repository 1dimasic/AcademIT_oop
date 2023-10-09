with open('input.csv', 'r', encoding='utf-8') as csv_file:
    input_line = ''
    output_line = ''
    quotes_count = 0

    for line in csv_file:
        input_line += line
        quotes_count += line.count('"')

        if quotes_count % 2 != 0:
            continue

        if input_line == '\n':
            input_line = ''
            quotes_count = 0
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

        for i in range(len(output_line) - 1):
            if output_line[i] == '"' and output_line[i + 1] == '"':
                output_line = output_line[:i] + output_line[i + 1:]

    print(output_line)

    #         for i in range(len(row)):
    #             row[i] = row[i].replace('""', '"')
    #             row[i] = row[i].replace('\n', '<br/>')
    #
    #         self.__data.append(row)
    #
    #         input_line = ''
    #         quotes_count = 0
    #
    # self.__write_html()
