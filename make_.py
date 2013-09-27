in_ = open("res_.csv", "r")
out_ = open("rf_11.csv", "w")

out_.write("id,ACTION\n")

i = 1
for line in in_.xreadlines():
    out_.write(str(i)+","+line.strip()+"\n")
    i += 1

in_.close()
out_.close()

