from datetime import datetime, date
from langchain_core.prompts import ChatPromptTemplate
from utils.azure_openai import chat
#from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field, computed_field

class NoticeEmailExtract(BaseModel):
    date_of_notice_str: str | None = Field(
        default=None,
        exclude=True,
        repr=False,
        description="""The date of the notice (if any) reformatted
        to match YYYY-mm-dd""",
    )
    entity_name: str | None = Field(
        default=None,
        description="""The name of the entity sending the notice (if present
        in the message)""",
    )
    entity_phone: str | None = Field(
        default=None,
        description="""The phone number of the entity sending the notice
        (if present in the message)""",
    )
    entity_email: str | None = Field(
        default=None,
        description="""The email of the entity sending the notice
        (if present in the message)""",
    )
    project_id: int | None = Field(
        default=None,
        description="""The project ID (if present in the message) -
        must be an integer""",
    )
    site_location: str | None = Field(
        default=None,
        description="""The site location of the project (if present
        in the message). Use the full address if possible.""",
    )
    violation_type: str | None = Field(
        default=None,
        description="""The type of violation (if present in the
        message)""",
    )
    required_changes: str | None = Field(
        default=None,
        description="""The required changes specified by the entity
        (if present in the message)""",
    )
    compliance_deadline_str: str | None = Field(
        default=None,
        exclude=True,
        repr=False,
        description="""The date that the company must comply (if any)
        reformatted to match YYYY-mm-dd""",
    )
    max_potential_fine: float | None = Field(
        default=None,
        description="""The maximum potential fine
        (if any)""",
    )

    @staticmethod
    def _convert_string_to_date(date_str: str | None) -> date | None:
        if not date_str:
            return None

        formats = [
            "%Y-%m-%d",        # 2024-10-15
            "%B %d, %Y",       # October 15, 2024
            "%b %d, %Y",       # Oct 15, 2024
            "%m/%d/%Y",        # 10/15/2024
            "%d %B %Y",        # 15 October 2024
            "%d %b %Y",        # 15 Oct 2024
        ]

        for fmt in formats:
            try:
                parsed_date = datetime.strptime(date_str, fmt).date()
                return parsed_date.strftime("%Y-%m-%d")
            except ValueError:
                continue

        print(f"Failed to parse date: {date_str}")
        return None

    @computed_field
    @property
    def date_of_notice(self) -> date | None:
        return self._convert_string_to_date(self.date_of_notice_str)

    @computed_field
    @property
    def compliance_deadline(self) -> date | None:
        return self._convert_string_to_date(self.compliance_deadline_str)


info_parse_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Parse the date of notice, sending entity name, sending entity
            phone, sending entity email, project id, site location,
            violation type, required changes, compliance deadline, and
            maximum potential fine from the message. If any of the fields
            aren't present, don't populate them. Try to cast dates into
            the YYYY-mm-dd format. Don't populate fields if they're not
            present in the message.

            Here's the notice message:

            {message}
            """,
        )
    ]
)

#notice_parser_model = ChatOllama(model="deepseek-r1:14b", temperature=0)

NOTICE_PARSER_CHAIN = (
    info_parse_prompt
    | chat.with_structured_output(NoticeEmailExtract)
)