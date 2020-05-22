""" main entry point """

import argparse
from os.path import exists, isabs, join, dirname
from pathlib import Path
from stegstash.imagelsb import encode, decode, simpleEncode, simpleDecode


def cli():
	""" command line interface """
	parser = argparse.ArgumentParser(
	description="Hide an recover data using the magic of steganograpy")
	# ImageLSB
	lsb = parser.add_subparsers(
	title="ImageLSB", description=
	"Hide and recover data from an image using Least Significant Bit steganography and variants"
	)
	lsbPasrser = lsb.add_parser("imagelsb")
	lsbPasrser.add_argument("--mode", help="Encode or decode")
	lsbPasrser.add_argument("--input-image", help="Path to the input image")
	lsbPasrser.add_argument("--output-image",
	help="Path to the output image (if applicable)")
	lsbPasrser.add_argument("--data-file",
	help="Path to the data file (if applicable)")
	lsbPasrser.add_argument("--iv", help="Initialisation vector (if applicable)")
	lsbPasrser.add_argument("--password", help="Password (if applicable)")

	args = parser.parse_args()

	# ImageLSB
	if args.mode.lower() == "encode":
		with open(args.data_file) as fileData:
			data = fileData.read()
		if args.iv:
			encode(args.input_image, args.output_image, data, args.iv, args.password)
		else:
			simpleEncode(args.input_image, args.output_image, data)
	if args.mode.lower() == "decode":
		if args.iv:
			data = decode(args.input_image, args.iv, args.password, True)
		else:
			data = simpleDecode(args.input_image, True)
		with open(args.data_file, "w") as fileData:
			fileData.write(data)


if __name__ == "__main__":
	cli()
