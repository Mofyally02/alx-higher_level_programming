#!/usr/bin/python3
"""Defines a file-writting function."""

def write_file(filename="", text=""):
	"""Write a string to a UTF8 text file.

	Args:
		filename (str): The name of the file to write.
		text (str): The text to writer to the file.
	Returns:
		The number of the characters written.
	"""
	wirth open(filename="w", encoding="utf-8") as f:
	return f.write(text)
