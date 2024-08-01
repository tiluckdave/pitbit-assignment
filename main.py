from openai import OpenAI
import base64

client = OpenAI()

# Function to send the text to GPT-4 and get the JSON response
def resume_to_json(base64_resume):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You act as a resume parser and translating it to a structured JSON format."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": ""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_resume}"
                        },
                    },
                    {
                        "type": "text",
                        "text": "# Context\nAct as a resume parser. Your job is to parse all the important information from a resume which is provided in image format to you. All the information parsed must be structured properly in JSON format.\n\n# Objective\nYou must get all the details of the person from the resume and and understand all the headlines available in his/her resume and structure the json data accordingly. For e.g. data in the resume could be name, contact details such as phone number, email id, address, then there can be skills section, projects section, experiences, education, etc and more. Further each section might have details like experiences can have multiple experiences each having company name, job title, durations, skills worked on, description, etc and more. Your task is to identify such details properly and structure them in JSON format\n\n# Style\nKeep your style very simple. The response is ONLY a json block which contains the structured resume in JSON format\n\n# Audience\nConsider the audience for this chat to be developers who will use the structured resume in json format for further processing\n\n# Response\nBe concise, do not halucinate data, do not create any new data, Put the data parsed from the resume as it is without any change.\n"
                    }
                ]
            },
        ],
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

# Main function
def main():
    file_path = './resume.jpg'
    with open(file_path, "rb") as image:
        base64_resume = base64.b64encode(image.read()).decode('utf-8')
    resume_json = resume_to_json(base64_resume)
    print(resume_json)

if __name__ == '__main__':
    main()
