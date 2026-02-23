import gzip
import binascii

with open("HTML_interface.html", "rb") as f:
    html_data = f.read()

compressed = gzip.compress(html_data, compresslevel=9)

with open("camera_index.h", "w") as f:
    f.write("const uint8_t index_ov2640_html_gz[] = {")
    f.write(",".join("0x%02x" % b for b in compressed))
    f.write("};\n")
    f.write("const size_t index_ov2640_html_gz_len = sizeof(index_ov2640_html_gz);\n")

print("✅ camera_index.h generated successfully!")
