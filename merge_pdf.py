import argparse
import glob
import os
from PyPDF2 import PdfMerger


def main(folder):
    merger = PdfMerger()
    input_path = os.path.join(folder, "*")
    output_path = os.path.join(folder, "merged.pdf")
    files = glob.glob(input_path)
    files.sort()
    for file in files:
        merger.append(file)
    merger.write(output_path)
    merger.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ファイル名順にPDFをマージ") 
    parser.add_argument("folder", help="PDFの入ったフォルダ。出力もそこに出る")
    args = parser.parse_args()
    folder = args.folder

    main(folder)
