import xml.etree.ElementTree as ET

FILL = "#F1AB78"
FILL_PERCENTAGE = 50
NAMESPACE = "{http://www.w3.org/2000/svg}"

xml = ET.parse("input.svg")
svg = xml.getroot()
rect = svg.find(f".//{NAMESPACE}rect")

if rect is not None:
    rect.set("fill", FILL)
    rect.set("height", f"{FILL_PERCENTAGE}%")
    rect.set("y", f"{100 - FILL_PERCENTAGE}%")

ET.register_namespace("", NAMESPACE[1:-1])
xml.write("output.svg")
