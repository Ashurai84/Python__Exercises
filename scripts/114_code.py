#116  Implement a context manager using the with statement that opens a file, writes text, and closes the file automatically.


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Example usage
with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")
