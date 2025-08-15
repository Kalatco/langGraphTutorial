from graphs.notice_extraction import NOTICE_EXTRACTION_GRAPH

# Draw the graph to a PNG file
image_data = NOTICE_EXTRACTION_GRAPH.get_graph().draw_mermaid_png()
with open("notice_extraction_graph3.png", mode="wb") as f:
  f.write(image_data)