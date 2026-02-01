var yL1 = "ReadNotebook",
  Kd5 = 2000,
  Cd5 = 2000,
  Cg2 = "Read a file from the local filesystem.",
  Fg2 = `Reads a file from the local filesystem. You can access any file directly by using this tool.
Assume this tool is able to read all files on the machine. If the User provides a path to a file assume that path is valid. It is okay to read a file that does not exist; an error will be returned.

Usage:
- The file_path parameter must be an absolute path, not a relative path
- By default, it reads up to ${Kd5} lines starting from the beginning of the file
- You can optionally specify a line offset and limit (especially handy for long files), but it's recommended to read the whole file by not providing these parameters
- Any lines longer than ${Cd5} characters will be truncated
- Results are returned using cat -n format, with line numbers starting at 1
- This tool allows ${S2} to VIEW images (eg PNG, JPG, etc). When reading an image file the contents are presented visually as ${S2} is a multimodal LLM.
- For Jupyter notebooks (.ipynb files), use the ${yL1} instead
- When reading multiple files, you MUST use the ${jw} tool to read them all at once`;
