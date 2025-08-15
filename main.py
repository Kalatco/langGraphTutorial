# from chains.notice_extraction import NOTICE_PARSER_CHAIN
# from chains.escalation_check import ESCALATION_CHECK_CHAIN

# from graphs.notice_extraction import NOTICE_EXTRACTION_GRAPH
from example_emails import EMAILS

from graphs.email_agent import email_agent_graph

# Example usage:
# res = NOTICE_PARSER_CHAIN.invoke({"message": EMAILS[0]})

# res = ESCALATION_CHECK_CHAIN.invoke({
# 	"message": "Several cracks in the foundation have been identified along with water leaks and damage.",
# 	"escalation_criteria": "There is currently water damage or potential water damage reported"
# })

# res = ESCALATION_CHECK_CHAIN.invoke({
# 	"message":  "The wheel chair ramps are too steep",
# 	"escalation_criteria": "There is currently water damage or potential water damage reported"
# })

# print(res)

# --------------

# initial_state_no_escalation = {
#   "notice_message": EMAILS[0],
#   "notice_email_extract": None,
#   "escalation_text_criteria": "There's a risk of fire or water damage at the site",
#   "escalation_dollar_criteria": 100_000,
#   "requires_escalation": False,
#   "escalation_emails": ["brog@abc.com", "bigceo@company.com"],
#  }

# no_esc_result = NOTICE_EXTRACTION_GRAPH.invoke(initial_state_no_escalation)
# print(no_esc_result["requires_escalation"])
# print(no_esc_result["follow_ups"])

# initial_state_escalation = {
#   "notice_message": EMAILS[0],
#   "notice_email_extract": None,
#   "escalation_text_criteria": "Workers explicitly violating safety protocols",
#   "escalation_dollar_criteria": 100_000,
#   "requires_escalation": False,
#   "escalation_emails": ["brog@abc.com", "bigceo@company.com"],
#  }


# esc_result = NOTICE_EXTRACTION_GRAPH.invoke(initial_state_escalation)
# print(esc_result["requires_escalation"])
# if ('follow_ups' in esc_result):
#   print(esc_result["follow_ups"])

# -----------------

message_1 = {"messages": [("human", EMAILS[1])]}

for chunk in email_agent_graph.stream(message_1, stream_mode="values"):
  chunk["messages"][-1].pretty_print()