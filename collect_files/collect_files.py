"""
Remake a large directory of training data
into a small testing set
Author: Josh McGrath
"""

import os
from os.path import join
import shutil
import click


def copy_files(in_dir, out_dir, nfiles):
    files = os.listdir(in_dir)
    firstn = files[:nfiles]
    for f in firstn:
        if os.path.isdir(join(in_dir,f)):
            raise ValueError(f"Unexpected Directory {join(in_dir, f)}")
        else:
            shutil.copyfile(join(in_dir, f), join(out_dir,f))


def collect(parent, out, nfiles):
    if os.path.isdir(out):
        raise ValueError(f"directory {out} exists, exiting without copy")
    os.mkdir(out)
    struct = os.listdir(parent)
    for listing in struct:
        if os.path.isdir(join(parent,listing)):
            os.mkdir(join(out, listing))
            copy_files(join(parent, listing), join(out, listing), nfiles)
        else:
            shutil.copyfile(join(parent, listing), join(out,listing))

@click.command()
@click.argument("parent")
@click.option("--out", default="out", help="entrypoint of copied directory")
@click.option("--n", default=3, help="number of files to copy from each subdirectory")
def main(parent, out, nfiles):
    collect(parent,out, nfiles)


if __name__ == "__main__":
    main()
