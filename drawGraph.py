from graphs.notice_extraction import NOTICE_EXTRACTION_GRAPH
from graphs.email_agent import email_agent_graph

# Draw the graph to a PNG file
image_data = email_agent_graph.get_graph().draw_mermaid_png()
with open("email_agent.png", mode="wb") as f:
  f.write(image_data)