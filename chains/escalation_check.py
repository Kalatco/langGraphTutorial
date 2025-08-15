from utils.azure_openai import chat
#from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class EscalationCheck(BaseModel):
    needs_escalation: bool = Field(
        description="""Whether the notice requires escalation
        according to specified criteria"""
    )

escalation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Determine whether the following notice received
            from a regulatory body requires immediate escalation.
            Immediate escalation is required when {escalation_criteria}.

            Here's the notice message:

            {message}
            """,
        )
    ]
)

#escalation_check_model = ChatOllama(model="deepseek-r1:14b", temperature=0)

ESCALATION_CHECK_CHAIN = (
    escalation_prompt
    | chat.with_structured_output(EscalationCheck)
)
