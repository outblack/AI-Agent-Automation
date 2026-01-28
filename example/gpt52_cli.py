"""
Simple CLI example using the OpenAI Responses API.

Prerequisites:
  - Python 3.8+
  - `pip install openai`
  - Export OPENAI_API_KEY in your environment
"""

import base64
import mimetypes
import os

from openai import OpenAI


def _image_to_data_url(path: str) -> str:
    mime_type, _ = mimetypes.guess_type(path)
    if not mime_type:
        mime_type = "application/octet-stream"
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("Missing OPENAI_API_KEY. Set it in your environment.")

    prompt = input("Enter your prompt: ").strip()
    if not prompt:
        raise SystemExit("Prompt cannot be empty.")

    reasoning_effort = input(
        "Reasoning effort (low/medium/high). Press Enter to skip: "
    ).strip()

    image_paths_input = input(
        "Image paths (comma-separated). Press Enter to skip: "
    ).strip()

    image_paths = [path.strip() for path in image_paths_input.split(",") if path.strip()]

    client = OpenAI(api_key=api_key)

    content = [{"type": "input_text", "text": prompt}]
    if image_paths:
        for path in image_paths:
            content.append(
                {
                    "type": "input_image",
                    "image_url": _image_to_data_url(path),
                }
            )

    request_kwargs = {
        "model": "gpt-5.2",
        "input": [
            {
                "role": "user",
                "content": content,
            }
        ],
    }
    if reasoning_effort:
        request_kwargs["reasoning_effort"] = reasoning_effort

    response = client.responses.create(**request_kwargs)

    print(response.output_text)


if __name__ == "__main__":
    main()
