import os
import sys
import soundfile as sf
import wavio


def dtype_to_sampwidth(dtype):
    if dtype == 'int8':
        return 1
    elif dtype == 'int16':
        return 2
    elif dtype == 'int32':
        return 4
    else:
        raise ValueError("Unsupported data type: {}".format(dtype))


def convert_aif_to_wav(input_folder, output_folder):
    for file in os.listdir(input_folder):
        if file.endswith(".aif") or file.endswith(".aiff"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(
                output_folder, os.path.splitext(file)[0] + ".wav")

            data, samplerate = sf.read(input_path)

            # Convert the data type to int16
            data = (data * (2**15 - 1)).astype('int16')

            sampwidth = dtype_to_sampwidth(data.dtype.name)
            wavio.write(output_path, data, samplerate, sampwidth=sampwidth)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        input_folder = r""  # Write your input folder des
        output_folder = r""  # Write your output des
        convert_aif_to_wav(input_folder, output_folder)
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        convert_aif_to_wav(input_folder, output_folder)
