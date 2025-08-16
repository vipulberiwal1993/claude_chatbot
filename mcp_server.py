from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# TODO: Write a tool to read a doc
@mcp.tool(
    name="read_doc_contents",
    description="Reads the content of the documents and return the answer in a string"
)
def read_document(doc_id: str = Field(description="Id of the document")):
    if doc_id not in docs:
        raise ValueError(f"Incorrect documentId:{doc_id}")
    return docs[doc_id]

# TODO: Write a tool to edit a doc
@mcp.tool(
    name="edit_doc_contents",
    description="Append the contents of the doc and return acknowledgment as True"
)
def write_doc(doc_id: str = Field(description="Id of the document"), content: str = Field("content of the document")):
    if doc_id not in docs:
        raise ValueError(f"Incorrect documentId:{doc_id}")
    docs[doc_id] += content
    return True




# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc



if __name__ == "__main__":
    mcp.run(transport="stdio")
