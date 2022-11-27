#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program adds two numbers

import random


def main():

    # process
    value = input("Please press to print all RGB values.")
    for r_value in range(0, 255):
        for g_value in range(0, 255):
            for b_value in range(0, 255):
                print("R {0} G {1} B {2}".format(r_value, g_value, b_value))
    print("\nDone.")


if __name__ == "__main__":
    main()
