from utils.azure_openai import chat
#from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

class BinaryAnswer(BaseModel):
    is_true: bool = Field(
        description="""Whether the answer to the question is yes or no.
        True if yes otherwise False."""
    )

binary_question_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Answer this question as True for "yes" and False for "no".
            No other answers are allowed:

            {question}
            """,
        )
    ]
)

#binary_question_model = ChatOllama(model="deepseek-r1:14b", temperature=0)

BINARY_QUESTION_CHAIN = (
    binary_question_prompt
    | chat.with_structured_output(BinaryAnswer)
)
