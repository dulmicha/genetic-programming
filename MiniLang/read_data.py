def read_data(file_path):
    inputs = []
    outputs = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(';')
                if len(parts) == 2:
                    input_parts = parts[0].strip().split(' ')
                    output_parts = parts[1].strip().split(' ')

                    input_values = [int(val) for val in input_parts if val]
                    output_values = [int(val) for val in output_parts if val]
                    inputs.append(input_values)
                    outputs.append(output_values)

    return inputs, outputs
