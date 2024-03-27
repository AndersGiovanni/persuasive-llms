for fname in ["argument_image_urls.txt", "control_image_urls.txt"]:

    lines = []

    with open(fname, "r") as infile:
        for line in infile:
            if not line.strip():
                continue
            lines.append(
                "https://tools.danskspeedcubingforening.dk/dontlook/svg_img/" + line.strip().rsplit("/", maxsplit=1)[-1].rsplit(".", maxsplit=1)[0].strip() + ".svg"
            )

    with open(f"new_{fname}", "w") as outfile:
        outfile.write("\n".join(lines))
