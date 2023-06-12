#!/usr/bin/env python3

# Autohint using a Blue Zone Reference Font and control instructions files,
# if available

import os
from ttfautohint import ttfautohint
from ttfautohint.options import parse_args as ttfautohint_parse_args
from fontTools.ttLib import TTFont


def get_control_file(file_path):
    """
    Join the control folder with the control file name.
    Return the control file path if it exists, otherwise return None.
    """
    control_folder = ["sources", "control-instructions"]
    control_ext = "control"
    file_name = os.path.basename(file_path)
    control_file = os.path.join(*control_folder, file_name[:-3] + control_ext)
    if not os.path.isfile(control_file):
        return None
    return control_file


def autohint_font(infile, outfile, parameters, control=None, reference=None):
    """Autohint a ttf font."""

    # Setup arguments
    font_name = os.path.basename(infile)

    print("\033[1mAUTOHINTING %s\033[0m" % (font_name))

    # Reference font argument
    if reference is not None:
        reference_arg = "--reference=%s" % (reference)
        print("Reference file: %s" % (os.path.basename(reference)))
        parameters.append(reference_arg)
    else:
        print("Reference file: no")

    # Control file argument
    if control is not None:
        control_arg = "--control-file=%s" % (control)
        print("Control file: %s" % (os.path.basename(control)))
        parameters.append(control_arg)
    else:
        print("Control file: no")

    # Assemble arguments
    args = ttfautohint_parse_args([
        infile,
        outfile,
        *parameters
    ])

    ttfautohint(**args)

    # Improve the appearance of a hinted font on Win platforms by enabling
    # the head table's flag 3.
    ttFont = TTFont(outfile)
    ttFont["head"].flags |= 1 << 3
    ttFont.save(outfile)


def main(args=None):
    """Process fonts."""

    cwd = os.getcwd()
    ttf_folder = os.path.join(cwd, "fonts", "ttf")

    parameters = [
        "--no-info",
        "--default-script=latn",
        "--fallback-script=latp",
        "--stem-width-mode=nnn"
    ]

    # Check if there is a ttf folder and it is not empty
    if not os.path.isdir(ttf_folder):
        print("ERROR: There is no \"fonts/ttf\" folder.")
        return
    if not os.listdir(ttf_folder):
        print("ERROR: The folder \"fonts/ttf\" is empty.")
        return

    # Check if there is a Regular font
    reference_font = None
    reference_font_path = None
    for file_name in os.listdir(ttf_folder):
        if file_name.endswith("-Regular.ttf"):
            reference_font = file_name
            break
    if reference_font:
        reference_font_path = os.path.join(cwd, ttf_folder, reference_font)
        autohint_font(
            reference_font_path,
            reference_font_path,
            parameters,
            get_control_file(reference_font_path),
        )

    # Autohint every other font
    for file_name in os.listdir(ttf_folder):
        if not file_name.endswith(".ttf"):
            continue
        if file_name == reference_font:
            continue

        font_path = os.path.join(cwd, ttf_folder, file_name)
        autohint_font(
            font_path,
            font_path,
            parameters,
            get_control_file(font_path),
            reference_font_path
        )


if __name__ == "__main__":
    main()
