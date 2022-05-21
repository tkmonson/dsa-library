# Given a filename that denotes a text file of server responses, create an
#     output file (named "gifs_" + filename) that stores the names of the GIFs
#     acquired successfully via GET requests. The order of the names in the
#     output does not matter, but no duplicates are allowed.

path_prefix = "data/"
filename = "hosts_access_log_00.txt"

gifname_set = set()
with open(path_prefix + filename) as f:
    for line in f:
        record = line.split()

        request_method = record[5][1:]
        request_resource = record[6].split("/")[-1]
        response_code = int(record[8])

        if request_method == "GET" and response_code == 200:
            if request_resource.endswith((".gif", ".GIF")):
                gifname_set.add(request_resource + "\n")

with open(path_prefix + "gifs_" + filename, "w") as g:
    g.write("")

with open(path_prefix + "gifs_" + filename, "a") as g:
    for gifname in gifname_set:
        g.write(gifname)

